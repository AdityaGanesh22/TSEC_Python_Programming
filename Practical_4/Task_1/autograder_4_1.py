# autograder_4_1.py

import importlib
import hashlib
import platform
import datetime
import io
import sys
import builtins

def run_tests():
    try:
        student_code = importlib.import_module("student_code_4_1")
        func = student_code.extract_words
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    feedback = []
    score = 0
    total = 30  # 3 tests worth 10 points each

    test_filename = "sample_text.txt"

    # Test 1: Extract 3-letter words
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        func(test_filename, [3])
        output = captured_output.getvalue().strip().split("\n")
        sys.stdout = sys.__stdout__

        expected = {"Cat", "bat", "rat", "dog"}
        if expected.issubset(set(output)):
            feedback.append("✅ Correctly extracted 3-letter words")
            score += 10
        else:
            feedback.append(f"❌ Did not extract 3-letter words correctly. Got: {output}")
    except Exception as e:
        sys.stdout = sys.__stdout__
        feedback.append(f"❌ Function raised error on 3-letter test: {e}")

    # Test 2: Extract 4-letter words
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        func(test_filename, [4])
        output = captured_output.getvalue().strip().split("\n")
        sys.stdout = sys.__stdout__

        expected = {"lion", "four", "five"}
        if expected.issubset(set(output)):
            feedback.append("✅ Correctly extracted 4-letter words")
            score += 10
        else:
            feedback.append(f"❌ Did not extract 4-letter words correctly. Got: {output}")
    except Exception as e:
        sys.stdout = sys.__stdout__
        feedback.append(f"❌ Function raised error on 4-letter test: {e}")

    # Test 3: Extract 5-letter words
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        func(test_filename, [5])
        output = captured_output.getvalue().strip().split("\n")
        sys.stdout = sys.__stdout__

        expected = {"tiger", "three", "seven"}
        if expected.issubset(set(output)):
            feedback.append("✅ Correctly extracted 5-letter words")
            score += 10
        else:
            feedback.append(f"❌ Did not extract 5-letter words correctly. Got: {output}")
    except Exception as e:
        sys.stdout = sys.__stdout__
        feedback.append(f"❌ Function raised error on 5-letter test: {e}")

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
        token = generate_token("Practical_4_Task_1")
        print("\nToken:", token)
        print("Paste this ID into the Excel sheet for verification.")
    else:
        print("\nToken not generated because not all tests passed.")