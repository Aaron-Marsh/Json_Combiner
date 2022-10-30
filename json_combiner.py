import sys
import os
import json
from collections import Counter
from pathlib import Path

# Set path to directory which contains the JSON files to combine
try:
    directory = Path(sys.argv[1])

except IndexError: 
    exit('Error: No path provided. Provide a path to directory containing JSON files to combine.')
except:
    exit('Error: Could not set path to directory.')

combinedfile_data_boards = []
combinedfile_data = {}

# Combine boards from each file into one list
try:
    for filename in os.listdir(directory):
        with open(directory / filename, 'r') as jsonfile:
            filedata = json.load(jsonfile)
            combinedfile_data_boards += filedata["boards"]

except FileNotFoundError:
    exit('Error: No directory found at this location - Check path.')
except IsADirectoryError:
    exit(f'Error: {os.path.basename(directory)} contains {filename} which is a directory, not a JSON file.')
except KeyError:
    exit(f'Error: Key error occured in {os.path.basename(directory)}/{filename}. Check formatting of object as "boards" key not found.')
except json.JSONDecodeError:
    exit(f"Error: Could not read {os.path.basename(directory)}/{filename} as a JSON formatted file.")

# Sort boards alphabetically by vendor and name, and add to combinedfile_data dictionary
try:
    combinedfile_data['boards'] = sorted(combinedfile_data_boards, key=lambda k: (k['vendor'], k['name']))

# If cannot sort by vendor and name, search for where key error occurs to report
except KeyError:
    for filename in os.listdir(directory):
        with open(directory / filename, 'r') as jsonfile:
            filedata = json.load(jsonfile)
        for board in filedata["boards"]:
            if "name" or "vendor" not in board.keys():
                exit(f"Error: Key error from incorrectly formatted object in {os.path.basename(directory)}/{filename}:\n{board}")

# Evaluate metadata and add to dictionary
vendors_list = [board['vendor'] for board in combinedfile_data_boards]
num_vendors = len(Counter(vendors_list).keys())
num_boards = len(combinedfile_data_boards)

metadata = {
    "total_vendors": num_vendors,
    "total_boards": num_boards
}
combinedfile_data['_metadata'] = metadata

# Create JSON file for combined data in the parent directory of the directory which contains multiple JSON files
combinedfile_name = f"{os.path.basename(directory)}_combined.json"
parent_directory = Path(os.path.dirname(directory))
combinedfile = parent_directory / combinedfile_name
combinedfile.touch()

# Write combined file data to the new JSON file
with open (combinedfile, 'r+') as file:
    json.dump(combinedfile_data, file, indent = 4)

print(f'Json files have been combined into new file at location:\n{combinedfile.absolute()}')

