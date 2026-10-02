import pandas as pd


def main():

    # --------------------------------
    # 1. Creating First Dataset
    # --------------------------------

    students = pd.DataFrame({
        "Student_ID": [1, 2, 3, 4],
        "Name": ["Ravi", "Sita", "Kiran", "Anu"],
        "Marks": [85, 90, 78, 92]
    })

    # --------------------------------
    # 2. Creating Second Dataset
    # --------------------------------

    details = pd.DataFrame({
        "Student_ID": [1, 2, 3, 5],
        "City": ["Guntur", "Vijayawada", "Hyderabad", "Chennai"],
        "Age": [20, 21, 19, 22]
    })

    print("===== STUDENTS DATA =====")
    print(students)

    print("\n===== DETAILS DATA =====")
    print(details)

    # --------------------------------
    # 3. Inner Merge
    # --------------------------------

    print("\n===== INNER MERGE =====")

    inner_merge = pd.merge(
        students,
        details,
        on="Student_ID",
        how="inner"
    )

    print(inner_merge)

    # --------------------------------
    # 4. Left Merge
    # --------------------------------

    print("\n===== LEFT MERGE =====")

    left_merge = pd.merge(
        students,
        details,
        on="Student_ID",
        how="left"
    )

    print(left_merge)

    # --------------------------------
    # 5. Outer Merge
    # --------------------------------

    print("\n===== OUTER MERGE =====")

    outer_merge = pd.merge(
        students,
        details,
        on="Student_ID",
        how="outer"
    )

    print(outer_merge)

    # --------------------------------
    # 6. Handling Missing Values
    # --------------------------------

    print("\n===== HANDLING MISSING VALUES =====")

    outer_merge["Age"] = outer_merge["Age"].fillna(0)
    outer_merge["City"] = outer_merge["City"].fillna("Unknown")

    print(outer_merge)

    # --------------------------------
    # 7. Concatenating Rows
    # --------------------------------

    print("\n===== CONCATENATING ROWS =====")

    extra_students = pd.DataFrame({
        "Student_ID": [6, 7],
        "Name": ["Rahul", "Priya"],
        "Marks": [82, 89]
    })

    concatenated_rows = pd.concat(
        [students, extra_students],
        ignore_index=True
    )

    print(concatenated_rows)

    # --------------------------------
    # 8. Concatenating Columns
    # --------------------------------

    print("\n===== CONCATENATING COLUMNS =====")

    contact = pd.DataFrame({
        "Phone": ["9876543210", "9876543211",
                  "9876543212", "9876543213"]
    })

    concatenated_columns = pd.concat(
        [students, contact],
        axis=1
    )

    print(concatenated_columns)

    # --------------------------------
    # 9. Joining DataFrames
    # --------------------------------

    print("\n===== JOINING DATAFRAMES =====")

    students_indexed = students.set_index("Student_ID")
    details_indexed = details.set_index("Student_ID")

    joined = students_indexed.join(
        details_indexed,
        how="left",
        lsuffix="_student",
        rsuffix="_details"
    )

    print(joined)


if __name__ == "__main__":
    main()