---
title: "Environment and package management"
description: "Ensure reproducibility and avoid conflicts in your projects."
---

## The Dependency Problem  
Python applications often rely on external libraries (packages) that are not included in the standard Python installation. A common challenge arises when **two projects require conflicting versions of the same library**:  

For example:
- **Project A** might need `pandas` version **1.0**.  
- **Project B** might need `pandas` version **2.0**.  

If you install `pandas` 2.0 globally (i.e., system-wide), **Project A might break** because it expects an older version. 

```{caution}
This creates a **fragile development environment and complicates collaboration, testing, and deployment**.
```

## The "It Works On My Machine" Problem

Another common issue especially when working in a team: **code that works locally may fail in other environments** (e.g., on a teammate’s machine, a CI/CD pipeline, or production). 

For example:  
- A developer might install dependencies globally (see above), leading to version mismatches elsewhere.  
- A project might rely on system-specific configurations or tools that are not replicated in other environments. 

```{caution}
This results in **unreliable workflows, wasted time debugging, and frustration for teams**.  
```


## The Solution 01: Virtual Environments

A **virtual environment** is a self-contained directory that isolates Python installations and packages for a specific project.

**Key benefits**:  
- **Isolation**: Each project has its own Python interpreter and package versions.  
  - *Project A* uses its own environment with `pandas` 1.0.  
  - *Project B* uses a separate environment with `pandas` 2.0.  
- **No conflicts**: Upgrading one project’s dependencies does not affect others.

## The Solution 02: Package Managers
**Package managers** automate dependency management, ensuring consistent and reliable installations across environments.  

**Key benefits**:  
- **Dependency resolution**: Automatically installs required packages and their dependencies.  
- **Version control**: Locks package versions to avoid conflicts.
- **Reproducibility**: Ensures the same environment can be recreated on any machine (e.g., using `requirements.txt`, `pipfile`, `pyproject.toml`).  


## The Usual Workflow
### Creating a virtual environment
1. Create a virtual environment.
2. Activate the virtual environment (steps depend on tool and OS used).
3. Install project-specific packages in the activated environment.

```{note}
Make sure that the virtual environment is activated before installing any packages. When a virtual environment is active, the terminal prompt typically changes to indicate its name, often displayed in parentheses. For example:  

```sh
(virtual-environment) user@machine:/path/to/project/
```

```{note}
You can also check which python is currently being used by running this command on your terminal/shell.

```sh
which python
```


## Common Tools
### venv

- `venv` is a built-in virtual environment manager in Python (since Python 3.3)
- https://docs.python.org/3/library/venv.html

#### Usage
To **create** a virtual environment named `myvenv` inside the `/my/python/project` folder 
```sh
python -m myvenv /my/python/project
```

To **activate** the `myvenv` environment (assuming you are already inside the `/my/python/project` folder):

**Linux/MacOS**
```sh
source .venv/bin/activate
```

**Windows**
```sh
.venv\Scripts\activate
```

To **deactivate** a virtual environment
```sh
deactivate
```

### pip
- `pip` is the default package installer for Python
- https://pip.pypa.io/en/stable/

#### Usage
To **install** packages using `pip`:
```sh
pip install <PACKAGE>
```

**specific version**
```sh
pip install <PACKAGE>==version
```

**from a GitHub repository**
```sh
pip install git+GITHUB-REPO-URL
```

**using requirements.txt**

A `requirements.txt` file is a **text file** used in Python projects to list all the **packages and their exact versions** required to run the project. It ensures that the same dependencies are installed consistently across different environments (e.g., development, testing, production) and helps collaborators or deployment systems recreate the project’s environment accurately.

```sh
pip install -r requirements.txt
```

To **upgrade** a package:
```sh
pip install --upgrade <PACKAGE>
```

To **uninstall** a package:
```sh
pip uninstall <PACKAGE>
```

To **create a `requirements.txt`** file:
```sh
pip freeze > requirements.txt
```

