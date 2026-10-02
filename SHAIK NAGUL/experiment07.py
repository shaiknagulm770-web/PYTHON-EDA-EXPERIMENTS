import pandas as pd


def main():

    # --------------------------------
    # 1. Creating Sample Dataset
    # --------------------------------

    data = {
        "Name": ["Ravi", "Sita", "Kiran", "Anu", "John", "Priya"],
        "Department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
        "City": ["Guntur", "Vijayawada", "Guntur",
                 "Vijayawada", "Hyderabad", "Hyderabad"],
        "Marks": [85, 90, 78, 92, 88, 86],
        "Age": [20, 21, 19, 22, 20, 21]
    }

    df = pd.DataFrame(data)

    print("===== ORIGINAL DATASET =====")
    print(df)

    # --------------------------------
    # 2. Grouping Data using groupby
    # --------------------------------

    print("\n===== GROUP BY DEPARTMENT =====")

    grouped = df.groupby("Department")

    print(grouped["Marks"].mean())

    # --------------------------------
    # 3. Aggregate Statistics
    # --------------------------------

    print("\n===== AGGREGATE STATISTICS =====")

    aggregate = df.groupby("Department")["Marks"].agg(
        ["mean", "sum", "min", "max", "count"]
    )

    print(aggregate)

    # --------------------------------
    # 4. Multiple Column Aggregation
    # --------------------------------

    print("\n===== MULTIPLE COLUMN AGGREGATION =====")

    multiple_aggregate = df.groupby("Department").agg(
        {
            "Marks": ["mean", "max", "min"],
            "Age": ["mean", "max", "min"]
        }
    )

    print(multiple_aggregate)

    # --------------------------------
    # 5. Creating Pivot Table
    # --------------------------------

    print("\n===== PIVOT TABLE =====")

    pivot = pd.pivot_table(
        df,
        values="Marks",
        index="Department",
        columns="City",
        aggfunc="mean"
    )

    print(pivot)

    # --------------------------------
    # 6. Pivot Table with Multiple
    #    Aggregate Functions
    # --------------------------------

    print("\n===== PIVOT TABLE WITH AGGREGATION =====")

    pivot_summary = pd.pivot_table(
        df,
        values="Marks",
        index="Department",
        columns="City",
        aggfunc=["mean", "max"]
    )

    print(pivot_summary)


if __name__ == "__main__":
    main()