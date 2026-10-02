import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


def main():

    # --------------------------------
    # 1. Creating Sample Dataset
    # --------------------------------

    data = {
        "Name": ["Ravi", "Sita", "Kiran", "Anu", "John"],
        "Age": [20, 21, 19, 22, 20],
        "Marks": [85, 90, 78, 92, 88],
        "City": ["Guntur", "Vijayawada", "Guntur",
                 "Hyderabad", "Vijayawada"]
    }

    df = pd.DataFrame(data)

    print("===== ORIGINAL DATASET =====")
    print(df)

    # --------------------------------
    # 2. Normalization
    # --------------------------------

    scaler = MinMaxScaler()

    df["Marks_Normalized"] = scaler.fit_transform(
        df[["Marks"]]
    )

    print("\n===== NORMALIZED DATA =====")
    print(df[["Marks", "Marks_Normalized"]])

    # --------------------------------
    # 3. Standardization
    # --------------------------------

    standard_scaler = StandardScaler()

    df["Marks_Standardized"] = standard_scaler.fit_transform(
        df[["Marks"]]
    )

    print("\n===== STANDARDIZED DATA =====")
    print(df[["Marks", "Marks_Standardized"]])

    # --------------------------------
    # 4. Log Transformation
    # --------------------------------

    df["Marks_Log"] = np.log1p(df["Marks"])

    print("\n===== LOG TRANSFORMED DATA =====")
    print(df[["Marks", "Marks_Log"]])

    # --------------------------------
    # 5. Label Encoding
    # --------------------------------

    label_encoder = LabelEncoder()

    df["City_Label"] = label_encoder.fit_transform(
        df["City"]
    )

    print("\n===== LABEL ENCODING =====")
    print(df[["City", "City_Label"]])

    # --------------------------------
    # 6. One-Hot Encoding
    # --------------------------------

    one_hot = pd.get_dummies(
        df["City"],
        prefix="City"
    )

    print("\n===== ONE-HOT ENCODING =====")
    print(one_hot)

    # --------------------------------
    # 7. Final Dataset
    # --------------------------------

    final_df = pd.concat(
        [df, one_hot],
        axis=1
    )

    print("\n===== FINAL TRANSFORMED DATASET =====")
    print(final_df)


if __name__ == "__main__":
    main()