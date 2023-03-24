import csv
from students import Student
from courses import Course
from enrollments import Enrollment

def read_data():
    students = {}
    courses = {}
    enrollments = []

    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            id, name, email = row
            students[id] = Student(id, name, email)

    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            id, name, credit = row
            courses[id] = Course(id, name, credit)

    with open('enrollments.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            student_id, course_id, semester = row
            enrollment = Enrollment(student_id, course_id, semester)
            enrollments.append(enrollment)
            students[student_id].add_course(courses[course_id])
            courses[course_id].add_student(students[student_id])

    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            student_id, course_id, grade = row
            if grade: 
                students[student_id].add_grade(courses[course_id], grade)
                courses[course_id].add_grade(students[student_id], grade)

    return students, courses, enrollments