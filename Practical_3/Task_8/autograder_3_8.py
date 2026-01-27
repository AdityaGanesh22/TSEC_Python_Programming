# autograder_3_8.py

import importlib
import hashlib
import platform
import datetime

def run_tests():
    try:
        student_code = importlib.import_module("student_code_3_8")
        add_func = student_code.add
        sub_func = student_code.subtract
        mul_func = student_code.multiply
        div_func = student_code.divide
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    tests = [
        ("Addition test", add_func, (5, 3), 8),
        ("Subtraction test", sub_func, (10, 4), 6),
        ("Multiplication test", mul_func, (7, 6), 42),
        ("Division test", div_func, (20, 5), 4.0),
    ]

    points_per_test = 10
    total = len(tests) * points_per_test
    score = 0
    feedback = []

    for label, func, args, expected in tests:
        try:
            result = func(*args)
            if result == expected:
                score += points_per_test
                feedback.append(f"✅ {label} passed")
            else:
                feedback.append(f"❌ {label} failed (got: {result}, expected: {expected})")
        except Exception as e:
            feedback.append(f"❌ {label} raised error: {e}")

    # Division by zero test
    try:
        div_func(10, 0)
        feedback.append("❌ Division by zero test failed (no error raised)")
    except ValueError:
        score += points_per_test
        feedback.append("✅ Division by zero test passed")
    except Exception as e:
        feedback.append(f"❌ Division by zero test raised wrong error: {e}")

    total += points_per_test

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
        token = generate_token("Practical_3_Task_8")
        print("\nToken:", token)
        print("Paste this ID into the Excel sheet for verification.")
    else:
        print("\n⚠️ Token not generated because not all tests passed.")