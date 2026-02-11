# Rno: <student roll number>
# student_code_5_5.py

# Scientific Debugging Techniques
# Provide a Python program with multiple logic and runtime errors.
# Students should apply scientific debugging techniques (like binary search debugging)
# to identify and resolve the issues methodically.

def buggy_program():
    print("Starting buggy program...")

    # Intentional errors:
    # 1. Using a variable before assignment
    total = count + 10   # Error: 'count' not defined

    # 2. Division by zero
    divisor = 0
    quotient = 100 / divisor   # Error: division by zero

    # 3. Logical error: incorrect loop condition
    numbers = [1, 2, 3, 4, 5]
    for i in range(len(numbers) + 5):   # Error: goes out of range
        print("Number:", numbers[i])

    # 4. Type error: adding string and integer
    name = "Student"
    age = 20
    message = name + age   # Error: cannot add str and int

    print("Program completed.")