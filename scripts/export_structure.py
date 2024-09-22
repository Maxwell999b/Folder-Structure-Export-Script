import os
import fnmatch

def parse_gitignore(gitignore_path):
    """Parses the .gitignore file and returns a list of patterns."""
    if not os.path.exists(gitignore_path):
        return []
    
    exclude_patterns = []
    with open(gitignore_path, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            # Ignore comments and empty lines
            if stripped_line and not stripped_line.startswith('#'):
                exclude_patterns.append(stripped_line)
    
    return exclude_patterns

def should_exclude(path, exclude_patterns, start_path, is_directory=False):
    """Determines if a given path should be excluded based on patterns."""
    rel_path = os.path.relpath(path, start_path)
    
    for pattern in exclude_patterns:
        # Handle directory patterns with a trailing slash
        if pattern.endswith('/') and is_directory:
            if rel_path.startswith(pattern.rstrip('/')):
                return True
        
        # Handle wildcard patterns for files inside specific folders
        if pattern.endswith('/*') and not is_directory:
            if fnmatch.fnmatch(rel_path, pattern):
                return True
        
        # Handle standard wildcard patterns for files or directories
        if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(os.path.basename(rel_path), pattern):
            return True
    
    return False

def export_folder_structure(start_path, output_file, exclude_dirs=None, exclude_files=None):
    """Exports the folder structure to a text file, respecting exclusion patterns."""
    if exclude_dirs is None:
        exclude_dirs = []
    if exclude_files is None:
        exclude_files = []

    # Parse .gitignore patterns
    gitignore_path = os.path.join(start_path, '.gitignore')
    gitignore_patterns = parse_gitignore(gitignore_path)

    # Combine all exclusion patterns
    all_exclude_patterns = exclude_dirs + gitignore_patterns + exclude_files

    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(start_path):
            rel_path = os.path.relpath(root, start_path)
            if rel_path == '.':
                rel_path = ''

            # Exclude directories based on the combined patterns
            dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d), all_exclude_patterns, start_path, is_directory=True)]
            
            # Write the folder structure
            level = rel_path.count(os.sep)
            indent = ' ' * 4 * level
            f.write(f'{indent}{os.path.basename(root)}/\n')
            
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                # Exclude files based on the combined patterns
                if not should_exclude(os.path.join(root, file), all_exclude_patterns, start_path):
                    f.write(f'{sub_indent}{file}\n')

# Usage
start_directory = '.'  # Current directory
output_file = 'folder_structure.txt'
exclude_directories = ['node_modules', '.git']  # Add any additional directories to exclude
exclude_directories_files = ['public/*', 'src/test/*','.vscode/*','.next/*','.github/*']  # Exclude only files inside specified folders

export_folder_structure(start_directory, output_file, exclude_directories, exclude_directories_files)
print(f"Folder structure exported to {output_file}")
