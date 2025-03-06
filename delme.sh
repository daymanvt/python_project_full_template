#!/bin/bash

# Script to rename the project structure from generic names to more descriptive ones
# Usage: bash rename_project.sh

set -e  # Exit on any error

echo "Starting project renaming process..."

# Create backup of the project
echo "Creating backup..."
TIMESTAMP=$(date +%Y%m%d%H%M%S)
BACKUP_DIR="../project_backup_$TIMESTAMP"
mkdir -p "$BACKUP_DIR"
cp -r ./* "$BACKUP_DIR/"
echo "Backup created at $BACKUP_DIR"

# Create new directory structure
echo "Creating new directory structure..."
mkdir -p src/textkit/advanced
mkdir -p src/dataval/validation

# Rename and move files
echo "Renaming and moving files..."

# mypackage1 -> textkit
cp src/mypackage1/__init__.py src/textkit/__init__.py
cp src/mypackage1/module1.py src/textkit/analyzer.py
cp src/mypackage1/module2.py src/textkit/transformer.py
cp src/mypackage1/cli.py src/textkit/cli.py
cp src/mypackage1/subpackage/__init__.py src/textkit/advanced/__init__.py
cp src/mypackage1/subpackage/module3.py src/textkit/advanced/summarizer.py

# mypackage2 -> dataval
cp src/mypackage2/__init__.py src/dataval/__init__.py
cp src/mypackage2/module1.py src/dataval/validators.py
cp src/mypackage2/module2.py src/dataval/transformers.py
cp src/mypackage2/cmd_example.py src/dataval/shell.py
cp src/mypackage2/subpackage/__init__.py src/dataval/validation/__init__.py
cp src/mypackage2/subpackage/module3.py src/dataval/validation/schema.py

# Update imports and references in all files
echo "Updating file contents with new package and module names..."

# Update textkit files
sed -i 's/mypackage1/textkit/g' src/textkit/*.py src/textkit/advanced/*.py
sed -i 's/from textkit.module1/from textkit.analyzer/g' src/textkit/*.py src/textkit/advanced/*.py
sed -i 's/import textkit.module1/import textkit.analyzer/g' src/textkit/*.py src/textkit/advanced/*.py
sed -i 's/from textkit.module2/from textkit.transformer/g' src/textkit/*.py src/textkit/advanced/*.py
sed -i 's/import textkit.module2/import textkit.transformer/g' src/textkit/*.py src/textkit/advanced/*.py
sed -i 's/from textkit.subpackage.module3/from textkit.advanced.summarizer/g' src/textkit/*.py src/textkit/advanced/*.py
sed -i 's/import textkit.subpackage.module3/import textkit.advanced.summarizer/g' src/textkit/*.py src/textkit/advanced/*.py

# Update dataval files
sed -i 's/mypackage2/dataval/g' src/dataval/*.py src/dataval/validation/*.py
sed -i 's/from dataval.module1/from dataval.validators/g' src/dataval/*.py src/dataval/validation/*.py
sed -i 's/import dataval.module1/import dataval.validators/g' src/dataval/*.py src/dataval/validation/*.py
sed -i 's/from dataval.module2/from dataval.transformers/g' src/dataval/*.py src/dataval/validation/*.py
sed -i 's/import dataval.module2/import dataval.transformers/g' src/dataval/*.py src/dataval/validation/*.py
sed -i 's/from dataval.subpackage.module3/from dataval.validation.schema/g' src/dataval/*.py src/dataval/validation/*.py
sed -i 's/import dataval.subpackage.module3/import dataval.validation.schema/g' src/dataval/*.py src/dataval/validation/*.py
sed -i 's/cmd_example/shell/g' src/dataval/*.py

# Update main.py
sed -i 's/mypackage1/textkit/g' main.py
sed -i 's/mypackage2/dataval/g' main.py
sed -i 's/import textkit.module1/import textkit.analyzer/g' main.py
sed -i 's/import textkit.module2/import textkit.transformer/g' main.py
sed -i 's/import dataval.module1/import dataval.validators/g' main.py
sed -i 's/import dataval.module2/import dataval.transformers/g' main.py
sed -i 's/from dataval.validation.schema/from dataval.validation.schema/g' main.py
sed -i 's/import dataval.cmd_example/import dataval.shell/g' main.py
sed -i 's/dataval.cmd_example.main/dataval.shell.main/g' main.py

# Update test files
sed -i 's/mypackage1/textkit/g' tests/*.py
sed -i 's/mypackage2/dataval/g' tests/*.py
sed -i 's/from textkit.module1/from textkit.analyzer/g' tests/*.py
sed -i 's/import textkit.module1/import textkit.analyzer/g' tests/*.py
sed -i 's/from textkit.module2/from textkit.transformer/g' tests/*.py
sed -i 's/import textkit.module2/import textkit.transformer/g' tests/*.py
sed -i 's/from dataval.module1/from dataval.validators/g' tests/*.py
sed -i 's/import dataval.module1/import dataval.validators/g' tests/*.py
sed -i 's/from dataval.module2/from dataval.transformers/g' tests/*.py
sed -i 's/import dataval.module2/import dataval.transformers/g' tests/*.py
sed -i 's/from dataval.validation.schema/from dataval.validation.schema/g' tests/*.py
sed -i 's/import dataval.validation.schema/import dataval.validation.schema/g' tests/*.py

# Update README.md
sed -i 's/mypackage1/textkit/g' README.md
sed -i 's/mypackage2/dataval/g' README.md
sed -i 's/cmd_example.py/shell.py/g' README.md
sed -i 's/python -m mypackage2.cmd_example/python -m dataval.shell/g' README.md

# Update setup.py
sed -i 's/name="delta-313"/name="textutils"/g' setup.py
sed -i 's/"mypackage1.cli:main"/"textkit.cli:main"/g' setup.py

# Update pyproject.toml
sed -i 's/name = "demo-project"/name = "textutils"/g' pyproject.toml
sed -i 's/textutils = "mypackage1.cli:main"/textutils = "textkit.cli:main"/g' pyproject.toml
sed -i 's/known-first-party = \["mypackage1", "mypackage2"\]/known-first-party = \["textkit", "dataval"\]/g' .ruff.toml

# Update pylint config
sed -i 's/src\/mypackage1/src\/textkit/g' .mypy.ini
sed -i 's/src\/mypackage2/src\/dataval/g' .mypy.ini

echo "Performing final cleanup..."
# Remove old directories after successful copies and updates
rm -rf src/mypackage1
rm -rf src/mypackage2

echo "Project renaming complete!"
echo "The old structure has been backed up to $BACKUP_DIR"
echo "Please review the changes before committing them."