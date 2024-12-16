# Automatic MTC Art Formatter

This script automates the process of converting and resizing card art images for the **Magic: The Gathering (MTC)** card game. It includes two main functionalities: converting card art to MTC format and descaling/rescaling art.

## Getting Started

### Prerequisites

- Python 3.x
- PIL (Python Imaging Library)

### Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running:

    ```bash
    pip install pillow
    ```

## Usage

1. **Prepare Your Artwork:**
   - Place the original card art images in the `Input` folder.
   - Ensure the filenames follow the desired format: `[Name](Category)[Description]_Rarity.png`.

2. **Run the Script:**
   - Open a terminal in the script's directory.
   - Execute the following command:

     ```bash
     python RUNME.py
     ```

   - Enter the desired `edition_id` when prompted.

3. **Review Output:**
   - The converted card art will be placed in the `CvrtrOutput` folder.
   - The descaled/rescaled art will be in the `RescalerOutput` folder.

4. **Clean Output Folders (Optional):**
   - To remove the contents of the output folders before each run, simply run the script.

## Notes

- The script automatically pads the file names with zeros based on the number of files, ensuring proper indexing.

## Modifying the Script

- The script provides flexibility for customization. You can modify the filenames, output folders, and other parameters to fit your specific needs.

## Troubleshooting

- If you encounter any issues, ensure that Python is installed correctly and all dependencies are installed.

Feel free to explore and modify the script according to your requirements. Happy card art formatting!
