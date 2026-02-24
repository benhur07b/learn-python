# Learn Python w/ BNHR
Built with [Jupyter Book](https://jupyterbook.org).

## Local deployment and development

### 📦 Requirements

Before getting started, ensure you have the following installed on your system:

- [Python](https://www.python.org/) (3.8+)
- [Node.js](https://nodejs.org/) (you can use [nvm](https://github.com/nvm-sh/nvm) to manage Node versions)
- [uv](https://github.com/astral-sh/uv) (modern Python package manager)

---

### 🚀 Getting Started

#### 1. Install Node.js with nvm

If you haven't already installed [nvm](https://github.com/nvm-sh/nvm), follow the installation instructions for your operating system.

Once nvm is installed, open a new terminal and run:

```bash
nvm install node
```

This will install the latest stable version of Node.js. You can then enable the default/latest node version with:

```bash
nvm use node
```

You can check which node and npm versions are running with:

```bash
node -v
npm -v
```

---

#### 2. Install Project Dependencies

Navigate to the root directory of this project and install the required Python dependencies:

```bash
uv sync
```

This command will install all dependencies listed in the `pyproject.toml` file.

---

#### 3. Run the Jupyter Book Locally

Once dependencies are installed, start the Jupyter Book server with:

```bash
uv run jupyter book start
```

This will build and serve the book on your local machine. Open your browser and navigate to:

```
http://localhost:3000
```

You can now explore the book interactively!

---

## 🛠️ Troubleshooting

- **Node.js not found**: Ensure you've reloaded your terminal after installing nvm, or run `source ~/.nvm/nvm.sh`.
- **uv not found**: Install uv using [these instructions](https://github.com/astral-sh/uv#installation).
- **Build errors**: Ensure all dependencies are installed with `uv sync`.

---