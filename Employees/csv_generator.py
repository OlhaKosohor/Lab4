from datetime import datetime, timedelta
from faker import Faker
import random
import csv

fake = Faker(locale="uk")


def birthday(from_year: int, to_year: int):
    start_date = datetime(from_year, 1, 1)
    end_date = datetime(to_year, 12, 31)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


def generator(gender: str):

    return [
        fake.last_name(),
        fake.first_name_male() if gender == "Чоловік" else fake.first_name_female(),
        fake.middle_name_male() if gender == "Чоловік" else fake.middle_name_female(),
        gender,
        birthday(1938, 2008).strftime("%d-%m-%Y"),
        fake.job(),
        fake.city(),
        fake.address().replace("\n", ", "),
        fake.phone_number(),
        fake.email(),
    ]


def write_csv(filename: str, num_records: int = 2000):
    male_count = int(num_records * 0.6)
    female_count = num_records - male_count

    with open(filename, "w", newline="", encoding="utf8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                "Last Name",
                "First Name",
                "Middle Name",
                "Gender",
                "Birthdate",
                "Position",
                "City",
                "Address",
                "Phone",
                "Email",
            ]
        )

        for _ in range(male_count):
            writer.writerow(generator("Чоловік"))

        for _ in range(female_count):
            writer.writerow(generator("Жінка"))
