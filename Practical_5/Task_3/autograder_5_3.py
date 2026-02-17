# autograder_5_3.py

import importlib
import hashlib
import platform
import datetime
import io
import sys
import logging

def run_tests():
    try:
        student_code = importlib.import_module("student_code_5_3")
        func = student_code.divide_numbers
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    feedback = []
    score = 0
    total = 20

    # Capture logs
    log_stream = io.StringIO()
    logging.basicConfig(stream=log_stream, level=logging.DEBUG, force=True)

    # Test 1: Valid division
    try:
        result = func(10, 2)
        logs = log_stream.getvalue()
        if result == 5 and "Division successful" in logs:
            feedback.append("✅ Valid division logged correctly")
            score += 10
        else:
            feedback.append("❌ Valid division not logged correctly")
    except Exception as e:
        feedback.append(f"❌ Error during valid division: {e}")

    # Reset log stream
    log_stream = io.StringIO()
    logging.basicConfig(stream=log_stream, level=logging.DEBUG, force=True)

    # Test 2: Division by zero
    try:
        result = func(10, 0)
        logs = log_stream.getvalue()
        if result is None and "Division by zero" in logs:
            feedback.append("✅ Division by zero logged correctly")
            score += 10
        else:
            feedback.append("❌ Division by zero not logged correctly")
    except Exception as e:
        feedback.append(f"❌ Error during division by zero: {e}")

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
        token = generate_token("Practical_5_Task_3")
        print("\nToken:", token)
        print("Paste this Token into the Excel sheet for verification.")
    else:
        print("\nToken not generated because not all tests passed.")