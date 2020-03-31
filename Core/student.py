class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_role(self):
        print("GPA"+self.gpa)
        if (str(self.gpa).isdigit() == False):
            print("Value is not digit")
        else:
            if (self.gpa > 3.5):
                return True
            else:
                return False

class Teacher(Student):
    def __init__(self,name,major, gpa, is_on_probation, subject = 'Teachsub'):
        super().__init__(name, major, gpa, is_on_probation)
        self.subject = subject

    def has_class(self):
        print(str(self)+"has_class function called")


