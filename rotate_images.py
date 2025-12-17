#!/usr/bin/env python3
"""
Script to rotate portrait images to landscape format.
Iterates through all images in the current directory and rotates portrait images 90 degrees.
"""

import os
import sys
from PIL import Image
from pathlib import Path

# Supported image formats
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.tif', '.webp', '.heic', '.heif'}

def is_image_file(file_path):
    """Checks if the file is an image."""
    ext = Path(file_path).suffix.lower()
    return ext in IMAGE_EXTENSIONS


def is_portrait(image):
    """Checks if the image is in portrait format."""
    width, height = image.size
    return height > width


def rotate_image(image_path):
    """Rotates a portrait image 90 degrees to landscape format."""
    try:
        # Open image
        with Image.open(image_path) as img:
            # Check if image is portrait
            if not is_portrait(img):
                print(f"  Skipping {image_path.name} - already landscape ({img.size[0]}x{img.size[1]})")
                return False
            
            # Rotate 90 degrees
            rotated = img.rotate(90, expand=True)
            
            # Save the rotated image (replaces original)
            # Maintain maximum quality - no compression or quality loss
            ext = image_path.suffix.lower()
            
            if ext in ['.jpg', '.jpeg']:
                # JPEG: maximum quality (100), no optimization that might degrade quality
                rotated.save(image_path, quality=100, optimize=False)
            elif ext == '.png':
                # PNG: lossless, no compression
                rotated.save(image_path, compress_level=0)
            elif ext == '.tiff' or ext == '.tif':
                # TIFF: lossless compression
                rotated.save(image_path, compression='tiff_lzw')
            elif ext == '.webp':
                # WebP: lossless
                rotated.save(image_path, lossless=True)
            else:
                # For other formats: save without compression if possible
                rotated.save(image_path)
            
            print(f"  ✓ Rotated {image_path.name} ({img.size[0]}x{img.size[1]} -> {rotated.size[0]}x{rotated.size[1]})")
            return True
            
    except Exception as e:
        print(f"  ✗ Error processing {image_path.name}: {str(e)}")
        return False


def process_directory(directory_path='.'):
    """Iterates through all images in a directory and rotates portrait images."""
    directory = Path(directory_path)
    
    if not directory.exists():
        print(f"Error: Directory '{directory_path}' does not exist.")
        return
    
    if not directory.is_dir():
        print(f"Error: '{directory_path}' is not a directory.")
        return
    
    print(f"Processing images in: {directory.absolute()}")
    print("-" * 60)
    
    # Get all files in the directory
    image_files = [f for f in directory.iterdir() if f.is_file() and is_image_file(f)]
    
    if not image_files:
        print("No image files found in the directory.")
        return
    
    print(f"Found {len(image_files)} image file(s).\n")
    
    rotated_count = 0
    skipped_count = 0
    
    for image_file in image_files:
        if rotate_image(image_file):
            rotated_count += 1
        else:
            skipped_count += 1
    
    print("-" * 60)
    print(f"Done! Rotated: {rotated_count}, Skipped: {skipped_count}")


if __name__ == "__main__":
    # If a directory is provided as an argument, use it, otherwise use current directory
    # Support for drag-and-drop: if a file is dropped on the script, use its directory
    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1])
        if target_path.is_file():
            # If it's a file, use its parent directory
            target_dir = str(target_path.parent)
        elif target_path.is_dir():
            # If it's a directory, use it directly
            target_dir = str(target_path)
        else:
            target_dir = '.'
    else:
        target_dir = '.'
    
    process_directory(target_dir)
    
    # Pause so user can see the result (for Windows)
    if sys.platform == 'win32':
        input("\nPress Enter to close...")
