import json

class MultiDictJSONHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_json(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        return data

    def write_json(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)


