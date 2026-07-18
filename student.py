students = []

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")

        score1 = float(input("Score 1: "))
        while score1 < 0 or score1 > 20:
            print("Invalid score! Please enter a score between 0 and 20.")
            score1 = float(input("Score 1: "))

        score2 = float(input("Score 2: "))
        while score2 < 0 or score2 > 20:
            print("Invalid score! Please enter a score between 0 and 20.")
            score2 = float(input("Score 2: "))

        score3 = float(input("Score 3: "))
        while score3 < 0 or score3 > 20:
            print("Invalid score! Please enter a score between 0 and 20.")
            score3 = float(input("Score 3: "))

        average = round((score1 + score2 + score3) / 3, 2)

        if average >= 18:
            level = "Excellent ⭐"
            result = "Passed"
        elif average >= 15:
            level = "Good 👍"
            result = "Passed"
        elif average >= 10:
            level = "Average 🙂"
            result = "Passed"
        else:
            level = "Failed ❌"
            result = "Failed"

        students.append({
            "name": name,
            "score1": score1,
            "score2": score2,
            "score3": score3,
            "average": average,
            "result": result,
            "level": level
        })

        print("\nStudent added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\n===== Students =====")
            for student in students:
                print("---------------------------")
                print("Name:", student["name"])
                print("Score 1:", student["score1"])
                print("Score 2:", student["score2"])
                print("Score 3:", student["score3"])
                print("Average:", student["average"])
                print("Result:", student["result"])
                print("Level:", student["level"])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
