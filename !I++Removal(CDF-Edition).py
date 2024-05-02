import os

def remove_incrementation():
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Get a list of all files in the same folder as the script
    all_files = os.listdir(script_dir)

    # Filter only PNG files
    png_files = [file for file in all_files if file.lower().endswith('.cdf')]

    print("Files to be processed:")
    for file_name in png_files:
        print(file_name)

    # Create a dictionary to store the original and new filenames
    file_mapping = {}

    # Generate the new filenames and store the mapping
    for file_name in png_files:
        # Find the first hyphen in the filename
        first_hyphen_index = file_name.find('_')

        # Check if there is a hyphen
        if first_hyphen_index >= 0:
            # Extract the part after the first hyphen
            rest_of_filename = file_name[first_hyphen_index + 1:]

            # Generate the new filename without the incrementation
            new_filename = rest_of_filename

            # Create the full paths for the old and new files
            old_file_path = os.path.join(script_dir, file_name)
            new_file_path = os.path.join(script_dir, new_filename)

            # Check if the new file exists
            count = 1
            while os.path.exists(new_file_path):
                # If the new file exists, add an underscore and retry
                new_filename = f"{count}-{rest_of_filename}"
                new_file_path = os.path.join(script_dir, new_filename)
                count += 1

            # Store the mapping
            file_mapping[old_file_path] = new_file_path

    # Save a log file with files that are not processed
    log_file_path = os.path.join(script_dir, "!LOG.txt")
    with open(log_file_path, 'w') as log_file:
        not_processed_files = set(png_files) - set(file_mapping.keys())
        log_file.write("Files not processed:\n")
        for not_processed_file in not_processed_files:
            log_file.write(f"{not_processed_file}\n")

    # Rename the files
    for old_path, new_path in file_mapping.items():
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} to {new_path}")

        # Replace later dashes with underscores
        new_path_with_underscore = new_path.replace('-', '_').replace(' ', '_').lower()
        os.rename(new_path, new_path_with_underscore)
        print(f"Replaced dashes with underscores: {new_path} to {new_path_with_underscore}")

# Run the function to remove the incrementation from PNG filenames
remove_incrementation()
