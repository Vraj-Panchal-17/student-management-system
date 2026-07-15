from models.student import Student
from utils.validators import (
    validate_age,
    validate_cgpa,
    validate_email,
    validate_mobile,
    validate_name,
    validate_spi,
)
import json

class StudentManager:
    def __init__(self):
        self.students = []
        self.next_student_id = 1

    def load_students(self):
        with open("data/students.json", "r") as file:
            data = json.load(file)
            
            for student_data in data:

                student = Student(student_data["student_id"], student_data["name"],student_data["age"],student_data["email"],student_data["mobile_number"],student_data["spi"],student_data["cgpa"])

                if student.student_id >= self.next_student_id:
                    self.next_student_id = student.student_id + 1
                self.students.append(student)


    def save_students(self):
        student_data = []

        for student in self.students:
            student_dict = {
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "email": student.email,
                "mobile_number": student.mobile_number,
                "spi": student.spi,
                "cgpa": student.cgpa
            }

            student_data.append(student_dict)

        with open("data/students.json", "w") as file:
            json.dump(student_data, file, indent=4)

    def add_student(self):
        name = validate_name()
        age = validate_age()
        email = validate_email()
        mobile = validate_mobile()
        spi = validate_spi()
        cgpa = validate_cgpa()
        
        student = Student(self.next_student_id, name, age, email, mobile, spi, cgpa)
        self.students.append(student)
        self.next_student_id += 1
        self.save_students()
        print("✅ Student added successfully!")

    def view_students(self):
        if not self.students:
            print("There is no student added yet.")
        else:
            for student in self.students:
                student.display_info()

    def delete_student(self):
        if not self.students:
            print("There is no student added yet.")
            return

        self.view_students()

        user = int(input("Enter ID number: "))

        for idx, student in enumerate(self.students):
            if student.student_id == user:
                self.students.pop(idx)
                self.save_students()
                print("✅ Student information deleted successfully.")
                return

        print("❌ Student ID not found.")
            


    def update_student(self):
        if not self.students:
            print("There is no student added yet.")
            return
        
        self.view_students()

        user = int(input("Student ID: "))

        for idx, student in enumerate(self.students):
            if student.student_id == user:
                new_name = validate_name()
                new_age = validate_age()
                new_email = validate_email()
                new_mobile = validate_mobile()
                new_spi = validate_spi()
                new_cgpa = validate_cgpa()

                student.name = new_name
                student.age = new_age
                student.email = new_email
                student.mobile = new_mobile
                student.spi = new_spi
                student.cgpa = new_cgpa

                self.save_students()
                print("✅ Student updated successfully.")
                return
            
            print("❌ Student ID not found.")

    def search_student(self):
        if not self.students:
            print("There is no student added yet.")
            return
        
        user = int(input("Enter Studnt ID: "))

        for student in self.students:
            if user == student.student_id:
                student.display_info()
                return
        
        print("❌ Student ID not found.")