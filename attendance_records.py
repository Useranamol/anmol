import json
import datetime
from student_record import Students
from file import MultiDictJSONHandler

multidictionary = MultiDictJSONHandler("attendance_records.json")

class Attendance:
    def __init__(self):
        self.students = Students()
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.attendance_records = self.read_attendance_json()

    # def write_attendance_json(self, data):
    #     try:
    #         with open('attendance_records.json', 'w') as file:
    #             json.dump(data, file, indent=2)
    #     except json.JSONDecodeError as e:
    #         print(f"Error encoding JSON: {e}")
    #
    # def read_attendance_json(self):
    #     try:
    #         with open('attendance_records.json', 'r') as file:
    #             data = json.load(file)
    #         return data
    #     except FileNotFoundError:
    #         print("Attendance file not found. Creating a new one.")
    #         self.write_attendance_json({})
    #         return {}
    #     except json.JSONDecodeError as e:
    #         print(f"Error decoding JSON: {e}")
    #         return {}

    def attendance_record(self):
        self.students.students_record = multidictionary.read_json()

        if not self.students.students_record:
            print("No student records found.")
            return

        self.date = datetime.datetime.now().strftime("%Y-%m-%d")

        if self.date in self.attendance_records:
            print(f"Attendance for {self.date} is already recorded.")
            return

        attendance_record_for_day = {}

        for key, student in self.students.students_record.get("students", {}).items():
            while True:
                registry = input(f"Is {student} present or absent? ").lower()
                if registry in ["present", "absent"]:
                    attendance_record_for_day[key] = {"student_id": student, "status": registry}
                    break
                else:
                    print("Please enter 'present' or 'absent'.")

        self.attendance_records[self.date] = attendance_record_for_day
        multidictionary.write_json(self.attendance_records)

        while True:
            to_continue = input("Do you want to continue the attendance for the next day? (yes/no) ").lower()
            if to_continue == "yes":
                self.date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                self.attendance_record()
            elif to_continue == "no":
                break
            else:
                print("Please enter 'yes' or 'no'.")

    def edit_attendance_record(self):

        self.students.students_record = multidictionary.read_json()

        while True:
            date_to_edit = input("Please enter the date of the attendance record to edit (YYYY-MM-DD): ")
            if date_to_edit in self.attendance_records:
                student_name = input("Please enter the name of the student: ")
                if student_name in self.students.students_record.get("students", {}).values():
                    while True:
                        new_status = input("Please enter 'present' or 'absent': ").lower()
                        if new_status in ["present", "absent"]:
                            for record in self.attendance_records[date_to_edit].values():
                                if record["student_id"] == student_name:
                                    record["status"] = new_status
                                    multidictionary.write_json(self.attendance_records)
                                    print("Attendance record updated.")
                                    return
                        else:
                            print("Please enter 'present' or 'absent'.")
                else:
                    print("Student not found. Please enter a valid student name.")

            else:
                print("Date not found. Please enter a valid date.")

    def show_student_attendance(self):
        date_input = input("Please enter the date of attendance record to view (YYYY-MM-DD): ")
        if date_input in self.attendance_records:
            print(f"Attendance records for {date_input}:")
            for student_id, record in self.attendance_records[date_input].items():
                print(f"Student ID: {student_id}, Status: {record['status']}")


        else:
            print("No attendance record found for the given date.")

    def show_history(self):
        self.students.students_record = multidictionary.read_json()
        self.user_student = input("Please enter the Student ID: ")


        for date, records in self.attendance_records.items():
            
            if self.user_student in records:

                student_attendance = records[self.user_student]
                student_status = student_attendance["status"]
                print(f"The attendance record of {self.user_student} on {date} is {student_status}")
            else:
                print(f"No attendance record found for {self.user_student} on {date}")




def student_attendance():
    attendance = Attendance()
    while True:

        user_input = input("Please Enter\n 1. For Attendance \n 2. To Edit Student Attendance \n 3. To Show Attendance Record \n 4. To Show History attendace of studdent \n 5. To exit \n")

        if user_input == "1":
            attendance.attendance_record()
        elif user_input == "2":
            attendance.edit_attendance_record()
        elif user_input == "3":
            attendance.show_student_attendance()
        elif user_input == "4":
            attendance.show_history()
        elif user_input == "5":
            break
        else:

            print("Input Error \n Please Enter the Given inputs \n")



