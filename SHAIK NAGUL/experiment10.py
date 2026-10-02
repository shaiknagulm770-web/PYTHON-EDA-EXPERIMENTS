import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    # --------------------------------
    # 1. Creating Sample Dataset
    # --------------------------------

    data = {
        "Age": [18, 19, 20, 21, 22, 23, 24, 25],
        "Study_Hours": [2, 3, 4, 5, 5, 6, 7, 8],
        "Marks": [55, 60, 65, 70, 72, 78, 85, 90],
        "Attendance": [70, 72, 75, 78, 80, 85, 88, 92]
    }

    df = pd.DataFrame(data)

    print("===== DATASET =====")
    print(df)

    # --------------------------------
    # 2. Scatter Plot
    # --------------------------------

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df["Study_Hours"],
        df["Marks"]
    )

    plt.title("Study Hours vs Marks")
    plt.xlabel("Study Hours")
    plt.ylabel("Marks")
    plt.grid(True, alpha=0.3)

    plt.show()

    # --------------------------------
    # 3. Correlation Matrix
    # --------------------------------

    correlation = df.corr()

    print("\n===== CORRELATION MATRIX =====")
    print(correlation)

    plt.figure(figsize=(8, 6))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Matrix")

    plt.show()

    # --------------------------------
    # 4. Pair Plot
    # --------------------------------

    sns.pairplot(df)

    plt.suptitle(
        "Pair Plot of Student Data",
        y=1.02
    )

    plt.show()


if __name__ == "__main__":
    main()