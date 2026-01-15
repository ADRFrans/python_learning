import requests

url = "https://api.agify.io/"

def get_age(name):

    data = None
    params = {"name": name}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error: goodluck")
        data = None
    return data

print("who are you looking for?")
name = input()

person = get_age(name)

if person is None:
    print("no person found")
else:
    print(person["age"])