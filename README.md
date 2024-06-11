# File Organizer

## Overview
This Python script helps organize files in a specified directory based on predefined categories and keywords. It categorizes files into separate lists based on keywords present in their filenames and allows users to select and open files within a chosen category using their system's default program.

## Requirements
- Python 3.x
- tkinter library (for GUI file dialog)
- Operating System: Windows, macOS, Linux

## Usage
1. Run the script.
2. Select a directory containing files to organize.
3. Choose a category to view files within that category.
4. Select a file to open it with the default program associated with its file type.
5. Continue selecting categories or choose to exit the program.

## Functionality
- **CategoriseFiles**: Separates files into different categories based on keywords specified in the `DictionaryOfKeywords` dictionary and predefined categories in `NameOfCategories`.
- **RunCode**: Prompts the user to choose a category or exit the program.
- **ShowBooks**: Displays the contents of a selected category and prompts the user to select a specific file to open.
- **SelectBooks**: Opens the selected file with the default program.
- **open_file_with_default_program**: Platform-specific function to open a file using the system's default program.

## Example
Suppose you have a directory containing various PDF files related to business and programming topics. Running this script allows you to organize these files into separate categories (e.g., "Business", "Programming") and quickly access files within a chosen category.

## Note
- Ensure that the required libraries (e.g., `tkinter`) are installed.
- The script supports Windows, macOS, and Linux operating systems.
- Customization: Modify the `DictionaryOfKeywords` and `NameOfCategories` variables to suit your specific file organization needs.
