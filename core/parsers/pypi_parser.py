import sys
import os
from core.pypi_checker import PyPiChecker
import sys
import os

# Ensure project's root is on sys.path so `core` package is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.pypi_checker import PyPiChecker
import json


def pypi_parser(package_name: str, output_file):    
    checker = PyPiChecker()
    data = checker.get_data(package_name)
    with open(output_file, "w") as f:
            json.dump(data, f, indent=2)
    return data

if __name__ == "__main__":
    pypi_parser("setuptools", "requests_data2.json")