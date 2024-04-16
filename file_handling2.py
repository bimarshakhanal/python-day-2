'''
Create a function add_to_json that takes a filename and a dictionary as input.The function should 
read the JSON data from the file, add the new dictionary to it, and write the updated data back to
the same file.
'''

import json
import logging

logging.basicConfig(filename='example.log',
                    encoding='utf-8', level=logging.DEBUG)


def update_json(filename, data):
    '''
    Function to update JSON file.
    Args:
        filename: Name of csv file to open
        data: Data to update
    '''
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Read existing data (assuming it's valid JSON)
            data = json.loads(f.read())
    except FileNotFoundError:
        # Create a new empty list if file doesn't exist
        logging.warning('File not found, creating a new file.')
        data = []
    except json.JSONDecodeError:
        # Handle invalid JSON data (optional)
        logging.error(f"Invalid JSON data found in {filename}.")
        return

    try:
        data.append(data)
    except ValueError:
        logging.error('Tried to add invalid data.')
    # Write updated data back to the file
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=2)


if __name__ == '__main__':
    # take user input
    fname = input("Enter file name: ")
    new_data = [
        {
            "name": "David",
            "age": 32
        },
        {
            "name": "John",
            "age": 25
        }
    ]
    update_json(fname, new_data)
