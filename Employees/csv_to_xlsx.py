import pandas as pd
from datetime import datetime


def load_csv(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        print(f"Помилка при відкритті файлу CSV: {e}")
        return None


def calculate_age(birthdate):
    birthdate = datetime.strptime(birthdate, "%d-%m-%Y")
    today = datetime.today()
    return (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )


def categorize_age(age):
    if age < 18:
        return "younger_18"
    elif 18 <= age <= 45:
        return "18-45"
    elif 45 < age <= 70:
        return "45-70"
    else:
        return "older_70"


def create_xlsx(df, output_file: str):
    try:
        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="all", index=False)

            for age_group in ["younger_18", "18-45", "45-70", "older_70"]:
                df_age_group = df[
                    df.apply(
                        lambda row: categorize_age(calculate_age(row["Birthdate"]))
                        == age_group,
                        axis=1,
                    )
                ]
                df_age_group["Age"] = df_age_group["Birthdate"].apply(
                    lambda dob: calculate_age(dob)
                )
                df_age_group = df_age_group[
                    ["Last Name", "First Name", "Middle Name", "Birthdate", "Age"]
                ]
                df_age_group.index += 1
                df_age_group.to_excel(writer, sheet_name=age_group, index_label="№")

        print("Ok")
    except Exception as e:
        print(f"Помилка при створенні XLSX файлу: {e}")
