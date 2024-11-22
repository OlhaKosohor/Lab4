from Employees.csv_generator import write_csv
from Employees.csv_to_xlsx import create_xlsx, load_csv
from Employees.graph import analyze_data

if __name__ == "__main__":
    CSV_FILE = "employees.csv"
    XLSX_FILE = "employees.xlsx"

    write_csv(CSV_FILE)
    df = load_csv(CSV_FILE)
    if df is not None:
        create_xlsx(df, XLSX_FILE)
        analyze_data(df)
