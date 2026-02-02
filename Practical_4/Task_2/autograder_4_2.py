# autograder_4_2.py

import importlib
import hashlib
import platform
import datetime
import io
import sys

def run_tests():
    try:
        student_code = importlib.import_module("student_code_4_2")
        func = student_code.find_closest_points
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    feedback = []
    score = 0
    total = 20

    test_filename = "sample_points.csv"

    # Capture output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        func(test_filename)
        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__

        if "Closest points are" in output and "with distance" in output:
            feedback.append("✅ Function executed and printed closest points")
            score += 10
        else:
            feedback.append("❌ Output did not match expected format")
    except Exception as e:
        sys.stdout = sys.__stdout__
        feedback.append(f"❌ Function raised error: {e}")

    # Check correctness by verifying known closest pair
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        func(test_filename)
        output = captured_output.getvalue().strip()
        sys.stdout = sys.__stdout__

        if "(1.0, 2.0, 3.0)" in output and "(1.1, 2.1, 3.1)" in output:
            feedback.append("✅ Correct closest pair identified")
            score += 10
        else:
            feedback.append("❌ Incorrect closest pair identified")
    except Exception as e:
        sys.stdout = sys.__stdout__
        feedback.append(f"❌ Function raised error: {e}")

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
        token = generate_token("Practical_4_Task_2")
        print("\nToken:", token)
        print("Paste this token into the Excel sheet for verification.")
    else:
        print("\nToken not generated because not all tests passed.")