# autograder_3_2.py

import importlib
import hashlib
import platform
import datetime

def run_tests():
    try:
        student_code = importlib.import_module("student_code_3_2")
        type_func = student_code.identify_number_type
        range_func = student_code.identify_range
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    tests = [
        ("Check single even", type_func, (4,), "Even"),
        ("Check single odd", type_func, (7,), "Odd"),
        ("Range 1 to 3", range_func, (1, 3), ["Odd", "Even", "Odd"]),
        ("Range 2 to 6", range_func, (2, 6), ["Even", "Odd", "Even", "Odd", "Even"]),
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
                feedback.append(f"❌ {label} failed (got: {result!r}, expected: {expected!r})")
        except Exception as e:
            feedback.append(f"❌ {label} raised error: {e}")

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
        token = generate_token("Practical_3_Task_2")
        print("\nToken:", token)
        print("Paste this ID into the Google Form/Excel sheet for verification.")
    else:
        print("\n⚠️ Token not generated because not all tests passed.")