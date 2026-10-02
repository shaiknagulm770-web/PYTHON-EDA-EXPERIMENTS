import pandas as pd


def main():

    # --------------------------------
    # 1. Creating Sample Dataset
    # --------------------------------

    data = {
        "Student": ["Ravi", "Sita", "Kiran", "Anu", "John"],
        "Marks": [85, 90, 78, 92, 88],
        "Age": [20, 21, 19, 22, 20]
    }

    df = pd.DataFrame(data)

    # --------------------------------
    # 2. Saving Dataset into
    # CSV, Excel, and JSON files
    # --------------------------------

    df.to_csv("students.csv", index=False)
    df.to_excel("students.xlsx", index=False)
    df.to_json("students.json", orient="records")

    # --------------------------------
    # 3. Importing Data
    # --------------------------------

    csv_data = pd.read_csv("students.csv")
    excel_data = pd.read_excel("students.xlsx")
    json_data = pd.read_json("students.json")

    # --------------------------------
    # 4. Basic Exploration
    # --------------------------------

    print("===== CSV DATA =====")
    print(csv_data)

    print("\n===== HEAD() =====")
    print(csv_data.head())

    print("\n===== INFO() =====")
    print(csv_data.info())

    print("\n===== DESCRIBE() =====")
    print(csv_data.describe())

    print("\n===== SHAPE =====")
    print(csv_data.shape)


if __name__ == "__main__":
    main()