from models.student import Student

class StudentManager:
    def __init__(self):
        self.students = []
        self.next_student_id = 1

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