import json


def read_json_file(file_path):
    """Reads a JSON file and returns the data. Returns [] if file doesn't exist or is invalid."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_json_file(file_path, data):
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise IOError(f"Error writing to file {file_path}: {e}")
