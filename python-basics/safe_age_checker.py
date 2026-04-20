age_input = input("Enter your age: ")

try:
    age = int(age_input)

    if age >= 18:
        print("You're an adult")
    else:
        print("You are under 18.")

except ValueError:
        print("Invalid Input. Please enter a number.")

