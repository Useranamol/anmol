def edit_attendance_record(self):
    self.attendance_records = self.read_attendance_json()

    while True:
        self.to_edit = input("Please enter the date of attendance history: ")
        if self.to_edit in self.attendance_records.keys():
            self.student = input("please enter the name of student. \n")
            if self.student in self.students.students_record.get("students", {}).keys():
                for key in self.students.students_record.get("students", {}).keys():
                    self.change_attendance = input("Please enter 'present' or 'absent': ")
                    if self.change_attendance == "present" or "absent":
                        self.attendance_record_for_day[self.to_edit] = {
                            "student_id": self.students.students_record["students"][key],
                            "present": self.change_attendance.lower()}
                    else:
                        print("please enter 'present' or 'absent' .")

            break
        else:
            print("Date not found. Please enter a valid date.")