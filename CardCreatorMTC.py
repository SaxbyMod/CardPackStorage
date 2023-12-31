import os
import re

def get_rarity_from_filename(filename):
    suffix_match = re.search(r'_(com|common|unc|uncommon|rare|anc|ancient|leg|legendary)\.png$', filename, flags=re.IGNORECASE)
    if suffix_match:
        return suffix_match.group(1).lower()
    else:
        return 'common'

def get_drop_weight(rarity):
    drop_weights = {'com': 10, 'unc': 5, 'rare': 3, 'anc': 2, 'leg': 1}
    return drop_weights.get(rarity, 10)  # Default to 10 for common if the rarity is not in the dictionary

def extract_category_and_description(filename):
    # Extract category from text inside parentheses
    category_match = re.search(r'\((.*?)\)', filename)
    category = category_match.group(1) if category_match else None

    # Extract description from text inside square brackets
    description_match = re.search(r'\[(.*?)\]', filename)
    description = description_match.group(1) if description_match else None

    return category, description

def generate_cdf_file(card_image_path):
    filename_no_extension = os.path.splitext(os.path.basename(card_image_path))[0]
    card_id = filename_no_extension.replace(" ", "_").lower()
    card_id = re.sub(r'\W+', '_', card_id)
    
    # Remove rarity suffix from card_id
    card_id = re.sub(r'_(com|common|unc|uncommon|rare|anc|ancient|leg|legendary)$', '', card_id)

    # Remove rarity suffix from image_name, replace underscores with spaces, and capitalize each word
    image_name = filename_no_extension.split("_", 1)[1]
    image_name = re.sub(r'_(com|common|unc|uncommon|rare|anc|ancient|leg|legendary)$', '', image_name)
    image_name = image_name.replace('_', ' ').title()

    illustration_path = f'[DIRPATHINSERT]/{filename_no_extension}'

    rarity = get_rarity_from_filename(os.path.basename(card_image_path))
    drop_weight = get_drop_weight(rarity)

    # Extract category and description from the filename
    category, description = extract_category_and_description(filename_no_extension)

    if not category:
        category = "Uncategorized"

    cdf_data = f'''
EditionID=[INSERTID]
CardID={card_id}
RarityLevel={rarity}

Name={image_name}
Category={category}
DropWeight={drop_weight}

IllustrationPath={illustration_path}
'''

    if description:
        cdf_data += f'Description={description}\n'

    cdf_name = re.sub(r'\W+', '_', filename_no_extension)
    cdf_name = f'{cdf_name}.cdf'

    with open(cdf_name, 'w') as file:
        file.write(cdf_data)

# Fetching images from 2 folders up > Assets > Inscryption_Finale_Cards
cards_folder = os.path.abspath(os.path.join(os.getcwd(), "../../Assets/[DIRPATHINSERT]"))
for filename in os.listdir(cards_folder):
    if filename.endswith(".png"):
        card_image_path = os.path.join(cards_folder, filename)
        generate_cdf_file(card_image_path)
