import random
import math

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
heights = [5.5, 6.0, 5.8]
skills = ["Python", "Java", "C++"]

people = []


def random_creation(name, age, height, skill):
    return {
        "name": name[random.choice(range(len(name)))],
        "age": age[random.choice(range(len(age)))],
        "height": height[random.choice(range(len(height)))],
        # Pick exactly 2 unique skills for this person.
        "skill": random.sample(skill, k=min(2, len(skill)))
    } 
i = 0

while i < 3: 
    person = random_creation(names, ages, heights, skills)
    people.append(person)
    i += 1

def avg_age(people):
    total_age = 0
    for person in people:
        total_age += person["age"]
    return total_age / len(people)
#go into each object of people 

def total_skills(people):
    total = 0 
    for person in people:
        total += len(person["skill"])
    return total
def oldest_person(people):
    oldest_person = people[0]
    for person in people:
        if person["age"] > oldest_person["age"]:
            oldest_person = person
    return oldest_person

print(avg_age(people))
print(total_skills(people))
for person in people:
    print(person)
print(f"Oldest person: {oldest_person(people)}")
