## Installation

### Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Quick Install (with uv - recommended)

```bash
git clone https://github.com/craigmonaghan/pkg-check
cd pkg-check
uv pip install -e .
```

### Alternative Install (with pip)
```bash
git clone https://github.com/craigmonaghan/pkg-check
cd pkg-check
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

### Making the Command Available Globally

The tool will be installed in your virtual environment. You have two options:

**Option 1:** Activate the virtual environment when using it:
```bash
source .venv/bin/activate  # Run this in each new terminal
pkg-check npm react
```

**Option 2:** Create a shell alias (recommended for convenience):

Add to your `~/.bashrc` or `~/.zshrc`:
```bash
# Adjust the path to where you cloned the repo
alias pkg-check="/path/to/pkg-check/.venv/bin/pkg-check"
```

Then reload your shell:
```bash
source ~/.bashrc  # or ~/.zshrc
```

Now `pkg-check` works from any directory without activating the venv!

## Usage

Check a package from any source:
```bash
pkg-check npm <package-name>
pkg-check pypi <package-name>
pkg-check aur <package-name>
```

### Examples
```bash
# Check NPM packages
pkg-check npm express
pkg-check npm react

# Check Python packages
pkg-check pypi requests
pkg-check pypi django

# Check AUR packages (Arch Linux)
pkg-check aur yay
pkg-check aur neovim-git
```

### Help
```bash
pkg-check --help
pkg-check npm --help
```

## Development

The `-e` flag installs in editable mode - code changes take effect immediately without reinstalling.

To make changes:
1. Edit any `.py` file
2. Changes work immediately (no reinstall needed)
3. Only reinstall if you modify `pyproject.toml`

## Uninstallation
```bash
uv pip uninstall pkg-check
```

Or with pip:
```bash
pip uninstall pkg-check
```