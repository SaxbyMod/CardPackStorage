import os

def get_filenames_without_extension(directory):
    filenames = set()
    for filename in os.listdir(directory):
        name, _ = os.path.splitext(filename)
        filenames.add(name)
    return filenames

def compare_folders(folder1, folder2):
    folder1_filenames = get_filenames_without_extension(folder1)
    folder2_filenames = get_filenames_without_extension(folder2)
    
    unique_to_folder1 = folder1_filenames - folder2_filenames
    unique_to_folder2 = folder2_filenames - folder1_filenames
    
    return unique_to_folder1, unique_to_folder2

# Replace 'folder1_path' and 'folder2_path' with the paths to the folders you want to compare
folder1_path = 'C://Users//Thinc//Downloads//New-folder'
folder2_path = 'C://Users//Thinc//Downloads//New-folder-2'

unique_to_folder1, unique_to_folder2 = compare_folders(folder1_path, folder2_path)

print("Files unique to folder 1:")
for filename in unique_to_folder1:
    print(filename)

print("\nFiles unique to folder 2:")
for filename in unique_to_folder2:
    print(filename)

unimportant = input("")