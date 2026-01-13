print("enter name:")
name = input()  
# Remove leading/trailing whitespace
clean_name = name.strip()  
title_case_name = clean_name.title()
print("enter age:")
age = input()
if age.isdigit():
    age = int(age)
    if age < 0:
        print("age cannot be negative, setting age to 0")
    else:
        if age < 18:
            print("67")
        elif age < 65:
            print("old folk")
        else:
            print("senior citizen")
        age = age
else:
    print("invalid age input, setting age to 0")
    age = 0
print(f"name: {title_case_name},\n age: {age}")