from student_record import Students
import json
import datetime

class Attendance:
    def __init__(self):
        self.students = Students()
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.attendace_records ={}

    def write_attendace_json(self, data):
        try:
            with open('attendace_records.json', 'w') as file:
                json.dump(data, file, indent=2)
        except json.JSONDecodeError as e:
            print(f"Error encoding JSON: {e}")

    def read_attendance_json(self):
        try:
            with open('attendace_records.json', 'r') as file:
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

        self.attendace_records = self.read_attendance_json()
        self.day = datetime.datetime.now().strftime("%Y-%m_%d")

        while True:

            self.tommorow = datetime.datetime.now() + datetime.timedelta(days=1)

            if self.attendace_records is None:
                self.attendace_records = {}

            if self.day in self.attendace_records:
                print(f" Attendace of {self.day} is already recorded .")
                break



            self.attendace_record_for_day = {}



            for key in self.students.students_record.get("students" , {}).keys():
                self.registry = input(f" Is {self.students.students_record["students"][key]}  Present or absent ? \n")
                if self.registry == "present".lower():
                    self.attendace_record_for_day[key] = { "student_id "  : self.students.students_record["students"][key] , "present" : self.registry}
                else:
                    print("please enter 'present' or 'absent' on lower ")
                    return


            self.attendace_records[self.day] = list(self.attendace_record_for_day.values())

            self.write_attendace_json(self.attendace_records)

            self.to_continue = input("Do you want to continue the attendace for next day ? \n")
            if self.to_continue == "yes".lower():
                self.day = self.tommorow.strftime("%Y-%m-%d")

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
                    self.attendace_records[self.to_edit] = {
                        "student_id": self.name_of_student,
                        "present": self.change_attendance.lower(),

                    }
                    self.write_attendace_json(self.attendace_records)
                    break
                else:
                    print("Student not found. Please enter a valid student name.")
            else:
                print("Date not found. Please enter a valid date.")

    def show_student_attendance(self, day):
        self.attendance_records = self.read_attendance_json()
        for key, value in self.attendance_records.get(day, {}).items():
            print(f"For date {key}, attendance records: {value}")


attendace = Attendance()

def Student_attendace():
    while True:
        user_input = input("Please Enter 1 . For Attendace \n 2 . To Edit Student Attendace \n 3 . To Show Attendace Record \n")
        if user_input == "1":
            attendace.attendance_records()
        elif user_input == "2":
            attendace.edit_attendance_record()
        elif user_input == "3":
            attendace.show_student_attendance()
        else:
            print("Input Error \n Please Enter 1 . For Attendace \n 2 . To Edit Student Attendace \n 3 . To Show Attendace Record")
            Student_attendace()