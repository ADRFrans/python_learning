class Profile:
    def __init__(self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills 
    
    def summary(self):
        return f"Name: {self.name}\nAge: {self.age}\nSkills: {self.skills}"
    
person_one = Profile("andrew", 30, ["Python", "Something"])
person_two = Profile("Phil", 1, ["Python", "Something"])
person_three = Profile("kyle", 300, ["Python", "Something"])

print(person_one.summary())
print(person_two.summary())
print(person_three.summary())