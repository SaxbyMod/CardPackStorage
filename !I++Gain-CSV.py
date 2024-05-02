import csv
import os

def add_number_to_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
        
    # Generate the new data with numbers added before the first row
    new_data = [['{:03d}_{}'.format(i, row[0])] + row[1:] for i, row in enumerate(data)]
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_data)

# Example usage:
input_file = 'input.csv'
output_file = 'output.csv'
add_number_to_csv(input_file, output_file)
