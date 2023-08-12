class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

class Subject:
    def __init__(self, subject_id, name):
        self.subject_id = subject_id
        self.name = name

class Class:
    def __init__(self, class_id, name, teacher):
        self.class_id = class_id
        self.name = name
        self.teacher = teacher
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def generate_class_report(self):
        print(f"Class Report for {self.name}")
        print("-----------------------------------")
        print(f"Teacher: {self.teacher.name}  Subject: {self.teacher.subject}")
        print("Students:")
        for student in self.students:
            print(f"ID: {student.student_id}  Name: {student.name}  Age: {student.age}  Grade: {student.grade}")
        print("-----------------------------------")

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.subjects = []
        self.classes = []

    def add_student(self, student_id, name, age, grade):
        student = Student(student_id, name, age, grade)
        self.students.append(student)

    def add_teacher(self, teacher_id, name, subject_id):
        subject = self.find_subject_by_id(subject_id)
        if subject:
            teacher = Teacher(teacher_id, name, subject)
            self.teachers.append(teacher)
        else:
            print("Invalid subject ID")

    def add_subject(self, subject_id, name):
        subject = Subject(subject_id, name)
        self.subjects.append(subject)

    def create_class(self, class_id, name, teacher_id):
        teacher = self.find_teacher_by_id(teacher_id)
        if teacher:
            class_obj = Class(class_id, name, teacher)
            self.classes.append(class_obj)
        else:
            print("Invalid teacher ID")

    def enroll_student_in_class(self, student_id, class_id):
        student = self.find_student_by_id(student_id)
        class_obj = self.find_class_by_id(class_id)

        if student and class_obj:
            class_obj.enroll_student(student)
        else:
            print("Invalid student or class ID")

    def generate_class_report(self, class_id):
        class_obj = self.find_class_by_id(class_id)
        if class_obj:
            class_obj.generate_class_report()
        else:
            print("Invalid class ID")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_teacher_by_id(self, teacher_id):
        for teacher in self.teachers:
            if teacher.teacher_id == teacher_id:
                return teacher
        return None

    def find_subject_by_id(self, subject_id):
        for subject in self.subjects:
            if subject.subject_id == subject_id:
                return subject
        return None

    def find_class_by_id(self, class_id):
        for class_obj in self.classes:
            if class_obj.class_id == class_id:
                return class_obj
        return None

# Example usage
school = School()

school.add_subject(1, "Mathematics")
school.add_subject(2, "Science")

school.add_teacher(1, "John Smith", 1)
school.add_teacher(2, "Jane Doe", 2)

school.add_student(101, "Alice", 15, 9)
school.add_student(102, "Bob", 14, 8)

school.create_class(1, "Class A", 1)
school.create_class(2, "Class B", 2)

school.enroll_student_in_class(101, 1)
school.enroll_student_in_class(102, 1)
school.enroll_student_in_class(102, 2)

school.generate_class_report(1)
school.generate_class_report(2)