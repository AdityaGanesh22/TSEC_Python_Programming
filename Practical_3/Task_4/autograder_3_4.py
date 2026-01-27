# autograder_3_4.py

import importlib
import hashlib
import platform
import datetime
import io
import sys

def run_tests():
    try:
        student_code = importlib.import_module("student_code_3_4")
        table_func = student_code.generate_table
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    tests = [
        ("Table of 3", 3, 5, "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n3 x 4 = 12\n3 x 5 = 15\n"),
        ("Table of 7", 7, 3, "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n"),
    ]

    points_per_test = 10
    total = len(tests) * points_per_test
    score = 0
    feedback = []

    for label, n, upto, expected in tests:
        try:
            buffer = io.StringIO()
            sys.stdout = buffer
            table_func(n, upto)
            sys.stdout = sys.__stdout__
            result = buffer.getvalue()
            if result == expected:
                score += points_per_test
                feedback.append(f"✅ {label} passed")
            else:
                feedback.append(f"❌ {label} failed (got:\n{result}expected:\n{expected})")
        except Exception as e:
            feedback.append(f"❌ {label} raised error: {e}")
        finally:
            sys.stdout = sys.__stdout__

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
        token = generate_token("Practical_3_Task_4")
        print("\nToken:", token)
        print("Paste this ID into the Google Form/Excel sheet for verification.")
    else:
        print("\n⚠️ Token not generated because not all tests passed.")