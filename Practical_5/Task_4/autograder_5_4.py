# autograder_5_4.py

import importlib
import hashlib
import platform
import datetime

def run_tests():
    try:
        student_code = importlib.import_module("student_code_5_4")
        buggy_function = student_code.buggy_function
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    feedback = []
    score = 0
    total = 10

    # The autograder cannot check debugging directly.
    # Instead, it verifies that the function exists.
    try:
        buggy_function
        feedback.append("✅ buggy_function exists for debugging demonstration")
        score += 10
    except Exception as e:
        feedback.append(f"❌ buggy_function not found: {e}")

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
        token = generate_token("Practical_5_Task_4")
        print("\nToken:", token)
        print("Paste this token into the Excel sheet for verification.")
    else:
        print("\nToken not generated because not all tests passed.")