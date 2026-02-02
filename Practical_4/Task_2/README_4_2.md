# Practical 4 – Task 2: Finding Closest Points in 3D Coordinates from CSV

## Objective
Develop a Python program that reads a CSV file containing 3D coordinates of points and finds the two closest points.

## Instructions
- Implement the function `find_closest_points(filename)` in `student_code_4_2.py`.
- The function should:
  - Read the CSV file.
  - Extract coordinates (x, y, z).
  - Compute Euclidean distances between all pairs of points.
  - Print the two closest points and their distance.

## Example
Suppose sample_points.csv contains:
```txt
1.0,2.0,3.0
4.0,5.0,6.0
1.1,2.1,3.1
7.0,8.0,9.0
```

Calling:
`find_closest_points("sample_points.csv")`

Output:
`Closest points are (1.0, 2.0, 3.0) and (1.1, 2.1, 3.1) with distance 0.173`

## Transition from C to Python
In C, you would use arrays and nested loops to compute distances.  
In Python, you can use lists and the math library for square root.

## How to check your solution
1. Save your solution in `student_code_4_2.py`.
2. Create a sample CSV file with coordinates.
3. Call `find_closest_points("sample_points.csv")` and verify the output.

## How to Run Autograder
1. Save your solution in `student_code_4_2.py`.
2. Run:
   `python autograder_4_2.py`
   or
   `python3 autograder_4_2.py`
3. Check your score, feedback, and token.

## Notes
- Handle `FileNotFoundError` gracefully.
- Do not change function names.
- Submit your token and screenshot in the Excel sheet.