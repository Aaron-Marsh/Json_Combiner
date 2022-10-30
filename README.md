# Json_Combiner

## About
This repository contains a CLI that can be used to combine development boards from multiple JSON files into a single JSON file. It requires an input parameter, which is the path to a directory containing the multiple JSON files. It has been built using Python.

## Installation and Usage
### Installation
Clone this repository or otherwise download the json_combiner.py file. You will need a python3 interpreter to execute this script in your CLI.

### Usage
Execute the json_combiner.py file with a python interpreter, using a path to a directory containing boards to combine as a parameter. For example, in MacOS with CWD containing json_combiner.py and example-boards directory, use following command:

`python json_combiner.py "example-boards"`

"example-boards" can be substituted for the path to another directory containing relevant JSON files. If the format of the directory and JSON files is correct (matches that of example-boards), then a new JSON file will be created in the parent directory of the input directory and will contain the combined JSON data. The combined file will have the name of the input directory with a "_combined" suffix e.g. "example-boards_combined". The combined data will be sorted by vendor and name, and include relevant _metadata.

## Assumptions
It has been assumed that users can execute python scripts, and that the input directory will be roughly as expected. Some error handling has been included to deal with incorrect paths and to highlight errors in the input data. However, it may still be possible for the input data to be different enough to expected that there may not be script specific error handling for those cases. It has also been assumed that the desired response to incorrectly formatted boards is to highlight the board for editing rather than ignore it and combine the rest of the data.
