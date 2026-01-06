# autograder_1_2.py

import importlib
import math
import hashlib
import platform
import datetime

def run_tests():
    try:
        student_code = importlib.import_module("student_code_1_2")
        circle_func = student_code.area_circle
        rect_func = student_code.area_rectangle
        tri_func = student_code.area_triangle
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    tests = [
        ("Circle area", circle_func, (3,), math.pi * 9),
        ("Rectangle area", rect_func, (4, 5), 20),
        ("Triangle area", tri_func, (6, 8), 24),
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

    now = datetime.datetime.now()
    batch_slot = (now.hour // 2) 
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
        assignment_tag = "Assignment_1_2"
        unique_id = generate_unique_id(assignment_tag)
        print("\nToken: :", unique_id)