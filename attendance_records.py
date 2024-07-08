from student_record import Students
import json
import datetime

class Attendance:
    def __init__(self):
        self.students = Students()
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.attendance_records ={}

    def write_attendance_json(self, data):
        try:
            with open('attendance_records.json', 'w') as file:
                json.dump(data, file, indent=2)
        except json.JSONDecodeError as e:
            print(f"Error encoding JSON: {e}")

    def read_attendance_json(self):
        try:
            with open('attendance_records.json', 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print("Attendance file not found. Creating a new one.")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

    def attendance_record(self):
        self.students.students_record = self.students.read_json()

        if self.students.students_record is None:
            return

        self.attendance_records = self.read_attendance_json()
        self.day = datetime.datetime.now().strftime("%Y-%m_%d")

        while True:

            self.tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

            if self.attendance_records is None:
                self.attendance_records = {}

            if self.day in self.attendance_records:
                print(f" Attendance of {self.day} is already recorded .")
                break



            self.attendance_record_for_day = {}



            for key in self.students.students_record.get("students" , {}).keys():
                self.registry = input(f"Is {self.students.students_record['students'][key]} present or absent?\n")
                if self.registry == "present".lower():
                    self.attendance_record_for_day[key] = { "student_id "  : self.students.students_record["students"][key] , "present" : self.registry}
                else:
                    print("please enter 'present' or 'absent' on lower ")
                    return


            self.attendance_records[self.day] = list(self.attendance_record_for_day.values())

            self.write_attendance_json(self.attendance_records)

            self.to_continue = input("Do you want to continue the attendance for next day ? \n")
            if self.to_continue == "yes".lower():
                self.day = self.tomorrow.strftime("%Y-%m-%d")

            else:
                break

    def edit_attendance_record(self):
        self.attendance_records = self.read_attendance_json()
        self.students.students_record = self.students.read_json()

        while True:
            self.to_edit = input("Please enter the date of attendance history: ")
            if self.to_edit in self.attendance_records.keys():
                self.name_of_student = input("Please enter the name of the student: ")
                if self.name_of_student in self.students.students_record.get("students", {}).values():
                    self.change_attendance = input("Please enter 'present' or 'absent': ")
                    for d in self.attendance_records[self.to_edit]:
                        if d["student_id"] == self.name_of_student:
                            d["present"] =  self.change_attendance.lower()
                    self.write_attendance_json(self.attendance_records)
                    break
                else:
                    print("Student not found. Please enter a valid student name.")
            else:
                print("Date not found. Please enter a valid date.")

    def show_student_attendance(self):
        date_input = input("Please enter the date of attendance date: ")
        self.attendance_records = self.read_attendance_json()
        for key, value in self.attendance_records.get(date_input, {}).items():
            print(f"For date {key}, attendance records: {value}")




def Student_attendance():
    attendance = Attendance()
    while True:
        user_input = input("Please Enter\n 1 . For Attendance \n 2 . To Edit Student Attendance \n 3 . To Show Attendance Record \n")
        if user_input == "1":
            attendance.attendance_record()
        elif user_input == "2":
            attendance.edit_attendance_record()
        elif user_input == "3":
            attendance.show_student_attendance()
        else:
            print("Input Error \n Please Enter 1 . For Attendance \n 2 . To Edit Student Attendance \n 3 . To Show Attendance Record")
            Student_attendance()

Student_attendance()