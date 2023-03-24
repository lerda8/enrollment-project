import csv
from students import Student
from courses import Course
from enrollments import Enrollment

# Load students from CSV file
students = {}
with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    for row in reader:
        id, name, email = row
        students[id] = Student(id, name, email)

# Load courses from CSV file
courses = {}
with open('courses.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    for row in reader:
        id, name, credit = row
        courses[id] = Course(id, name, credit)

# Load enrollments from CSV file
enrollments = []
with open('enrollments.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    for row in reader:
        student_id, course_id, semester, grade = row
        enrollment = Enrollment(student_id, course_id, semester, grade)
        enrollments.append(enrollment)

def add_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    students[id] = Student(id, name, email)
    print("Student added successfully.")

def enroll_student():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    semester = input("Enter semester: ")
    enrollment = Enrollment(student_id, course_id, semester)
    enrollments.append(enrollment)
    print("Student enrolled successfully.")

def grade_student():
    student_id = input("Enter student ID: ")
    course_id = input("Enter course ID: ")
    for enrollment in enrollments:
        if enrollment.student_id == student_id and enrollment.course_id == course_id:
            grade = input("Enter grade: ")
            enrollment.grade = grade
            print("Grade added successfully.")
            return
    print("Error: student/course not found or not enrolled.")

def display_student():
    student_id = input("Enter student ID: ")
    if student_id in students:
        student = students[student_id]
        print(f"Name: {student.name}")
        print(f"Email: {student.email}")
        print("Enrollments:")
        for enrollment in enrollments:
            if enrollment.student_id == student_id:
                course = courses[enrollment.course_id]
                grade = enrollment.grade or "N/A"
                print(f"- {course.name} ({course.credit} credits), semester {enrollment.semester}, grade: {grade}")
        return
    print("Error: student not found.")

def display_course():
    course_id = input("Enter course ID: ")
    if course_id in courses:
        course = courses[course_id]
        print(f"Name: {course.name}")
        print(f"Credit: {course.credit}")
        print("Enrollments:")
        for enrollment in enrollments:
            if enrollment.course_id == course_id:
                student = students[enrollment.student_id]
                grade = enrollment.grade or "N/A"
                print(f"- {student.name} ({student.email}), semester {enrollment.semester}, grade: {grade}")
        return
    print("Error: course not found.")

# Menu loop
while True:
    print("MENU")
    print("1. Add Student")
    print("2. Enroll Student to Course")
    print("3. Grade Student")
    print("4. Display Student")
    print("5. Display Course")
    print("0. EXIT")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        enroll_student()
    elif choice == "3":
        grade_student()
    elif choice == "4":
        display_student()
    elif choice == "5":
        display_course()
    elif choice == "0":
        break
    else:
        print("Error: invalid choice.")