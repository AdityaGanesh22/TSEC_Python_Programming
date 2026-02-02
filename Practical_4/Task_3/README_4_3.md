# Practical 4 – Task 3: Sorting City Names from File

## Objective
Develop a Python program that reads a file containing city names (one per line),
sorts them alphabetically, and writes them into another file.

## Instructions
- Implement the function `sort_cities(input_file, output_file)` in `student_code_4_3.py`.
- The function should:
  - Read city names from `input_file`.
  - Sort them alphabetically.
  - Write them line by line into `output_file`.

## Example
Suppose `sample_cities.txt` contains:
```
Mumbai
Delhi
Chennai
Kolkata
Bengaluru
Hyderabad
```

Calling:
`sort_cities("sample_cities.txt", "sorted_cities.txt")`

Output file `sorted_cities.txt` will contain:
```
Bengaluru
Chennai
Delhi
Hyderabad
Kolkata
Mumbai
```

## Transition from C to Python
In C, you would use arrays and sorting algorithms like bubble sort or quicksort.  
In Python, you can simply use the built-in `sort()` method.

## How to check your solution
1. Save your solution in `student_code_4_3.py`.
2. Create a sample file with city names.
3. Call `sort_cities("sample_cities.txt", "sorted_cities.txt")` and verify the output.

## How to Run Autograder
1. Save your solution in `student_code_4_3.py`.
2. Run:
   `python autograder_4_3.py`
   or
   `python3 autograder_4_3.py`
3. Check your score, feedback, and token.

## Notes
- Handle `FileNotFoundError` gracefully.
- Do not change function names.
- Submit your token and screenshot in the Excel sheet.