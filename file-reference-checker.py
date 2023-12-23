"""
MIT License

Copyright (c) 2024 K. Mohan Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os


def get_file_extension(file_path):
    """
    Get the file extension from a given file path.

    Args:
        file_path (str): The path of the file.

    Returns:
        str: The file extension.
    """
    try:
        _, extension = os.path.splitext(file_path)
        return extension
    except Exception as e:
        print(f"Error in get_file_extension: {e}")
        return None


def collect_all_files(directory):
    """
    Collect all files in the given directory and its subdirectories.

    Args:
        directory (str): The directory to search for files.

    Returns:
        list: A list of file paths.
    """
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        all_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                current_file_path = os.path.join(root, file)
                all_files.append(current_file_path)
        return all_files
    except Exception as e:
        print(f"Error in collect_all_files: {e}")
        return []


def filter_files_by_extensions(file_list, target_extensions):
    """
    Filter a list of files based on specified target extensions.

    Args:
        file_list (list): List of file paths.
        target_extensions (list): List of target file extensions.

    Returns:
        list: Filtered list of file paths.
    """
    try:
        filtered_files = [
            file for file in file_list if get_file_extension(file) in target_extensions
        ]
        return filtered_files
    except Exception as e:
        print(f"Error in filter_files_by_extensions: {e}")
        return []


def search_file_references(interesting_files, all_files):
    """
    Search for references to interesting files within other files.

    Args:
        interesting_files (list): List of files to search for references.
        all_files (list): List of all files.

    Returns:
        list: Unreferenced files.
    """
    try:
        unreferenced_files = []
        for file in all_files:
            reference_count = 0
            for interesting_file in interesting_files:
                try:
                    with open(interesting_file, "r", encoding="utf-8") as f:
                        content = f.read()
                        basename = os.path.basename(file)
                        if interesting_file != file and basename in content:
                            reference_count += 1
                except UnicodeDecodeError as decode_error:
                    print(
                        f"UnicodeDecodeError in search_file_references: {decode_error} ({interesting_file})"
                    )
            if reference_count == 0:
                unreferenced_files.append(file)
        return unreferenced_files
    except Exception as e:
        print(f"Error in search_file_references: {e}")
        return []


if __name__ == "__main__":
    # Set the directory path
    directory = os.path.abspath("/relative/path/to/your/directory")

    # Collect all files in the directory
    all_files = collect_all_files(directory)

    # Filter interesting files by extensions
    interesting = filter_files_by_extensions(all_files, [".html", ".css"])

    # Search for unreferenced files
    unreferenced = search_file_references(interesting, all_files)

    # Print unreferenced files
    if len(unreferenced) > 0:
        for file in unreferenced:
            print("No references found for: " + file)
