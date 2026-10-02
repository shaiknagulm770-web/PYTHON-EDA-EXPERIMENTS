import pandas as pd
import numpy as np


def main():

    # --------------------------------
    # 1. Creating Sample Dataset
    # --------------------------------

    data = {
        "Age": [20, 21, np.nan, 22, 20],
        "Marks": [85, np.nan, 78, np.nan, 88],
        "City": ["Guntur", None, "Hyderabad", None, "Chennai"]
    }

    df = pd.DataFrame(data)

    # --------------------------------
    # 2. Display Original Dataset
    # --------------------------------

    print("===== ORIGINAL DATASET =====")
    print(df)

    # --------------------------------
    # 3. Mean Imputation
    # --------------------------------

    mean_fill = df.copy()

    mean_fill["Age"] = mean_fill["Age"].fillna(
        mean_fill["Age"].mean()
    )

    mean_fill["Marks"] = mean_fill["Marks"].fillna(
        mean_fill["Marks"].mean()
    )

    print("\n===== MEAN IMPUTATION =====")
    print(mean_fill)

    # --------------------------------
    # 4. Median Imputation
    # --------------------------------

    median_fill = df.copy()

    median_fill["Age"] = median_fill["Age"].fillna(
        median_fill["Age"].median()
    )

    median_fill["Marks"] = median_fill["Marks"].fillna(
        median_fill["Marks"].median()
    )

    print("\n===== MEDIAN IMPUTATION =====")
    print(median_fill)

    # --------------------------------
    # 5. Mode Imputation
    # --------------------------------

    mode_fill = df.copy()

    mode_fill["City"] = mode_fill["City"].fillna(
        mode_fill["City"].mode()[0]
    )

    print("\n===== MODE IMPUTATION =====")
    print(mode_fill)

    # --------------------------------
    # 6. Forward Fill
    # --------------------------------

    forward_fill = df.ffill()

    print("\n===== FORWARD FILL =====")
    print(forward_fill)

    # --------------------------------
    # 7. Backward Fill
    # --------------------------------

    backward_fill = df.bfill()

    print("\n===== BACKWARD FILL =====")
    print(backward_fill)

    # --------------------------------
    # 8. Drop Rows with Missing Values
    # --------------------------------

    drop_rows = df.dropna()

    print("\n===== DROP ROWS =====")
    print(drop_rows)

    # --------------------------------
    # 9. Drop Columns with Missing Values
    # --------------------------------

    drop_columns = df.dropna(axis=1)

    print("\n===== DROP COLUMNS =====")
    print(drop_columns)


if __name__ == "__main__":
    main()