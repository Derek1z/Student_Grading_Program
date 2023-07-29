def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

def main():
    while True:
        try:
            marks = float(input("Enter the marks obtained by the student: "))
            if marks < 0 or marks > 100:
                raise ValueError("Invalid marks. Marks should be between 0 and 100.")
            
            grade = calculate_grade(marks)
            print(f"Grade: {grade}")
        
        except ValueError as error:
            print(f"Error: {error}")
        
        choice = input("Do you want to calculate grade for another student? (yes/no): ")
        if choice.lower() != "yes":
            break

if __name__ == "__main__":
    main()
