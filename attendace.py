def show_history(self):
    self.students.students_record = self.students.read_json()
    self.user_student = input("Please enter the Student Id: ")

    if self.date in self.attendance_records:
        for x in self.attendance_records:
            student_attendance = self.attendance_records[x]
        if self.user_student in student_attendance:
            attendance_status = student_attendance[self.user_student]["status"]
            print(f"Attendance status for {self.user_student[]} on {self.date}: {attendance_status}")
        else:
            print(f"No attendance record found for {self.user_student} on {self.date}.")
    else:
        print(f"No attendance records available for {self.date}.")