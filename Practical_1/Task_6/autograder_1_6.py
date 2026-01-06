# autograder_1_6.py

import importlib
import hashlib
import platform
import datetime

def run_tests():
    try:
        student_code = importlib.import_module("student_code_1_6")
        add_func = student_code.add_numbers
        sub_func = student_code.subtract_numbers
        mul_func = student_code.multiply_numbers
        div_func = student_code.divide_numbers
        mod_func = student_code.modulus_numbers
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    tests = [
        ("Addition", add_func, (10, 5), 15),
        ("Subtraction", sub_func, (10, 5), 5),
        ("Multiplication", mul_func, (10, 5), 50),
        ("Division", div_func, (10, 5), 2),
        ("Modulus", mod_func, (10, 5), 0),
    ]

    points_per_test = 10
    total = len(tests) * points_per_test
    score = 0
    feedback = []

    for label, func, args, expected in tests:
        try:
            result = func(*args)
            passed = abs(result - expected) < 1e-6
            if passed:
                score += points_per_test
                feedback.append(f"✅ {label} passed")
            else:
                feedback.append(
                    f"❌ {label} failed (got: {result!r}, expected: {expected!r})"
                )
        except Exception as e:
            feedback.append(f"❌ {label} raised error: {e}")

    return {"score": score, "total": total, "feedback": "\n".join(feedback)}

def generate_unique_id(assignment_tag: str):
    # System info (computer-specific)
    sysinfo = platform.node() + platform.system() + platform.release()

    # Current time bucket (2-hour batches)
    now = datetime.datetime.now()
    batch_slot = (now.hour // 2)  # integer division
    date_str = now.strftime("%Y-%m-%d")

    # Combine everything
    combined = sysinfo + assignment_tag + date_str + str(batch_slot)
    uid = hashlib.sha256(combined.encode()).hexdigest()[:10]
    return uid

if __name__ == "__main__":
    result = run_tests()
    print(f"Final Score: {result['score']} / {result['total']}")
    print("Feedback:\n", result["feedback"])

    if result['score'] == result['total']:
        unique_id = generate_unique_id("Assignment_1_6")
        print("\nToken: ", unique_id)