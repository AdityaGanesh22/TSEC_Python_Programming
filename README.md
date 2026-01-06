# Python Programming Assignments – General Instructions

Welcome to your Python assignments repository! Please read these instructions carefully before starting. They apply to **all assignments** in this repository.

---

## 📥 Downloading the Files from GitHub
1. Go to the GitHub repository link shared with you.
2. Click on the green **Code** button and select **Download ZIP**.
3. Extract the ZIP file to a folder on your computer.
4. Each assignment will have three files:
   - `student_code_X_Y.py` → where you write your solution
   - `autograder_X_Y.py` → script to test and grade your code
   - `README.txt` → instructions specific to that assignment

---

## 🖥️ Writing and Testing Your Code
1. Open the file `student_code_X_Y.py` for the assignment you are working on.
2. Replace the `pass` statements with your code logic.
3. Save the file.
4. Open your **Command Line Interface (CLI)**:
   - On Windows: open **Command Prompt** or **PowerShell**
   - On Mac/Linux: open **Terminal**
5. Navigate to the folder where you extracted the assignments using:
   ```bash
   cd path/to/your/folder
   ```
6. Test your functions interactively before running the autograder:
    ```python
    >>> from student_code_X_Y import *
    >>> # Try calling your functions here
    ```

## 📝 Running the Autograder
1. Once you are confident your code works, run the autograder:
```bash
python .\autograder_X_Y.py
```
 or
```bash
python3 .\autograder_X_Y.py
```
2 The autograder will:
- Run a set of predefined tests
- Print your score and feedback
- Generate a Token for your submission
## 📊 Submitting Your Work
1. After running the autograder, take a screenshot of the final output showing:
- Your score
- Feedback
- Token
2. Paste your Token into the Excel sheet or Google Form provided by your instructor.
3. Upload the screenshot along with the ID as proof of completion.
## ⚠️ Important Points to Remember
- Do not rename files or functions. The autograder depends on exact names.
- Do not edit the autograder script. Any changes may invalidate your results.
- Your Token is tied to your computer, assignment, and batch time slot:
    - Same student, same assignment, same batch → same ID
    - Different assignment or batch → different ID
- If two students copy the same code on the same computer in the same batch, their IDs will match. This helps detect plagiarism.
- Always test your functions in the CLI before running the autograder to catch simple mistakes early.
- Submit both the Token and the screenshot. Submissions without screenshots will not be accepted.
- If you encounter errors:
- Check that your file is saved correctly.
- Ensure you are running the correct autograder for the assignment.
- Verify your Python installation (`python --version`).
## ✅ Workflow Summary
1. Download assignment files from GitHub.
2. Write your solution in `student_code_X_Y.py`.
3. Test your functions in the CLI.
4. Run the autograder (`autograder_X_Y.py`).
5. Record your score, feedback, and Token.
6. Submit your Token and screenshot in the Excel sheet/Google Form.

Happy coding and good luck with your assignments! 🚀
