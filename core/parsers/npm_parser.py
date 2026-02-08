import sys
import os

# Ensure project's root is on sys.path so `core` package is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from core.npm_checker import NPMChecker
import json

def npm_parser(package_name: str, output_file):    
    checker = NPMChecker()
    checker.check_package(package_name)
    data = checker.get_data(package_name)

    if output_file:
        with open(output_file, "w") as f:
            json.dump(data, f, indent=2)
    return data

if __name__ == "__main__":
    npm_parser("react", "requests_data2.json")