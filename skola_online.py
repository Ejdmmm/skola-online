# vyhledani konkretniho studenta a tridy na zaklade jejich ID
class Student:
    def __init__(self, id, first_name, last_name, grade):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.classroom = None
   
def __str__(self):
        return f"ID: {self.id}, Name: {self.first_name} {self.last_name}, Grade: {self.grade}, Classroom: {self.classroom}"
 ## vraci a prevadi na retezec, to co je napsane v {...}

class Classroom:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = [] ## vytvori pak
def add_students(self,student):
    self.students.append(student)
    student.classroom = self

def remove_student(self,student):
    self.students.remove(student)
    student.classroom = None
def __str__(self):
    return f"ID: {self.id}, Name: {self.name}, Students: {len(self.students)}" # jak se prevede na retezec (vrati), id tridy, jmeno apod

class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name= name
        self.grades = {} ## doplni se pak
def set_grade(self,student, grade):
    self.grades[student] = grade

def get_total_grade(self, student):
    return self.grades.get(student)
def __str__(self):
    return f"ID: {self.id}, Name: {self.name}"

def create_student():
    id = input("Enter student ID:")
    f_name = input("Enter first name:")
    l_name = input("Enter last name:")
    grade = input("Enter student's grade: ")
    return Student(id, f_name, l_name, grade)
    ## trida
def create_classroom():
    id = input("Enter classroom ID: ")
    name = input("Enter classroom name: ")
    return Classroom(id, name)
    
   ## vytvoreni predmetu 
def create_subject(): 
    id = input("Enter subject ID: ")
    name = input("Enter subject name: ")
    return Subject(id, name)
    ## trida
def set_student_classroom(students, classrooms):
    student_id = input("Enter student ID: ") 
    classroom_id = input("Enter classroom ID: ")
    student = next((s for s in students if s.id == student_id), None) ## vyhledává první prvek v zadaném seznamu, který splňuje zadanou podmínku
    classroom = next((c for c in classrooms if c.id == classroom_id), None) ## to same, hledaji se konretni student a trida na zaklade jejich id
    if student and classroom:
        classroom.add_student(student)
        print("Student assigned to classroom successfully.") 
    else:
        print("Student or classroom not found.")
    ## celkove znamky
def print_total_grade(subjects, students):
    student_id = input("Enter ID: ")
    subject_id = input("Enter subject ID: ")
    student = next((s for s in students if s.id == student_id), None)
    subject = next((s for s in subjects if s.id == subject_id), None)
    if student and subject:
        grade = subject.get_total_grade(student) ## total znamky
        if grade:
            print(f"Total grade for student {student_id} in subject {subject_id} is {grade}.") 
        else:
            print(f"No grade found for student {student_id} in subject {subject_id}.")
    else:
        print("Student or subject not found.")
        
        
def main():
    students = []
    classrooms = []
    subjects = []
    
    while True:
        print("\nMain Menu:")
        print("1. Create student")
        print("2. Create classroom")
        print("3. Create subject")
        print("4. Set student classroom")
        print("5. Print total grade")
        print("0. Exit")
        
        option = input("Select an option: ")
        
        if option == "1":
            student = create_student()
            students.append(student)
            print("Student created successfully.")
        elif option == "2":
            classroom = create_classroom()
            classrooms.append(classroom)
            print("Classroom created successfully.")
        elif option == "3":
            subject = create_subject()
            subjects.append(subject)
            print("Subject created successfully.")
        elif option == "4":
            set_student_classroom(students, classrooms)
        elif option == "5":
            print_total_grade(subjects, students)
        elif option == "0":
            print("Exiting")
            break
        else:
            print("Invalid option.")
            
if __name__ == "__main__":
    main() ## slouzi ke spusteni, ale jen kdyz to je v hlavnim souboru


 
