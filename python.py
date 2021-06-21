import datetime


class Course:

    def __init__(self, **kwargs) -> None:
        self.course = {

        }

        for key, value in kwargs.items():
            self.course[key] = [value]

    def courses(self):
        print(self.course)


class Student(Course):
    def __init__(self, lname, fname, adminNo, **kwargs):
        self.lname = lname
        self.fname = fname
        dob = datetime.datetime(2000, 2, 15)
        self.dob = dob
        self.adminNo = adminNo
        super().__init__(**kwargs)

    def studentDetails(self):

        print("Hello there!! My name is " +
              self.lname + " " + self.fname + ".")
        print("My student id is " + self.adminNo + ". :)")

    def courseDetails(self):
        print("Hello there, I am enrolled in the following courses: " +
              super().courses())


Mensah = Student("Ebenezer", "MEns", "234",
                 CSCD31="Intro CompScience", CSCD21="Data Structures and Algo")

Mensah.studentDetails()

Mensah.courseDetails()
