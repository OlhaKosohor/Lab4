import pandas as pd
import matplotlib.pyplot as plt
from .csv_to_xlsx import categorize_age, calculate_age


def plot_pie_chart(data, labels, title):
    plt.figure(figsize=(8, 6))
    plt.pie(data, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title(title)
    plt.show()


def analyze_data(df):
    df["Gender"].value_counts().plot(
        kind="bar", title="Кількість співробітників за статтю"
    )
    plt.show()

    df["Age"] = df["Birthdate"].apply(lambda dob: calculate_age(dob))
    df["Age Category"] = df["Age"].apply(categorize_age)

    age_categories = df["Age Category"].value_counts()
    plot_pie_chart(
        age_categories,
        age_categories.index,
        "Кількість співробітників за віковими категоріями",
    )

    gender_age_category = df.groupby(["Gender", "Age Category"]).size().unstack()
    gender_age_category.plot(
        kind="bar", stacked=True, title="Кількість співробітників за віком та статтю"
    )
    plt.show()
