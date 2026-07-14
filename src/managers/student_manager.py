from models.student import Student
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
        name = input("Student Name: ")
        age = int(input("Age: "))
        email = input("Email ID: ")
        mobile = input("Contact No: ")
        spi = float(input("SPI: "))
        cgpa = float(input("CGPA: "))
        
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
                new_name = input("Student Name: ")
                new_age = int(input("Age: "))
                new_email = input("Email ID: ")
                new_mobile = input("Contact No: ")
                new_spi = float(input("SPI: "))
                new_cgpa = float(input("CGPA: "))

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