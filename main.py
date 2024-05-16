class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        if self.grades:
            sumOfGrades = sum(self.grades)
            return round(sumOfGrades/len(self.grades), 2)
        else:
            return 0

    def __repr__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGrades: {self.grades}\nAverage: {self.average()}"


class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grades):
        new_student = Student(name, age, grades)
        self.students.append(new_student)

    def display_all_students(self):
        for student in self.students:
            print(student)
            print("")

def main():
    student_db = StudentDatabase()


    student_db.add_student("Alice", 20, [90, 85, 92])
    student_db.add_student("Bob", 22, [78, 82, 88])
    student_db.add_student("Charlie", 19, [95, 90, 93])

    print("All students in the database:")
    student_db.display_all_students()

    print("\nAdd a new student David:")
    student_db.add_student("David", 21, [83, 76, 89])
    student_db.display_all_students()


main()