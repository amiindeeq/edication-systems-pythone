class Student:
    def __init__(self, student_id, name, age, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department

class Professor:
    def __init__(self, professor_id, name, department):
        self.professor_id = professor_id
        self.name = name
        self.department = department

class Course:
    def __init__(self, course_id, name, department):
        self.course_id = course_id
        self.name = name
        self.department = department
        self.professor = None
        self.students = []

    def assign_professor(self, professor):
        self.professor = professor

    def enroll_student(self, student):
        self.students.append(student)

    def generate_course_report(self):
        print(f"Course Report for {self.name}")
        print("-----------------------------------")
        print(f"Professor: {self.professor.name}  Department: {self.department}")
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}  Name: {student.name}  Age: {student.age}")
        print("-----------------------------------")

class Department:
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name

class College:
    def __init__(self):
        self.students = []
        self.professors = []
        self.courses = []
        self.departments = []

    def add_student(self, student_id, name, age, department_id):
        department = self.find_department_by_id(department_id)
        if department:
            student = Student(student_id, name, age, department)
            self.students.append(student)
        else:
            print("Invalid department ID")

    def add_professor(self, professor_id, name, department_id):
        department = self.find_department_by_id(department_id)
        if department:
            professor = Professor(professor_id, name, department)
            self.professors.append(professor)
        else:
            print("Invalid department ID")

    def create_course(self, course_id, name, department_id):
        department = self.find_department_by_id(department_id)
        if department:
            course = Course(course_id, name, department)
            self.courses.append(course)
        else:
            print("Invalid department ID")

    def assign_professor_to_course(self, professor_id, course_id):
        professor = self.find_professor_by_id(professor_id)
        course = self.find_course_by_id(course_id)
        if professor and course:
            course.assign_professor(professor)
        else:
            print("Invalid professor or course ID")

    def enroll_student_in_course(self, student_id, course_id):
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
        if student and course:
            course.enroll_student(student)
        else:
            print("Invalid student or course ID")

    def generate_course_report(self, course_id):
        course = self.find_course_by_id(course_id)
        if course:
            course.generate_course_report()
        else:
            print("Invalid course ID")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_professor_by_id(self, professor_id):
        for professor in self.professors:
            if professor.professor_id == professor_id:
                return professor
        return None

    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def find_department_by_id(self, department_id):
        for department in self.departments:
            if department.department_id == department_id:
                return department
        return None

# Example usage
college = College()

college.add_department(1, "Computer Science")
college.add_department(2, "Electrical Engineering")

college.add_professor(1, "John Smith", 1)
college.add_professor(2, "Jane Doe", 2)

college.add_student(101, "Alice", 20, 1)
college.add_student(102, "Bob", 21, 2)

college.create_course(201, "Python Programming", 1)
college.create_course(202, "Digital Circuits", 2)

college.assign_professor_to_course(1, 201)
college.assign_professor_to_course(2,I apologize for the incomplete response. Here's the complete code for the college management system project in Python:

```python
class Student:
    def __init__(self, student_id, name, age, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department

class Professor:
    def __init__(self, professor_id, name, department):
        self.professor_id = professor_id
        self.name = name
        self.department = department

class Course:
    def __init__(self, course_id, name, department):
        self.course_id = course_id
        self.name = name
        self.department = department
        self.professor = None
        self.students = []

    def assign_professor(self, professor):
        self.professor = professor

    def enroll_student(self, student):
        self.students.append(student)

    def generate_course_report(self):
        print(f"Course Report for {self.name}")
        print("-----------------------------------")
        print(f"Professor: {self.professor.name}  Department: {self.department}")
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}  Name: {student.name}  Age: {student.age}")
        print("-----------------------------------")

class Department:
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name

class College:
    def __init__(self):
        self.students = []
        self.professors = []
        self.courses = []
        self.departments = []

    def add_student(self, student_id, name, age, department_id):
        department = self.find_department_by_id(department_id)
        if department:
            student = Student(student_id, name, age, department)
            self.students.append(student)
        else:
            print("Invalid department ID")

    def add_professor(self, professor_id, name, department_id):
        department = self.find_department_by_id(department_id)
        if department:
            professor = Professor(professor_id, name, department)
            self.professors.append(professor)
        else:
            print("Invalid department ID")

    def create_course(self, course_id, name, department_id):
        department = self.find_department_by_id(department_id)
        if department:
            course = Course(course_id, name, department)
            self.courses.append(course)
        else:
            print("Invalid department ID")

    def assign_professor_to_course(self, professor_id, course_id):
        professor = self.find_professor_by_id(professor_id)
        course = self.find_course_by_id(course_id)
        if professor and course:
            course.assign_professor(professor)
        else:
            print("Invalid professor or course ID")

    def enroll_student_in_course(self, student_id, course_id):
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
        if student and course:
            course.enroll_student(student)
        else:
            print("Invalid student or course ID")

    def generate_course_report(self, course_id):
        course = self.find_course_by_id(course_id)
        if course:
            course.generate_course_report()
        else:
            print("Invalid course ID")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_professor_by_id(self, professor_id):
        for professor in self.professors:
            if professor.professor_id == professor_id:
                return professor
        return None

    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def find_department_by_id(self, department_id):
        for department in self.departments:
            if department.department_id == department_id:
                return department
        return None

# Example usage
college = College()

college.add_department(1, "Computer Science")
college.add_department(2, "Electrical Engineering")

college.add_professor(1, "John Smith", 1)
college.add_professor(2, "Jane Doe", 2)

college.add_student(101, "Alice", 20, 1)
college.add_student(102, "Bob", 21, 2)

college.create_course(201, "Python Programming", 1)
college.create_course(202, "Digital Circuits", 2)

college.assign_professor_to_course(1, 201)
college.assign_professor_to_course(2, 202)

college.enroll_student_in_course(101, 201)
college.enroll_student_in_course(102, 201)
college.enroll_student_in_course(102, 202)

college.generate_course_report(201)
college.generate_course_report(202)