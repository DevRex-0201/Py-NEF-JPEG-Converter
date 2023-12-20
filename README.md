# NEF to JPEG Converter

## Overview

This Python script provides a simple graphical user interface (GUI) for converting Nikon Raw Image files (.NEF) to JPEG format. It uses the Tkinter library for the GUI and the Python Imaging Library (PIL) for image conversion. The script allows you to specify the source folder containing NEF files, the destination folder for the converted JPEGs, as well as the quality and DPI settings for the output images.

## Features

- User-friendly GUI for selecting the source folder.
- Converts NEF files to JPEG format with customizable quality and DPI settings.
- Preserves the original image size.

## Requirements

- Python 3.x
- Pillow (PIL fork) library
- Tkinter library (usually included with Python)

## Installation

1. Clone this repository to your local machine or download the script.

   ```bash
   git clone https://github.com/yourusername/nef-to-jpeg-converter.git
   ```

2. Install the required libraries using pip:

   ```bash
   pip install pillow
   ```

## Usage

1. Run the script by executing `nef_to_jpeg_converter.py`.

2. The GUI will appear, allowing you to select the source folder containing NEF files.

3. Specify the destination folder where the converted JPEGs will be saved.

4. Set the quality (0-100) and DPI (dots per inch) for the output images. (Defaults to quality=95 and dpi=(300, 300))

5. Click the "Convert" button to start the conversion process.

6. Progress and completion messages will be displayed in the console.

## Example

```python
python nef_to_jpeg_converter.py
```

## Notes

- The script processes all .NEF files in the source folder and saves the converted JPEGs in the specified destination folder.

- Original image sizes are preserved in the converted JPEGs.

- Any errors encountered during the conversion process will be displayed in the console.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Pillow (PIL Fork)](https://pillow.readthedocs.io/en/stable/index.html) - Python Imaging Library used for image conversion.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI library.
