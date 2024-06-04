import uuid
from datetime import datetime
import json
import os

class Registry():
    def __init__(self):
        self.students_record = {"students": {}}

    def write_json(self, data):
        try:
            with open('students.json', 'w') as file:
                json.dump(data, file, indent=2)
        except json.JSONDecodeError as e:
            print(f"Error encoding JSON: {e}")

    def read_json(self):
        try:
            with open('students.json', 'r') as file:
                data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
        except FileNotFoundError:
            return None

    def get_unique_id(self):
        today = datetime.now().strftime("%Y-%m-%d")
        unique_id = str(uuid.uuid4())
        return f"{today}-{unique_id}"

    def add_students(self):
        self.students_record = self.read_json()
        if self.students_record is None:
            self.students_record = {"students": {}}
        new_student = input("Please enter the name of the student: ")
        student_id = self.get_unique_id()
        self.students_record["students"][student_id] = new_student
        print(f"Student {new_student} added successfully!")
        self.write_json(self.students_record)  # Corrected method invocation

# Create an empty students.json file if it doesn't exist
if not os.path.exists('students.json'):
    with open('students.json', 'w') as file:
        json.dump({"students": {}}, file)

# registry = Registry()
# registry.add_students()
