# File Reference Checker

File Reference Checker is a Python script designed to analyze files in a specified directory and find unreferenced files.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Collect All Files:** Recursively collects all files in a specified directory and its subdirectories.

- **Filter Files by Extensions:** Filters files based on specified target file extensions (e.g., .html, .css).

- **Search for File References:** Identifies unreferenced files by analyzing the content of interesting files within the directory.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mohanGups/file-reference-checker.git
   ```

2. **Navigate to the Repository:**
   ```bash
   cd file-reference-checker
   ```

3. **Run the Script:**
   ```bash
   python file_reference_checker.py
   ```

4. **Adjust Configuration:**
   - Modify the `directory` variable in the script to point to the target directory.
   - Customize the `interesting_extensions` list to include file extensions of interest (e.g., [".html", ".css"]).

5. **Review Unreferenced Files:**
   - The script will output files with no references found.

## Installation

No installation is required. Clone the repository and run the script as described in the [Usage](#usage) section.

## Dependencies

The script has no external dependencies. It uses standard Python libraries for file and directory operations.

## Contributing

If you find issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.