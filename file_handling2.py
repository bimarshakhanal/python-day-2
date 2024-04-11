'''
Create a function add_to_json that takes a filename and a dictionary as input.The function should read the
JSON data from the file, add the new dictionary to it, and write the updated data back to the same file.
'''

import json

def update_JSON(fname, new_data):
    '''
    Function to update JSON file.
    Args:
        fname: Name of csv file to open
        new_data: Data to update
    '''
    try:
        with open(fname, 'r') as f:
            # Read existing data (assuming it's valid JSON)
            data = json.loads(f.read())
    except FileNotFoundError:
        # Create a new empty list if file doesn't exist
        data = []
    except json.JSONDecodeError:
        # Handle invalid JSON data (optional)
        print(f"Error: Invalid JSON data found in {fname}.")
        return
    
    data.append(new_data)
    # Write updated data back to the file
    with open(fname, 'w') as outfile:
        json.dump(data, outfile, indent=2)


if __name__=='__main__':
    #take user input
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
    update_JSON(fname,new_data)
