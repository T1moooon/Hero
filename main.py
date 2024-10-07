import os
from faker import Faker
import file_operations
import random
import ast



def main():
    fake = Faker("ru_RU")
    skills = [
        "Стремительный прыжок",
        "Электрический выстрел",
        "Ледяной удар",
        "Стремительный удар",
        "Кислотный взгляд",
        "Тайный побег",
        "Ледяной выстрел",
        "Огненный заряд"
    ]
    with open('letter-mapping.txt') as file:
        text_style = ast.literal_eval(file.read())
    output_dir = "cards"
    os.makedirs(output_dir, exist_ok=True)
    for i in range(10):
        runic_skills = []
        for skill in skills:
            new_word = ""
            for letter in skill:
                new_word += text_style.get(letter, letter)
            runic_skills.append(new_word)
        random_skills = random.sample(runic_skills, 3)

        context = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": random_skills[0],
            "skill_2": random_skills[1],
            "skill_3": random_skills[2]
        }
        output_filename = os.path.join(output_dir, "result_{}.svg".format(i + 1))
        file_operations.render_template('charsheet.svg', output_filename, context)


if __name__ == "__main__":
    main()