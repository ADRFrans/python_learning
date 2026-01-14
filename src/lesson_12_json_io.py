import json

list_of_dicts = []

first = {
    "Name": "andrew",
    "age": 24,
    "Skills": ["Python", "Something"]
}
second = {
    "Name": "andrew",
    "age": 24,
    "Skills": ["Python", "Something"]
}
third = {
    "Name": "andrew",
    "age": 24,
    "Skills": ["Python", "Something"]
}

list_of_dicts.append(first)
list_of_dicts.append(second)
list_of_dicts.append(third)

def save_to_file(file_name, string):
    with open(file_name, 'w') as file:
        json.dump(string, file,  indent=2)

save_to_file("data/profiles.json", list_of_dicts)

def read_from_file(file_name):
    with open(file_name, 'r') as file:
        content = json.load(file)
    return content
json_content = read_from_file("data/profiles.json")

print(json_content)