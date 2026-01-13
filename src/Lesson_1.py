#Lesson 1 : Introduction to Python

#Variables 
first_name = "Andrew"
last_name = "F"
age = 24

#Collections 
skills = ["running", "lifting", "swimming"]
profile = {
    "first_name": first_name,
    "last_name": last_name,
    "age": age,
    "skills": skills
}

#Functions
def greeting(profile):
    if not profile["first_name"] or not profile["last_name"]:
        return "Hello, Guest!"
    return f"Hello, {profile['first_name']} Skill = {profile['skills'][1]} and {profile['skills'][2]} !"
#Main Execution
#When you run a file directly, like python src/Lesson1.py, python sets __name_ to "__main__"
# when the file is imported into another file, __name__ is set to the module's name.
#why it's used 
# - it lets you run code only whne the file is executed directly, not when imported
if __name__ == "__main__":
    print(greeting(profile))