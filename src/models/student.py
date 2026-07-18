class Student:
    def __init__(self, student_id: int, name: str, age: int, email: str, mobile_number, spi: float, cgpa: float):
    
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.mobile_number = mobile_number
        self.spi = spi
        self.cgpa = cgpa

    def display_info(self):
        width = 42

        top_border = "┌" + "─" * width + "┐"
        middle_line = "├" + "─" * width + "┤"
        bottom_border = "└" + "─" * width + "┘"

        print(top_border)
        print(f"│{'STUDENT DETAILS':^{width}}│")
        print(middle_line)

        print(f"│  {'Student ID':<13}: {self.student_id:<24}│")
        print(f"│  {'Name':<13}: {self.name:<24}│")
        print(f"│  {'Age':<13}: {self.age:<24}│")
        print(f"│  {'Email':<13}: {self.email:<24}│")
        print(f"│  {'Contact':<13}: {self.mobile_number:<24}│")
        print(f"│  {'SPI':<13}: {self.spi:<24}│")
        print(f"│  {'CGPA':<13}: {self.cgpa:<24}│")

        print(bottom_border)

student1 = Student(101, "Alice Smith", 20, "alice@email.com", "+1234567890", 8.5, 8.7)
student1.display_info()