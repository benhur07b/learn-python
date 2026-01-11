---
title: "Notebooks"
description: "Use notebooks to write executable code alongside markdown, visualizing results in real time, and sharing insights through dynamic, shareable documents ideal for education, research, and data-driven storytelling."
---

Interactive notebooks have become indispensable tools for data science, education, and exploratory programming. Notebooks are used to write executable code alongside markdown, visualize results in real time, and share insights through dynamic, shareable documents ideal for education, research, and data-driven storytelling.

## Jupyter
- https://jupyter.org/
- De facto standard for interactive computing in Python
- JupyterLab: latest web-based interactive development environment for notebooks, code, and data.
- Jupyter Notebook: original web application for creating and sharing computational documents. It offers a simple, streamlined, document-centric experience.
- Can be used for more than Python (e.g. R, Julia)
- Files are notebook files (.ipynb)

### Usage

#### Install JupyterLab

When inside a uv project, run:    
```sh
uv add jupyterlab
```

With a conda environment activated, run:
```sh
conda install -c conda-forge jupyter lab
```

Using pip
```sh
pip install jupyterlab
```

#### Run JupyterLab

When inside a uv project, run:
```sh
uv run jupyter lab
```

With an environment activated, run:

```sh
jupyter lab
```

## marimo
- https://marimo.io/
- next-generation Python notebooks
- **reactive**: if a variable is changed on one cell, dependent cells are automatically updated
- built-in interactive elements
- Python-first, outputs are stored as standard Python scripts (.py)

### Usage

#### Install marimo:
When inside a uv project, run:
```sh
uv add marimo
```

With a conda environment activated, run:
```sh
conda install -c conda-forge marimo
```

Using pip:
```sh
pip install marimo
```

#### Run marimo
Create or edit notebook
```sh
marimo edit PYTHON_SCRIPT.py
```

Run as read-only app
```sh
marimo run PYTHON_SCRIPT.py
```

Run marimo with uv
```sh
uv run marimo <MARIMO COMMANDS>
```