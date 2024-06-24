from student_record import Records

class Menu:
    def __init__(self):
        while True:
            self.welcome = input("Please Enter:\n1. Student Record\n2. Attendance Record\n3. Search Student\n")
            if self.welcome == "1":
                Records()
                break
            elif self.welcome == "2":
                self.Attendance_record()
                pass
            elif self.welcome == "3":
                self.Search_student()
                pass
            else:
                print("Please enter 1, 2, or 3. Try again.")

menu = Menu()
