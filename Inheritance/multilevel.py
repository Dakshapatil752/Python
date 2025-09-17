# Multilevel Inheritance Example: Student -> Exam -> Result

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display_student(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

class Exam(Student):
    def __init__(self, name, roll, subject, marks):
        super().__init__(name, roll)
        self.subject = subject
        self.marks = marks

    def display_exam(self):
        print(f"Subject: {self.subject}, Marks: {self.marks}")

class Result(Exam):
    def __init__(self, name, roll, subject, marks):
        super().__init__(name, roll, subject, marks)

    def display_result(self):
        self.display_student()
        self.display_exam()
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

# Example usage
r = Result("Alice", 101, "Math", 85)
r.display_result()