class Profile:
    def __init__(self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills 
    
    def summary(self):
        return f"Name: {self.name}\nAge: {self.age}\nSkills: {self.skills}"
    
    def has_skills(self, skill):
        return skill in self.skills

person_one = Profile("andrew", 30, ["Python", "Something"])
person_two = Profile("Phil", 1, ["Pasthon", "Something"])
person_three = Profile("e", 300, ["Python", "Something"])
person_four = Profile("anew", 30, ["Pythoasdn", "Something"])
person_five = Profile("Pil", 1, ["Python", "Something"])
person_six = Profile("kae", 300, ["Pythqqqon", "Something"])

person_list = []

person_list.append(person_one)
person_list.append(person_two)
person_list.append(person_three)
person_list.append(person_four)
person_list.append(person_five)
person_list.append(person_six)

for person in person_list:
    if person.has_skills("Python") == True:
        print(person.name)
    
