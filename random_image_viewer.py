import os
import random
from PIL import Image

# Path to your folder containing image files
image_folder = "./imgs"

# List all image files in the folder
image_files = [file for file in os.listdir(image_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Shuffle the image files
random.shuffle(image_files)

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    image = Image.open(image_path)
    image.show()
    input("Press Enter to close the image and view the next image...")

print("No more images to display.")
