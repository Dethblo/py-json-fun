# Python program to read
# json file


import json

# reads a json file and prints the contents
def read_json():
    # Opening JSON file
    f = open('data.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data['emp_details']:
        print(i)

    # Closing file
    f.close()


# main entry point
if __name__ == '__main__':
    read_json()

