import pandas as pd
import matplotlib.pyplot as plt


def main():

    # --------------------------------
    # 1. Creating Sample Dataset
    # --------------------------------

    data = {
        "Marks": [65, 70, 72, 75, 78, 80, 82, 85,
                  85, 88, 90, 92, 95, 96, 98]
    }

    df = pd.DataFrame(data)

    print("===== DATASET =====")
    print(df)

    # --------------------------------
    # 2. Central Tendency
    # --------------------------------

    print("\n===== CENTRAL TENDENCY =====")

    print("Mean:", df["Marks"].mean())
    print("Median:", df["Marks"].median())
    print("Mode:", df["Marks"].mode()[0])

    # --------------------------------
    # 3. Histogram
    # --------------------------------

    plt.figure(figsize=(8, 5))

    plt.hist(
        df["Marks"],
        bins=5,
        edgecolor="black"
    )

    plt.title("Histogram of Marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.grid(axis="y", alpha=0.3)

    plt.show()

    # --------------------------------
    # 4. Box Plot
    # --------------------------------

    plt.figure(figsize=(8, 5))

    plt.boxplot(df["Marks"])

    plt.title("Box Plot of Marks")
    plt.ylabel("Marks")
    plt.grid(axis="y", alpha=0.3)

    plt.show()

    # --------------------------------
    # 5. Violin Plot
    # --------------------------------

    plt.figure(figsize=(8, 5))

    plt.violinplot(df["Marks"])

    plt.title("Violin Plot of Marks")
    plt.ylabel("Marks")
    plt.grid(axis="y", alpha=0.3)

    plt.show()


if __name__ == "__main__":
    main()