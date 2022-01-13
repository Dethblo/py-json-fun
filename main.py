# Python program to read
# json file


import json


# illustrates reading json string (both file and string)
def read_json():
    # JSON string
    a = '{"name": "Bob", "languages": "English"}'

    # deserializes into dict
    # and returns dict.
    y = json.loads(a)

    print("JSON string = ", y)
    print()

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

def write_json():
    # Data to be written
    dictionary = {
        "name": "sathiyajith",
        "rollno": 56,
        "cgpa": 8.6,
        "phonenumber": "9976770500"
    }

    # Explicitly Serializing json into an string object before writing
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    print("\nWriting sample1.json file")
    with open("sample1.json", "w") as outfile:
        outfile.write(json_object)

    # Letting json.dump directly write the dictionary to the file (without the conversion to an object)
    print("\nWriting sample2.json file")
    with open("sample2.json", "w") as outfile:
        json.dump(dictionary, outfile)


# main entry point
if __name__ == '__main__':
    read_json()
    write_json()
