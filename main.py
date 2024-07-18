from student_record import Records
from attendance_records import student_attendance
class Menu:
    def __init__(self):
        while True:
            self.welcome = input("Please Enter:\n1. Student Record\n2. Attendance Record\n")
            if self.welcome == "1":
                Records()
                break
            elif self.welcome == "2":
                student_attendance()
                break

            else:
                print("Please enter 1 or 2. Try again.")
                self.__init_subclass__()

menu = Menu()
