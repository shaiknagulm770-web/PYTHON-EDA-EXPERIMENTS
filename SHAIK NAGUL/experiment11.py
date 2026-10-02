import pandas as pd
import matplotlib.pyplot as plt


def main():

    # --------------------------------
    # 1. Creating Time Series Dataset
    # --------------------------------

    data = {
        "Date": [
            "2026-01-01",
            "2026-02-01",
            "2026-03-01",
            "2026-04-01",
            "2026-05-01",
            "2026-06-01",
            "2026-07-01",
            "2026-08-01",
            "2026-09-01",
            "2026-10-01",
            "2026-11-01",
            "2026-12-01"
        ],
        "Sales": [
            120, 135, 150, 145, 170, 180,
            175, 190, 210, 205, 225, 240
        ]
    }

    df = pd.DataFrame(data)

    print("===== ORIGINAL DATASET =====")
    print(df)

    # --------------------------------
    # 2. Parse Date-Time Column
    # --------------------------------

    df["Date"] = pd.to_datetime(df["Date"])

    print("\n===== PARSED DATE-TIME =====")
    print(df)

    # --------------------------------
    # 3. Set Date-Time as Index
    # --------------------------------

    df.set_index("Date", inplace=True)

    print("\n===== DATE-TIME INDEXED DATA =====")
    print(df)

    # --------------------------------
    # 4. Visualize Trend
    # --------------------------------

    plt.figure(figsize=(10, 5))

    plt.plot(
        df.index,
        df["Sales"],
        marker="o"
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.grid(True, alpha=0.3)

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

    # --------------------------------
    # 5. Visualize Seasonality
    # --------------------------------

    df["Month"] = df.index.month

    monthly_average = df.groupby("Month")["Sales"].mean()

    plt.figure(figsize=(10, 5))

    plt.plot(
        monthly_average.index,
        monthly_average.values,
        marker="o"
    )

    plt.title("Monthly Seasonality")
    plt.xlabel("Month")
    plt.ylabel("Average Sales")
    plt.xticks(range(1, 13))
    plt.grid(True, alpha=0.3)

    plt.show()


if __name__ == "__main__":
    main()