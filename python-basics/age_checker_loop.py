while True:
    age_input = input("Enter your age: ")

    try:
        age = int(age_input)

        if age >= 18:
            print("You are an adult")
        else:
            print("You are under 18.")

        break

    except ValueError:
        print("Invalid Input. Please enter a number.")