:::note[FREEZING REQUIREMENTS]
The `pip freeze` command captures all installed packages and their versions in the current environment and sends the list to a file (e.g. `requirements.txt`).

This file can then be used to install the same packages in another environment.
:::


### conda and conda re-implementations
- `conda` (https://docs.conda.io/en/latest/) is a cross-platform package and environment manager
- manages packages, dependencies, and environments
- supports packages from different languages, not just Python
- `miniconda` 
    - minimal installation of conda
    - uses the `conda` command
    - https://www.anaconda.com/docs/getting-started/miniconda/main
- `mamba` 
    - faster reimplementation of conda
    - uses the `mamba` command
    - https://mamba.readthedocs.io/en/latest/

#### Usage
To **create** a virtual environment named `myvenv`:
```sh
conda create -n myvenv
```

**using a specific Python version**
```sh
conda create -n myvenv python=version.number
```

To **list** conda environments in the machine:
```sh
conda env list
``` 

To **remove** an environment named `myvenv`:
```sh
conda remove -n myvenv --all
```

To **activate** an environment named `myvenv`:
```sh
conda activate myvenv
```

To **deactivate** an environment:
```sh
conda deactivate
```

To **install** packages with `conda`:

**current environment**
```sh
conda install <PACKAGE>
```

**specific environment**
```sh
conda install -n myvenv <PACKAGE>
```

**from conda-forge channel**
```sh
conda install -c conda-forge <PACKAGE>
```

**multiple packages**
```sh
conda install <PACKAGE1> <PACKAGE2> <PACKAGE3>
```

To **update** packages:
```sh
conda update <PACKAGE>
```

**from a specific channel**
```sh
conda update <PACKAGE> --override-channels --channel <CHANNEL>
```

**multiple packages**
```sh
conda update <PACKAGE1> <PACKAGE2> <PACKAGE3>
```

**all packages**
```sh
conda update --all
```

To **search** for a package:
```sh
conda search <PACKAGE>
```

To **list** packages in the current environment:
```sh
conda list
```

To **remove** a package in the current environment:
```sh
conda remove <PACKAGE>
```

```{tip}
**NEED SPEED? TRY MAMBA**

Install `mamba` in the environment:
```sh
conda install -n base mamba -c conda-forge
```

### uv
- `uv` is an extremely fast, modern tool that replaces and unifies environment and package management
- https://docs.astral.sh/uv/
- **GREAT FOR PYTHON-ONLY LIBRARIES**

#### Usage
To install `uv`:
**Linux and macOS**
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows**
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

To **create/initialize** a project:
```sh
uv init
```
<figcaption>This creates a virtual environment `.venv` inside the project folder</figcaption>

To **add** a dependency to a project:
```sh
uv add <PACKAGE>
```

To **remove** a dependency to a project:
```sh
uv remove <PACKAGE>
```

To **run** a command in the project environment:
```sh
uv run <COMMAND>
```

`uv` can also interface with `pip` to manually manage environments and packages. Simply add the `uv` command in front of the usual `venv` and `pip` commands.

**create a virtual environment**
```sh
uv venv ...
```

**install packages with pip**
```sh
uv pip install ...
```

**uninstall packages with pip**
```sh
uv pip uninstall ...
```

```{tip} 
**USE UV WITH CONDA**

You can also install `uv` inside a conda environment. This gives you:
1. speed when installing Python packages w/ `uv`
2. compatibility with other packages available in `conda`
```

## Why This Matters  
Virtual environments and package managers are **cornerstones of modern Python development**. They solve the dependency problem, eliminate the “It Works On My Machine” dilemma, and ensure: 

- **Collaboration**: Team members can work on the same project without conflicts.  
- **Reproducibility**: Code behaves consistently across development, testing, and production.  
- **Scalability**: Projects grow without breaking existing functionality.  

```{tip} 
**PRO-TIP**

By mastering these virtual environments and package managers, you’ll avoid common pitfalls and build robust, maintainable Python applications.
```