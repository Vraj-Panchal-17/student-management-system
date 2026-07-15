def validate_name():
    while True:
        name = input("Name: ").strip()

        if name == "":
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name should contain only letters and spaces.")
            continue

        return name
        
def validate_age():
    while True:
        try:
            age = int(input("Age: "))
            
            if age < 1 or age > 100:
                print("Please Enter Valid Age.")
                continue     

        except ValueError:
            print("Age Must Be an Integer")
            continue    

        return age 
            
def validate_email():
    while True:
        try:
            email = input("Email: ").strip()

            # Must contain exactly one '@'
            if email.count("@") != 1:
                print("Please Enter Valid Email.")
                continue

            local_part, domain_part = email.split("@")

            # Basic checks: non-empty parts
            if not local_part or not domain_part:
                print("Please Enter Valid Email.")
                continue

            # Avoid whitespace and require a dot in the domain (basic heuristic)
            if " " in local_part or " " in domain_part:
                print("Please Enter Valid Email.")
                continue

            if "." not in domain_part:
                print("Please Enter Valid Email.")
                continue

        except ValueError:
            print("Please Enter Valid Email.")
            continue

        return email
      
def validate_mobile():
    while True:
        mobile_number = input("Mobile Number: ")

        if len(mobile_number) == 10 and mobile_number.isdigit():
            return mobile_number
        
        else:
            print("Please Enter Valid 10-digit Mobile Number.")

def validate_spi():
    while True:
        try:
            spi = float(input("SPI: "))

            if spi > 10 or spi < 0:
                print("SPI Must Be Between 0 and 10.")
                continue
            
            return spi
        
        except ValueError:
            print("Please Enter a Valid SPI.")

def validate_cgpa():
    while True:
        try:
            cgpa = float(input("CGPA: "))

            if cgpa > 10 or cgpa < 0:
                print("CGPA Must Be Between 0 and 10.")
                continue
            
            return cgpa
        
        except ValueError:
            print("Please enter a valid number.")
        