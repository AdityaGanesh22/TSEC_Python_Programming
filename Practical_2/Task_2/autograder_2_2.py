# autograder_2_2.py

import importlib
import hashlib
import platform
import datetime

def run_tests():
    try:
        student_code = importlib.import_module("student_code_2_2")
        union_func = student_code.union_enrollments
        intersection_func = student_code.intersection_enrollments
        difference_func = student_code.difference_enrollments
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    CET = {"Aditi", "Rahul", "Sneha"}
    JEE = {"Rahul", "Sneha", "Karan"}
    NEET = {"Aditi", "Karan", "Meera"}

    tests = [
        ("Union CET & JEE", union_func, (CET, JEE), {"Aditi", "Rahul", "Sneha", "Karan"}),
        ("Intersection CET & JEE", intersection_func, (CET, JEE), {"Rahul", "Sneha"}),
        ("Difference CET - JEE", difference_func, (CET, JEE), {"Aditi"}),
        ("Union JEE & NEET", union_func, (JEE, NEET), {"Rahul", "Sneha", "Karan", "Aditi", "Meera"}),
        ("Intersection JEE & NEET", intersection_func, (JEE, NEET), {"Karan"}),
        ("Difference NEET - CET", difference_func, (NEET, CET), {"Karan", "Meera"}),
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
        token = generate_token("Practical_2_Task_2")
        print("\nToken:", token)
        print("Paste this ID into the Google Form/Excel sheet for verification.")
    else:
        print("\n⚠️ Token not generated because not all tests passed.")