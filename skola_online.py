class Student:
    def __init__(self, student_id, first_name, last_name, grade):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.classroom = None

    def __str__(self):
        return f"ID: {self.id}, Name: {self.first_name} {self.last_name}, Grade: {self.grade}, Classroom: {self.classroom}"

class Classroom:
    def __init__(self, class_id, name):
        self.id = class_id
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        student.classroom = self

    def remove_student(self, student):
        self.students.remove(student)
        student.classroom = None

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Students: {len(self.students)}"

class Subject:
    def __init__(self, subject_id, name):
        self.id = subject_id
        self.name = name
        self.grades = {}

    def set_grade(self, student, grade):
        self.grades[student] = grade

    def get_total_grade(self, student):
        return self.grades.get(student)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

def create_student():
    id = input("Enter student ID: ")
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    grade = float(input("Enter student's grade: "))
    return Student(id, f_name, l_name, grade)

def create_classroom():
    id = input("Enter classroom ID: ")
    name = input("Enter classroom name: ")
    return Classroom(id, name)

def create_subject():
    id = input("Enter subject ID: ")
    name = input("Enter subject name: ")
    return Subject(id, name)

def set_student_classroom(students, classrooms):
    student_id = input("Enter student ID: ")
    classroom_id = input("Enter classroom ID: ")
    student = next((s for s in students if s.id == student_id), None)
    classroom = next((c for c in classrooms if c.id == classroom_id), None)
    if student and classroom:
        classroom.add_student(student)
        print("Student assigned to classroom successfully.")
    else:
        print("Student or classroom not found.")

def print_total_grade(subjects, students):
    student_id = input("Enter student ID: ")
    subject_id = input("Enter subject ID: ")
    student = next((s for s in students if s.id == student_id), None)
    subject = next((s for s in subjects if s.id == subject_id), None)
    if student and subject:
        grade = subject.get_total_grade(student)
        if grade is not None:
            print(f"Total grade for student {student_id} in subject {subject_id} is {grade}.")
        else:
            print(f"No grade found for student {student_id} in subject {subject_id}.")
    else:
        print("student or subject not found.")

def main():
    students = []
    classrooms = []
    subjects = []

    options_mapping = {
        "1": (create_student, students, "Student created successfully."),
        "2": (create_classroom, classrooms, "Classroom created successfully."),
        "3": (create_subject, subjects, "Subject created successfully."),
        "4": (set_student_classroom, (students, classrooms), "Student assigned to classroom successfully."),
        "5": (print_total_grade, (subjects, students), None),
        "0": (exit, [], "Exiting")
    }

    while True:
        print("Main Menu:")
        print("1. Create student")
        print("2. Create classroom")
        print("3. Create subject")
        print("4. Set student classroom")
        print("5. Print total grade")
        print("0. Exit")

        option = input("Enter option: ")

        if option in options_mapping:
            func, args, success_message = options_mapping[option]
            result = func(*args)
            if success_message and result is not None:
                print(success_message)
            elif result is None:
                print("Operation executed successfully.")
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()