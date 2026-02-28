import json


def export(checker, package_name, output_file):
    checker = checker()
    checker.check_package(package_name)
    data = checker.get_data(package_name)
    if output_file:
        with open(output_file, "w") as f:
            json.dump(data, f, indent=2)
    return data