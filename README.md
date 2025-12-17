# Rotate Images to Landscape Format

A Python script that automatically rotates portrait images 90 degrees to landscape format.

## Installation

1. Install Python 3.7 or later
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Simplest way (Windows):

#### Option 1 - Drag and drop folder onto `rotate_images_drag_drop.bat`:

1. Open File Explorer and find the folder with your images
2. Drag the folder and drop it onto the file `rotate_images_drag_drop.bat`
3. The script automatically processes all images in that folder

#### Option 2 - Drag and drop folder onto `rotate_images.py`:

1. Open File Explorer and find the folder with your images
2. Drag the folder and drop it onto the file `rotate_images.py`
3. The script automatically processes all images in that folder

### From Command Line:

Run the script in the folder where your images are:

```bash
python rotate_images.py
```

Or specify a specific folder:

```bash
python rotate_images.py C:\path\to\folder
```

## Features

- Scans all images in the folder
- Automatically identifies portrait images (height > width)
- Rotates portrait images 90 degrees to landscape format
- **Preserves original quality** - no quality loss during rotation
- Ignores video files
- Supports common image formats: JPG, PNG, BMP, GIF, TIFF, WEBP, HEIC
- Replaces original files (backup before running if you want to keep originals)

## Warning

⚠️ **Important**: The script replaces original files. Backup your images before running the script if you want to keep the original versions.
