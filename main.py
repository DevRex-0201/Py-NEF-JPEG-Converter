import os
from tkinter import Tk, filedialog
from PIL import Image

def select_folder():
    root = Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select the source folder
    source_folder = filedialog.askdirectory(title="Select Source Folder")
    root.destroy()

    return source_folder

def convert_nef_to_jpeg(source_folder, dest_folder, quality=95, dpi=(300, 300)):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Get a list of all .NEF files in the source folder
    nef_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.nef')]

    # Iterate through each .NEF file and convert to .JPEG
    for nef_file in nef_files:
        nef_path = os.path.join(source_folder, nef_file)
        jpeg_path = os.path.join(dest_folder, os.path.splitext(nef_file)[0] + '.jpg')

        try:
            # Open the NEF file
            with Image.open(nef_path) as img:
                # Get the original image size
                original_size = img.size

                # Save the image as JPEG with specified quality and DPI without resizing
                img.convert("RGB").save(jpeg_path, "JPEG", quality=quality, dpi=dpi)
                
                # Resize the saved image to the original size
                with Image.open(jpeg_path) as saved_img:
                    saved_img = saved_img.resize(original_size, Image.BILINEAR)
                    saved_img.save(jpeg_path)

                print(f"Conversion successful. Saved as {jpeg_path}")
        except Exception as e:
            print(f"Error converting {nef_file}: {e}")

if __name__ == "__main__":
    # Use the select_folder function to get the source folder interactively
    source_folder = select_folder()

    if source_folder:
        # Define the destination folder
        dest_folder = "path/to/destination/folder"

        # Call the conversion function with specified quality and DPI
        convert_nef_to_jpeg(source_folder, dest_folder, quality=95, dpi=(300, 300))
