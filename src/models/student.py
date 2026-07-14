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
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Contact: {self.mobile_number}")
        print(f"SPI: {self.spi}")
        print(f"CGPA: {self.cgpa}")
