# python_project_full_template

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate virtual environment with uv
uv sync
source .venv/bin/activate

# Installing dependencies
uv pip install -e .  # Install the package in development mode

# Code Formatting
uvx ruff format .  # Format code with ruff

# Linting
uvx ruff check .  # Run ruff linter
uvx ruff check --fix .  # Run ruff with auto-fix
uvx pylint src/mypackage1 src/mypackage2  # Run pylint

# Type Checking
uvx mypy src/mypackage1 src/mypackage2  # Run type checking

# Testing
pytest  # Run all tests with pytest
pytest tests/test_module1.py  # Run specific test file
pytest -xvs  # Run with verbose output and stop on first failure
python -m unittest tests/unittest_example.py  # Run unittest tests


# Run the main demo
python main.py  # Run all demos
python main.py --demo text  # Run text utilities demo
python main.py --demo data  # Run data validation demo
python main.py --demo cmd  # Run interactive cmd shell
python main.py --demo unittest  # Run unittest examples

# Run the cmd example directly
python cmd_example.py
```

## NOTE: `~/.zshrc`controls caching of python packages.