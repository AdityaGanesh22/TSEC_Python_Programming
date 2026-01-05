import importlib
import io
from contextlib import redirect_stdout
import hashlib
import platform
import datetime

def run_tests():
    try:
        student_code = importlib.import_module("student_code_1_1")
        func = student_code.personalized_greeting
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    tests = [
        ("Basic name", "Aditya"),
        ("Another name", "Ravi"),
        ("Empty string", ""),
    ]

    points_per_test = 10
    total = len(tests) * points_per_test
    score = 0
    feedback = []

    for label, name in tests:
        expected = f"Hello, {name}! Welcome to the Python course."
        try:
            with io.StringIO() as buf:
                with redirect_stdout(buf):
                    ret = func(name)
                printed = buf.getvalue().strip()

            # Strict enforcement: must print once and return None
            passed = (ret is None) and (printed == expected)

            if passed:
                score += points_per_test
                feedback.append(f"✅ {label} passed")
            else:
                feedback.append(
                    f"❌ {label} failed (returned: {ret!r}, printed: {printed!r}, expected: {expected!r})"
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

    assignment_tag = "Assignment_1_1"
    unique_id = generate_unique_id(assignment_tag)
    print("\nUnique ID:", unique_id)
