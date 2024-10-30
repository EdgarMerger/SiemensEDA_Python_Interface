readme_content = """
# Python Script for Processing Class Files with Type Hinting

This Python script automates the processing of a source file, extracts class information, and generates a new output file with additional information on properties, including type hints and accessibility attributes. It also provides utilities for file management, cleanup, and organized output.
This script was run with Xpedition Designer VX.2.13 installed, so it has created ifc file for Xpedition Designer.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Script Details](#script-details)
- [License](#license)

## Overview

This script is designed to parse an input file (like `designer_orig.py`) containing class definitions, and it generates an enhanced output file (`designer.py`) with additional type hinting and access control attributes for properties. The script automates file generation, processing, copying, and cleanup, making it useful for updating code files with type and access information.

## Features

- **Class Parsing**: Parses class definitions and processes `get` and `put` property mappings.
- **Type Hinting**: Adds type hints (e.g., `bool`, `int`, `str`) to properties based on preset lists.
- **Access Control**: Annotates properties as `read_only`, `write_only`, or `read/write`.
- **File Management**: Automates generation, movement, and cleanup of files.

## Requirements

- **Python 3.6+**
- `makepy.py` file should be present for generating input data.

## Usage

### Steps to Run the Script

1. Place `makepy.py` in the same directory as this script.
2. Run the script:
    ```bash
    python sniff_designer_ifc.py
    ```
3. The script will perform the following steps automatically:
   - Generate an input file (`designer_orig.py`) using `makepy.py`.
   - Process the file and output `designer_ifc.py` with added type hints and access attributes.
   - Copy the generated file to the desired directory.
   - Cleanup temporary files created during the process.

### Functions Overview

- **`generate_input()`**: Runs `makepy.py` to create an initial input file (`designer_orig.py`) based on specified parameters.
- **`generate_output()`**: Reads `designer_orig.py`, processes classes, and writes annotated data to `designer_ifc.py`.
- **`copy_result()`**: Moves `designer_ifc.py` to the target directory.
- **`cleanup()`**: Deletes `designer_orig.py` after processing.

## Script Details

The core function in this script is `process_file()`, which:
- Reads `get` and `put` property mappings in classes.
- Annotates property types and access control.
- Collects class names for module-wide imports.

Key lists, `t_bool` and `t_int`, define type mappings for specific properties (`bool`, `int`). Unknown properties are annotated as `str`.

## License

This project is open-source and available under the [MIT License](LICENSE).
"""

