class Student:
    def __init__(self,id,first_name, last_name, grade):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.classroom = None
    def __str__(self): ## prevadeni na string, pri volani metody, vraci parametry
        return f"ID:{self.id},{self.first_name},{self.last_name}, 


