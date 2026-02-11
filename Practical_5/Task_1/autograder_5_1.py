# autograder_5_1.py

import importlib
import hashlib
import platform
import datetime
import io
import sys
import builtins

def run_tests():
    try:
        student_code = importlib.import_module("student_code_5_1")
        func = student_code.divide_numbers
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    feedback = []
    score = 0
    total = 30

    # Test 1: Valid division
    inputs = ["10", "2"]
    builtins.input = lambda prompt="": inputs.pop(0)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        func()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        if "5" in output:
            feedback.append("✅ Correct division performed")
            score += 10
        else:
            feedback.append("❌ Division result incorrect")
    except Exception as e:
        sys.stdout = sys.__stdout__
        feedback.append(f"❌ Error during valid division: {e}")

    # Test 2: Division by zero
    inputs = ["10", "0"]
    builtins.input = lambda prompt="": inputs.pop(0)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        func()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        if "Division by zero" in output or "not allowed" in output:
            feedback.append("✅ Division by zero handled correctly")
            score += 10
        else:
            feedback.append("❌ Division by zero not handled")
    except Exception as e:
        sys.stdout = sys.__stdout__
        feedback.append(f"❌ Error during division by zero: {e}")

    # Test 3: Invalid input
    inputs = ["abc", "2"]
    builtins.input = lambda prompt="": inputs.pop(0)
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        func()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        if "Invalid input" in output or "numeric" in output:
            feedback.append("✅ Invalid input handled correctly")
            score += 10
        else:
            feedback.append("❌ Invalid input not handled")
    except Exception as e:
        sys.stdout = sys.__stdout__
        feedback.append(f"❌ Error during invalid input: {e}")

    return {"score": score, "total": total, "feedback": "\n".join(feedback)}

def generate_token(assignment_tag: str):
    sysinfo = platform.node() + platform.system() + platform.release()
    now = datetime.datetime.now()
    batch_slot = (now.hour // 2)
    date_str = now.strftime("%Y-%m-%d")
    combined = sysinfo + assignment_tag + date_str + str(batch_slot)
    uid = hashlib.sha256(combined.encode()).hexdigest()[:10]
    return uid

if __name__ == "__main__":
    result = run_tests()
    print(f"Final Score: {result['score']} / {result['total']}")
    print("Feedback:\n", result["feedback"])

    if result['score'] == result['total']:
        token = generate_token("Practical_5_Task_1")
        print("\nToken: ", token)
        print("Paste this Token into the Excel sheet for verification.")
    else:
        print("\nToken not generated because not all tests passed.")