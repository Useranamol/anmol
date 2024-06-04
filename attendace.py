from main import Registry
from datetime import datetime , timedelta
import json

registry = Registry()
a = registry.__init__()
b = registry.read_json()
c = registry.write_json()


class Attendace():
    registry = Registry()
    a = registry.__init__()
    b = registry.read_json()

    def write_attendace_file(self , data):
        try:
            with open('attendance.json', 'w') as file:
                json.dump(data, file, indent=2)
        except json.JSONDecodeError as e:
            print(f"Error encoding JSON: {e}")

    def read_attendace_file(self ):
        try:
            with open('attendance.json', 'r') as file:
                data = json.load(file)
            return data

        except json.JSONDecodeError as e:
            return None

    def attendace(self):
        self.a = self.b
        print(f"Error decoding JSON: {e}")

        if self.a is None:
            print("No record is found !")
            return

        self.attendace_record = self.read_attendace_file()
        self.day =  datetime.now().strftime("%Y-%m-%d")

        while True:
            self.tommorow = datetime.now() + timedelta(days=1)

            if self.day in self.attendace_record:
                print(f" records of day {self.day} is already recorded !")
                break

            if self.attendace_record is None:
                self.attendace_record = {}

            self.attendace_for_day = {}

            for key in self.a.keys():
                self.input = input(f" is {self.a[key]} is present or absent \n ").lower()
                if self.input == "present" or self.inputp == "absent":
                    self.attendace_for_day[key] = { "student_id" : a[key] , "present" : self.input}
                else:
                    print("Please type 'present' or 'absent'.")
                    return
            self.attendance_records[self.day] = list(self.attendance_for_day.values())

            self.write_attendancejson(self.a)

            self.to_continue = input("Do you want to continue for the next day (yes/no)?: ").lower()
            if self.to_continue == "yes":
                self.day = self.tomorrow.strftime("%Y-%m-%d")
            else:
                break





