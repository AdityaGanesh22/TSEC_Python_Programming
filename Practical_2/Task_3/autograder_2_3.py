# autograder_2_3.py

import importlib
import hashlib
import platform
import datetime

def run_tests():
    try:
        student_code = importlib.import_module("student_code_2_3")
        create_func = student_code.create_record
        update_grade_func = student_code.update_grade
        update_attendance_func = student_code.update_attendance
        delete_func = student_code.delete_record
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    tests = [
        ("Create Record", create_func, ({}, "Aditi", "A", 90), {"Aditi": {"grade": "A", "attendance": 90}}),
        ("Update Grade", update_grade_func, ({"Rahul": {"grade": "B", "attendance": 85}}, "Rahul", "A"), {"Rahul": {"grade": "A", "attendance": 85}}),
        ("Update Attendance", update_attendance_func, ({"Sneha": {"grade": "C", "attendance": 70}}, "Sneha", 95), {"Sneha": {"grade": "C", "attendance": 95}}),
        ("Delete Record", delete_func, ({"Karan": {"grade": "B", "attendance": 80}}, "Karan"), {}),
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
        token = generate_token("Practical_2_Task_3")
        print("\nToken:", token)
        print("Paste this ID into the Google Form/Excel sheet for verification.")
    else:
        print("\n⚠️ Token not generated because not all tests passed.")