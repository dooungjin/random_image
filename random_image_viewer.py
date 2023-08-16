import os
import random
from PIL import Image
import keyboard

# Path to your folder containing image files
image_folder = "./imgs"

# List all image files in the folder
image_files = [file for file in os.listdir(image_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Shuffle the image files
image_to_skip = set()
no_skip_imgs = len(image_files) - len(image_to_skip)
round_num = 1

while no_skip_imgs > 0:
    random.shuffle(image_files)
    print("Round number:", round_num)
    print("Number of images:", no_skip_imgs)

    img_num = 1
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        
        if image_path in image_to_skip:
            continue
        
        image = Image.open(image_path)
        image.show()
        
        user_input = input(f"Image {img_num}/{no_skip_imgs}. Press 1 to skip, any key to continue: ")
        img_num += 1

        if user_input == "1":
            image_to_skip.add(image_path)

    no_skip_imgs = len(image_files) - len(image_to_skip)
    round_num += 1
