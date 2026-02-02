# autograder_4_3.py

import importlib
import hashlib
import platform
import datetime
import os

def run_tests():
    try:
        student_code = importlib.import_module("student_code_4_3")
        func = student_code.sort_cities
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    feedback = []
    score = 0
    total = 20

    input_file = "sample_cities.txt"
    output_file = "sorted_cities.txt"

    # Run student function
    try:
        func(input_file, output_file)
        if os.path.exists(output_file):
            with open(output_file, "r") as f:
                sorted_cities = [line.strip() for line in f if line.strip()]
            expected = sorted(["Mumbai", "Delhi", "Chennai", "Kolkata", "Bengaluru", "Hyderabad"])
            if sorted_cities == expected:
                feedback.append("✅ Cities sorted correctly")
                score += 20
            else:
                feedback.append(f"❌ Cities not sorted correctly. Got: {sorted_cities}")
        else:
            feedback.append("❌ Output file not created")
    except Exception as e:
        feedback.append(f"❌ Function raised error: {e}")

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
        token = generate_token("Practical_4_Task_3")
        print("\nToken:", token)
        print("Paste this ID into the Excel sheet for verification.")
    else:
        print("\nToken not generated because not all tests passed.")