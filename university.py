class Student:
    def __init__(self, student_id, name, age, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class Enrollment:
    def __init__(self, student, course, grade=None):
        self.student = student
        self.course = course
        self.grade = grade

class University:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []

    def add_student(self, student_id, name, age, email):
        student = Student(student_id, name, age, email)
        self.students.append(student)

    def add_course(self, course_id, name):
        course = Course(course_id, name)
        self.courses.append(course)

    def enroll_student(self, student_id, course_id):
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)

        if student and course:
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)
            print(f"Student {student.name} enrolled in course {course.name}")
        else:
            print("Invalid student or course ID")

    def record_grade(self, student_id, course_id, grade):
        enrollment = self.find_enrollment(student_id, course_id)

        if enrollment:
            enrollment.grade = grade
            print(f"Grade recorded for student {enrollment.student.name} in course {enrollment.course.name}")
        else:
            print("No enrollment found for the given student and course ID")

    def generate_student_report(self, student_id):
        student = self.find_student_by_id(student_id)

        if student:
            print(f"Report for student {student.name}")
            print("-----------------------------------")
            for enrollment in self.enrollments:
                if enrollment.student == student:
                    course_name = enrollment.course.name
                    grade = enrollment.grade if enrollment.grade else "N/A"
                    print(f"Course: {course_name}, Grade: {grade}")
            print("-----------------------------------")
        else:
            print("Invalid student ID")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def find_enrollment(self, student_id, course_id):
        for enrollment in self.enrollments:
            if enrollment.student.student_id == student_id and enrollment.course.course_id == course_id:
                return enrollment
        return None

# Example usage
university = University()

university.add_student(101, "John Smith", 20, "john@example.com")
university.add_student(102, "Jane Doe", 21, "jane@example.com")

university.add_course(201, "Mathematics")
university.add_course(202, "Physics")

university.enroll_student(101, 201)
university.enroll_student(101, 202)
university.enroll_student(102, 202)

university.record_grade(101, 201, 85)
university.record_grade(101, 202, 90)

university.generate_student_report(101)
university.generate_student_report(102)