# Folder Structure Export Script

## Overview

This Python script is designed to generate a detailed folder structure of your project and save it in a `folder_structure.txt` file. It traverses the project directory from the root level and respects certain exclusion rules for both directories and files. It can also parse and honor patterns from a `.gitignore` file, helping you export an accurate representation of your project’s structure.

## Features

- **Directory and File Exclusion**: You can specify folders or files to exclude during the folder structure export.
- **Gitignore Parsing**: Automatically detects and respects exclusion patterns defined in your project's `.gitignore`.
- **Customizable Exclusions**: You can define additional files and directories to exclude beyond those specified in `.gitignore`.
- **Exports as Text**: The folder structure is output to a text file (`folder_structure.txt`) with indentation representing folder hierarchy.

## Usage

### Requirements

- Python 3.x

  > create and test on : `Python 3.12.4`

  - Ensure that pc contains python installed on it.
  - Execute the follow command to check terminal "cmd,powershell":
  - ```bash
    python --version
    ```
  - Should see output Like this :
  - ```bash
    Python 3.12.4
    ```

### Steps to Use the Script

1.  **Clone or Download** the script and place it in the root directory of your project.
2.  **Run the Script**:

    - Ensure that you are at the root of your project folder.
    - Execute the script using Python:

      ```bash
      python export_structure.py
      ```

3.  **Output**:

    - A file named `folder_structure.txt` will be generated in your project root, containing the folder structure based on your project’s hierarchy.
    - Excluded files inside specified folders (e.g., `public/*`, `src/test/*`, etc.) will not appear in the exported structure.

### Example

Given the following directory structure:

```css
project-root/
├── src/
│   ├── main.py
│   ├── test/
│   │   └── test_main.py
├── public/
│   └── index.html
├── .gitignore
└── README.md
```

And exclusions specified as:

- Exclude all files inside `public/`, `src/test/`, `.vscode/`, `.next/`, `.github/`.

The generated `folder_structure.txt` will look like this:

```css
project-root/
    src/
        main.py
    public/
    .gitignore
    README.md
```

Notice that the `public/` folder is included but its files are excluded, and `test_main.py` inside `src/test/` is excluded.

## Configuration

### Excluding Directories

To exclude entire directories (e.g., `node_modules`, `.git`), add them to the `exclude_directories` list in the script:

```python
exclude_directories = ['node_modules', '.git']
```

### Excluding Files Inside Specific Folders

To exclude files inside specific folders (e.g., `public/*`, `src/test/*`), add them to the `exclude_directories_files` list:

```python
exclude_directories_files = ['public/*', 'src/test/*', '.vscode/*', '.next/*', '.github/*']
```

These patterns will ensure that only the files inside these directories are excluded, while the folders themselves remain visible in the output.

### .gitignore Parsing

The script automatically parses `.gitignore` in the root folder to exclude files or directories based on the rules defined in it.

## Important Notes

- The script must be run from the **root of your project** to ensure it captures all relevant files and folders.
- The exclusions are flexible, and you can modify them as needed for your specific project structure.

---

### License

This script is open for use in any project.
