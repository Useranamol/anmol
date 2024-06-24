class Menu():

    def __init__(self):
        self.welcome = input("Please Enter \n 1. For  Student Record \n 2. For Attendace record \n 3. For Search Student \n")
        if self.welcome == 1 :
            self.Student_record()
            pass
        elif self.welcome == 2:
            self.Attendace_record()
            pass
        elif self.welcome == 3:
            self.Search_student()
            pass
        else:
            print("please Enter 1 or 2 or 3 \n Error")
            self.__init__()

menu = Menu()