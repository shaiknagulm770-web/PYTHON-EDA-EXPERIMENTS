import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def main():

    # --------------------------------
    # 1. Creating Dataset
    # --------------------------------

    data = {
        "Month": [
            "Jan", "Feb", "Mar", "Apr",
            "May", "Jun", "Jul", "Aug"
        ],
        "Sales": [120, 135, 150, 145, 170, 180, 175, 195],
        "Profit": [20, 25, 30, 28, 35, 40, 38, 45],
        "Customers": [50, 55, 60, 58, 65, 70, 68, 75]
    }

    df = pd.DataFrame(data)

    print("===== DATASET =====")
    print(df)

    # --------------------------------
    # 2. Interactive Line Graph
    # --------------------------------

    line_fig = px.line(
        df,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Sales"
    )

    line_fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Sales"
    )

    line_fig.show()

    # --------------------------------
    # 3. Interactive Scatter Plot
    # --------------------------------

    scatter_fig = px.scatter(
        df,
        x="Customers",
        y="Sales",
        size="Profit",
        hover_data=["Month"],
        title="Customers vs Sales"
    )

    scatter_fig.show()

    # --------------------------------
    # 4. Dashboard
    # --------------------------------

    dashboard = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Monthly Sales",
            "Monthly Profit",
            "Customers vs Sales",
            "Sales and Profit"
        )
    )

    # Sales Line Chart
    dashboard.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Sales"],
            mode="lines+markers",
            name="Sales"
        ),
        row=1,
        col=1
    )

    # Profit Bar Chart
    dashboard.add_trace(
        go.Bar(
            x=df["Month"],
            y=df["Profit"],
            name="Profit"
        ),
        row=1,
        col=2
    )

    # Customers vs Sales
    dashboard.add_trace(
        go.Scatter(
            x=df["Customers"],
            y=df["Sales"],
            mode="markers",
            name="Customers vs Sales"
        ),
        row=2,
        col=1
    )

    # Sales and Profit
    dashboard.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Sales"],
            mode="lines+markers",
            name="Sales"
        ),
        row=2,
        col=2
    )

    dashboard.add_trace(
        go.Scatter(
            x=df["Month"],
            y=df["Profit"],
            mode="lines+markers",
            name="Profit"
        ),
        row=2,
        col=2
    )

    dashboard.update_layout(
        title_text="Sales Dashboard",
        height=800,
        showlegend=True
    )

    dashboard.show()


if __name__ == "__main__":
    main()