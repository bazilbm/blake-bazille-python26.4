# Section 1: Variables and Types

name = "Blake"
age = 48
height = 5.11
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# Section 2: User Input and Math

name = input("Please enter your name: ")
Year_of_birth = input("Please enter your year of birth: ")
conv_age = int(Year_of_birth)
year_current = 2026
age = year_current - conv_age
print(f"Hi, {name}! You are approximately {age} years old.")

# Section 3: Type Conversion and f-strings

first = float(input("Enter your first number: "))
second = float(input("Enter your second number: "))
product = first * second
print(f"{first} * {second} = {product}")

# Section 4: Formatted Receipt

item = "Cherry Snocone"
price = 4.00
quantity = 2
total= price * quantity
print()
print()
print("==============================")
print("           Receipt            ")
print("==============================")
print()
print(f"Item:       {item}")
print(f"Price:      ${price:.2f}")
print(f"Quantity:   {quantity}")
print()
print("------------------------------")
print(f"Total:      ${total:.2f}")
print("------------------------------")
print()

# Section 5: Mini-Project - Profile Card

name = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("What is your hobby? ")
fun_fact = input("What is one fun fact about you? ")
birthyear = input("What year were you born? ")
conv_age = int(birthyear)
year_current = 2026
age = year_current - conv_age
print()
print("╔════════════════════════════╗")
print()
print(f"   Profile:  {name}")
print()
print("╚════════════════════════════╝")
print()
print(f"Hometown:   {hometown}")
print(f"Hobby:      {hobby}")
print(f"Fun_Fact:   {fun_fact}")
print(f"Age:        {age}")
print()
