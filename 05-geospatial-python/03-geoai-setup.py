import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # GeoAI Programming Exercise

    ## Working Environment Setup

    ###Introduction

    This document describes how to configure the working environment for the GeoAI training module. The goal of this training is to demonstrate how GeoAI workflows can be implemented using both QGIS and Python. QGIS will be used not only for spatial data preparation and visualization but also to demonstrate simple GeoAI workflows within a GIS environment. Python will be used for more flexible and programmable machine learning workflows using scikit-learn and the GeoAI library developed by Qiusheng Wu.

    Because geospatial software depends on compiled system components such as GDAL and PROJ, proper installation and environment isolation are necessary, especially on Windows systems. A well-configured environment ensures stability, reproducibility, and consistent behavior across training participants.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Software Components Used in This Training

    This module integrates two complementary environments: QGIS and Python.

    QGIS will be used for spatial data exploration, preprocessing, visualization, raster analysis, and demonstration of simple GeoAI workflows. This includes using built-in processing tools and graphical model builders to perform classification or predictive tasks in a no-code or low-code environment. The objective is to help trainees understand how GeoAI concepts can be implemented directly within a desktop GIS platform.

    Python will be used for programmable GeoAI workflows. Within Python, we will focus specifically on scikit-learn for classical machine learning algorithms and the GeoAI library by Qiusheng Wu for geospatial AI utilities. Python allows greater flexibility, reproducibility, and customization of models beyond what is available in a purely graphical interface.

    This training intentionally avoids deep learning frameworks and advanced AI libraries to maintain conceptual clarity and reduce setup complexity.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Installing QGIS (Windows)

    Download the Long Term Release (LTR) version of QGIS from the official website. The LTR version is recommended for training purposes because it is stable and widely supported.

    Install QGIS using the default installation settings. After installation, launch QGIS to confirm that it opens correctly. Ensure that the Processing Toolbox is available, as it will be used for demonstrating spatial analysis and simple machine learning workflows.

    No additional plugins are required at this stage unless specified in later modules.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Installing Python and uv (Windows)

    For this training module, we will use uv as our Python package and environment manager. uv replaces both pip and traditional virtual environment management by automatically creating and managing isolated environments within the project directory.

    First, install Python 3.11 or newer from the official Python website. During installation, ensure that the option to add Python to the system PATH is enabled.

    After Python is installed, open PowerShell and install uv:

    > pip install uv


    Verify installation:

    > uv --version


    If a version number appears, uv is correctly installed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Initializing the Project Environment

    Navigate to your project directory and initialize a new Python project:

    > uv init


    This creates a pyproject.toml file, which defines project metadata and dependencies.

    Unlike traditional workflows, there is no need to manually create or activate a virtual environment. uv automatically creates and manages a .venv directory when dependencies are installed or synchronized.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Installing Required Python Libraries

    Install the required geospatial and machine learning libraries:

    > uv add geopandas rasterio numpy pandas matplotlib scikit-learn


    Install the GeoAI library by Qiusheng Wu:

    > uv add geoai-py


    If marimo will be used for interactive training notebooks:

    > uv add marimo


    When these commands are executed, uv automatically creates an isolated virtual environment inside the project folder and installs the dependencies there.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Running Python Within the Project

    To run Python using the managed environment, use:

    > uv run python


    To launch marimo:

    > uv run marimo edit


    There is no need to manually activate .venv. uv ensures commands run inside the correct environment.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Reproducibility

    uv maintains dependency versions inside pyproject.toml and a lock file. To recreate the environment on another machine, simply run:

    > uv sync


    This installs the exact locked versions, ensuring consistent behavior across all trainees.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###
    """)
    return


if __name__ == "__main__":
    app.run()
