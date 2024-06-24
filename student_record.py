import uuid
from datetime import datetime
import json

class Students:
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

    def get_unique_id(self):
        today = datetime.now().strftime("%Y-%m-%d")
        unique_id = str(uuid.uuid4())
        return f"{today}-{unique_id}"

    def students_exist(self):
        self.students_record = self.read_json()
        return self.get_unique_id() in self.students_record

    def add_students(self):
        self.students_record = self.read_json()
        if self.students_record is None:
            self.students_record = {"students": {}}
        new_student = input("Please enter the name of the student: ")
        student_id = self.get_unique_id()
        self.students_record["students"][student_id] = new_student
        print(f"Student {new_student} added successfully!")
        self.write_json(self.students_record)

    def edit_student(self):
        self.students_record = self.read_json()
        self.student_id = input("Please enter the Student ID: ")
        if self.student_id in self.students_record["students"]:
            enter_new_name = input("Please enter the new name for the student: ")
            self.students_record["students"][self.student_id] = enter_new_name
            print(f"Student {self.student_id} updated successfully!")
            self.write_json(self.students_record)
        else:
            print(f"Student with ID {self.student_id} not found.")

    def delete_student(self):
        self.students_record = self.read_json()
        self.student_id = input("Please enter the Student ID: ")

        if self.student_id in self.students_record["students"]:
            removed_student_name = self.students_record["students"].pop(self.student_id)
            print(f"Student with ID {self.student_id} ({removed_student_name}) removed successfully!")
            self.write_json(self.students_record)
        else:
            print(f"Student with ID {self.student_id} not found.")

    def show_students(self):
        self.students_record = self.read_json()
        for student_name in self.students_record.get("students", {}).values():
            print(student_name)


students = Students()

def Records():

    while True:
        student_input = input("Please enter:\n1. Show students\n2. Add students\n3. Edit student\n4. Delete student\n5. Exit\n")
        if student_input == "1":
            students.show_students()
            break
        elif student_input == "2":
            students.add_students()
            break
        elif student_input == "3":
            students.edit_student()
            break
        elif student_input == "4":
            students.delete_student()
            break
        elif student_input == "5":
            break
        else:
            print("Please enter 1, 2, 3, 4, or 5 to continue. Try again.")

