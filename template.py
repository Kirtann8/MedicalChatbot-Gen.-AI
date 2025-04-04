import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py", 
    "env",  # This should be handled as a directory
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    if filepath.suffix == "":  # If there's no file extension, treat it as a directory
        os.makedirs(filepath, exist_ok=True)
        logging.info(f"Creating directory: {filepath}")
        continue  # Skip file creation for directories

    filedir = filepath.parent

    if filedir != Path("."):  # Ignore if it's in the root directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filepath.name}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
