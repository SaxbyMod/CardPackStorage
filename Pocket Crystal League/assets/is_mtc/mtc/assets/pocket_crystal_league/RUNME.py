import os
from PIL import Image
import logging
import shutil

def main():
    # Set the edition_id
    edition_id = input("Enter the edition_id: ")

    # Path for card art conversion
    card_art_input_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "Input"))
    card_art_cvrtr_output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "CvrtrOutput"))
    card_art_rescaler_output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "RescalerOutput"))

    # Create input and output folders if they don't exist
    os.makedirs(card_art_input_dir, exist_ok=True)
    os.makedirs(card_art_cvrtr_output_dir, exist_ok=True)
    os.makedirs(card_art_rescaler_output_dir, exist_ok=True)

    print(f"Converting card art to MTC format from: {card_art_input_dir}")
    print(f"Outputting converted card art to: {card_art_cvrtr_output_dir}")

    # Clean out the CvrtrOutput folder
    clean_folder(card_art_cvrtr_output_dir)

    # Convert card art to MTC format
    convert_card_art(card_art_input_dir, card_art_cvrtr_output_dir)

    # Inform the user that card art has been converted
    print("Card art converted to MTC format successfully.")

    # Path for art descaling/rescaling
    assets_rescaler_input_dir = card_art_cvrtr_output_dir

    print(f"Descaling/Rescaling art in: {card_art_rescaler_output_dir}")

    # Clean out the RescalerOutput folder
    clean_folder(card_art_rescaler_output_dir)

    # Descale/Rescale art
    resize_images(assets_rescaler_input_dir, card_art_rescaler_output_dir)

    # Inform the user that art has been descaled/rescaled
    print("Art descaled/rescaled successfully.")

def clean_folder(folder_path):
    # Clean out the contents of the specified folder
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error cleaning folder: {e}")

def convert_card_art(input_dir, output_dir):
    # Get the total number of files in the input directory
    total_files = len([f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))])

    # Calculate the zero-padding length based on the total number of files
    zero_padding_length = len(str(total_files))

    # Iterate over the original images
    for i, filename in enumerate(sorted(os.listdir(input_dir))):
        print(filename)
        # Path to the original image
        old_image_path = os.path.join(input_dir, filename)

        # Open the original image and convert it to RGBA mode
        img = Image.open(old_image_path).convert("RGBA")

        # Get the dimensions of the original image
        width, height = img.size

        # Determine the larger dimension
        max_dim = max(width, height)

        # Calculate the paste coordinates to center the old image in the new image
        paste_x = (max_dim - width) // 2
        paste_y = (max_dim - height) // 2

        # Create a new image with the larger dimension
        new_img = Image.new("RGBA", (max_dim, max_dim), (0, 0, 0, 0))

        # Paste the old image onto the new image
        new_img.paste(img, (paste_x, paste_y))

        # Generate the new filename with dynamic zero-padding
        new_filename = f"{str(i).zfill(zero_padding_length)}_{filename}"
        print(filename + " Completed")
        # Save the new image
        new_image_path = os.path.join(output_dir, new_filename)
        new_img.save(new_image_path)

        # Close the images
        img.close()
        new_img.close()

def resize_images(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            logging.info(f"Importing image: {input_path}")

            with Image.open(input_path) as image:
                # Check if the image size is smaller than the target size
                if image.size[0] < 448 or image.size[1] < 448:
                    logging.info(f"Resizing image using nearest neighbor: {input_path}")
                    resized_image = image.resize((448, 448), Image.NEAREST)
                else:
                    resized_image = image.resize((448, 448), Image.LANCZOS)

                resized_image.save(output_path, quality=95)

            logging.info(f"Image exported: {output_path}")

if __name__ == "__main__":
    main()
