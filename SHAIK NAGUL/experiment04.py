import pandas as pd
import numpy as np


def main():

    # --------------------------------
    # 1. Creating Sample Dataset
    # --------------------------------

    data = {
        "Name": ["Ravi", "Sita", "Kiran", "Anu", "John",
                 "Ravi", "Rahul", "Priya"],
        "Marks": [85, 90, 78, 92, 88, 85, 250, 86],
        "Age": [20, 21, 19, 22, 20, 20, 21, 20]
    }

    df = pd.DataFrame(data)

    # --------------------------------
    # 2. Display Original Dataset
    # --------------------------------

    print("===== ORIGINAL DATASET =====")
    print(df)

    # --------------------------------
    # 3. Finding Duplicate Entries
    # --------------------------------

    print("\n===== DUPLICATE ENTRIES =====")
    print(df[df.duplicated()])

    # --------------------------------
    # 4. Removing Duplicate Entries
    # --------------------------------

    df_no_duplicates = df.drop_duplicates()

    print("\n===== DATASET AFTER REMOVING DUPLICATES =====")
    print(df_no_duplicates)

    # --------------------------------
    # 5. Detecting Outliers using Z-score
    # --------------------------------

    marks = df_no_duplicates["Marks"]

    mean = marks.mean()
    std = marks.std()

    z_score = (marks - mean) / std

    print("\n===== Z-SCORES =====")
    print(z_score)

    # --------------------------------
    # 6. Identifying Outliers
    # --------------------------------

    outliers = df_no_duplicates[abs(z_score) > 2]

    print("\n===== OUTLIERS =====")
    print(outliers)

    # --------------------------------
    # 7. Removing Outliers
    # --------------------------------

    df_clean = df_no_duplicates[abs(z_score) <= 2]

    print("\n===== DATASET AFTER REMOVING OUTLIERS =====")
    print(df_clean)

    # --------------------------------
    # 8. Comparing Distributions
    # --------------------------------

    print("\n===== DISTRIBUTION BEFORE OUTLIER REMOVAL =====")
    print(df_no_duplicates["Marks"].describe())

    print("\n===== DISTRIBUTION AFTER OUTLIER REMOVAL =====")
    print(df_clean["Marks"].describe())


if __name__ == "__main__":
    main()