import marimo

__generated_with = "0.19.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Fertilizer Use and Crop Response Analysis

    In this exercise, you will analyze farm-level data to understand how efficiently
    fertilizer is converted into crop production.

    You will practice:
    - Python basics
    - NumPy
    - Pandas
    - Loops
    - Groupby, filtering, lambda functions
    - Basic data visualization

    This is an **instructional exercise**. Focus on clarity, not complexity.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    return (pd,)


@app.cell
def _(mo):
    mo.md("""
    ## Dataset Description

    The agricultural extension office collected the following information:

    - **Farm_ID** – Unique farm identifier
    - **Crop** – Crop planted
    - **Fertilizer_kg** – Amount of fertilizer applied (kg)
    - **Production_tons** – Total crop production (tons)

    The dataset below represents **one planting season**.
    """)
    return


@app.cell
def _(pd):
    data = {
        "Farm_ID": ["F001", "F002", "F003", "F004", "F005", "F006"],
        "Crop": ["Rice", "Corn", "Rice", "Banana", "Corn", "Rice"],
        "Fertilizer_kg": [120, 90, 150, 110, 80, 140],
        "Production_tons": [10.0, 7.2, 11.5, 18.0, 5.5, 8.0]
    }

    df = pd.DataFrame(data)
    df
    return


@app.cell
def _(mo):
    mo.md("""
    ## Task 1: Data Exploration

    1. Display the **first 5 rows** of the dataset.
    2. Display the **data types** of each column.
    3. Display **summary statistics** for numerical columns.

    This step helps you understand the structure of the data.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ## Task 2: Fertilizer Efficiency Index (FEI)

    Define the **Fertilizer Efficiency Index (FEI)** as:

    FEI = Production (tons) ÷ Fertilizer applied (kg)

    ### Instructions:
    1. Create a new column called **FEI**
    2. Round the FEI values to **3 decimal places**

    FEI represents how efficiently fertilizer is converted into production.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ## Task 3: Identifying Inefficient Fertilizer Use

    A farm is considered **inefficient** if:

    FEI < 0.07

    ### Instructions:
    1. Filter farms with FEI less than 0.07
    2. Display only the following columns:
       - Farm_ID
       - Crop
       - Fertilizer_kg
       - FEI
     These farms may require fertilizer optimization or soil testing.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ## Task 4: Average Fertilizer Efficiency by Crop

    ### Instructions:
    1. Compute the **average FEI** for each crop.
    2. Sort the results from **highest to lowest**.

    This shows which crops respond best to fertilizer application.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ## Task 5: Advisory Messages Using Loops

    Using the **average FEI per crop**, print advisory messages:

    - **High efficiency**: FEI ≥ 0.10
    - **Moderate efficiency**: 0.07–0.099
    - **Low efficiency**: FEI < 0.07

    Use a **for loop** and conditional statements.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ## Task 6: Efficiency Classification Using Lambda

    ### Instructions:
    1. Create a new column called **Efficiency_Class**
    2. Use a **lambda function**:
       - "Efficient" if FEI ≥ 0.08
       - "Inefficient" otherwise
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ## Task 7: Data Visualization

    ### A. Bar Chart
    Create a **bar chart** showing the average FEI per crop.

    ### B. Scatter Plot
    Create a **scatter plot** with:
    - x-axis: Fertilizer_kg
    - y-axis: Production_tons
    - Color by Crop

    Label axes and add titles to your plots.
    """)
    return


@app.cell
def _():
    # Write your solution here
    return


@app.cell
def _(mo):
    mo.md("""
    ## Reflection Questions

    1. Which crop uses fertilizer most efficiently?
    2. Does applying more fertilizer always increase production?
    3. How can this analysis help farmers make better decisions?
     Answer briefly in your own words.
    """)
    return


if __name__ == "__main__":
    app.run()
