# Practical 4 – Task 1: Extracting Words from Text File

## Objective
Develop a Python program that reads a text file and prints words of specified lengths (e.g., three, four, five letters).

## Instructions
- Implement the function extract_words(filename, lengths) in `student_code_4_1.py`.
- The function should:
  - Open the file and read its contents.
  - Split the text into words.
  - Print words whose lengths match any value in the list `lengths`.

## Example
Suppose `testfile.txt` contains:
`cat dog elephant fox bat`

Calling:
`extract_words("testfile.txt", [3])`

Output:
```
cat
dog
fox
bat
```

## Transition from C to Python
In C, you would use file I/O functions like fopen, fscanf, and strlen.  
In Python, file handling is simpler:
```python
with open("filename.txt", "r") as f:
    text = f.read()
words = text.split()
```

## How to check your solution
1. Save your solution in `student_code_4_1`.py.
2. Create a sample text file with words.
3. Call `extract_words("filename.txt", [3,4,5])` and verify the output.

## How to Run Autograder
1. Save your solution in `student_code_4_1.py`.
2. Run:
   `python autograder_4_1.py`
   or
   `python3 autograder_4_1.py`
3. Check your score, feedback, and token.

## Notes
- Handle FileNotFoundError gracefully.
- Do not change function names.
- Submit your token and screenshot in the Excel sheet.