# autograder_5_5.py

import importlib
import hashlib
import platform
import datetime
import sys

def run_tests():
    try:
        student_code = importlib.import_module("student_code_5_5")
        func = student_code.binary_search
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    feedback = []
    score = 0
    total = 20

    # Test 1: Target present
    arr = [1, 3, 5, 7, 9]
    result = func(arr, 5)
    if result == 2:
        feedback.append("✅ Found target correctly")
        score += 10
    else:
        feedback.append("❌ Did not find target correctly")

    # Test 2: Target absent
    result = func(arr, 4)
    if result == -1:
        feedback.append("✅ Returned -1 when target not found")
        score += 10
    else:
        feedback.append("❌ Did not return -1 when target not found")

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
        token = generate_token("Practical_5_Task_5")
        print("\nToken:", token)
        print("Paste this Token into the Excel sheet for verification.")
    else:
        print("\nToken not generated because not all tests passed.")