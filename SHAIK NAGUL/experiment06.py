import pandas as pd


def main():

    # --------------------------------
    # 1. Creating Sample Dataset
    # --------------------------------

    data = {
        "Name": ["Ravi", "Sita", "Kiran", "Anu", "John"],
        "Age": [20, 21, 19, 22, 20],
        "Marks": [85, 90, 78, 92, 88],
        "City": ["Guntur", "Vijayawada", "Hyderabad",
                 "Hyderabad", "Chennai"]
    }

    df = pd.DataFrame(data)

    print("===== ORIGINAL DATASET =====")
    print(df)

    # --------------------------------
    # 2. Selecting a Column
    # --------------------------------

    print("\n===== SELECTING A COLUMN =====")
    print(df["Name"])

    # --------------------------------
    # 3. Selecting Multiple Columns
    # --------------------------------

    print("\n===== SELECTING MULTIPLE COLUMNS =====")
    print(df[["Name", "Marks"]])

    # --------------------------------
    # 4. Indexing using loc
    # --------------------------------

    print("\n===== INDEXING USING loc =====")
    print(df.loc[0])
    print(df.loc[1:3, ["Name", "Marks"]])

    # --------------------------------
    # 5. Indexing using iloc
    # --------------------------------

    print("\n===== INDEXING USING iloc =====")
    print(df.iloc[0])
    print(df.iloc[1:4, 0:3])

    # --------------------------------
    # 6. Boolean Filtering
    # --------------------------------

    print("\n===== STUDENTS WITH MARKS > 85 =====")
    print(df[df["Marks"] > 85])

    # --------------------------------
    # 7. Conditional Selection
    # --------------------------------

    print("\n===== STUDENTS WITH AGE >= 20 AND MARKS > 85 =====")

    condition = (df["Age"] >= 20) & (df["Marks"] > 85)

    print(df[condition])

    # --------------------------------
    # 8. Filtering using OR condition
    # --------------------------------

    print("\n===== STUDENTS FROM HYDERABAD OR CHENNAI =====")

    condition = (df["City"] == "Hyderabad") | (df["City"] == "Chennai")

    print(df[condition])

    # --------------------------------
    # 9. Slicing Rows
    # --------------------------------

    print("\n===== ROW SLICING =====")
    print(df[1:4])

    # --------------------------------
    # 10. Advanced Slicing
    # --------------------------------

    print("\n===== ADVANCED SLICING =====")
    print(df.loc[1:4, "Name":"Marks"])


if __name__ == "__main__":
    main()