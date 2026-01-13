print("what is your name?")

user_name = input()

print(f"hello, {user_name}!")

print("what is your age?")

user_age = input()

def build_profile(name, age):
    return f"Name: {name} | Age: {age}"

def save_to_file(file_name, string):
    with open(file_name, 'w') as file:
        file.write(string)

print(build_profile(user_name, user_age))
print("please confirm saving to file (yes/no):")
confirmation = input().strip().lower()
if confirmation == 'yes':
    save_to_file("data/user_profile.txt", build_profile(user_name, user_age))

def read_from_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

print(read_from_file("data/user_profile.txt"))