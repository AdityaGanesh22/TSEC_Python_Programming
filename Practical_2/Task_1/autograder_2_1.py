# autograder_2_1.py

import importlib
import hashlib
import platform
import datetime

def run_tests():
    try:
        student_code = importlib.import_module("student_code_2_1")
        # List functions
        add_list = student_code.add_task_list
        remove_list = student_code.remove_task_list
        update_list = student_code.update_task_list
        sort_list = student_code.sort_tasks_list

        # Tuple functions
        add_tuple = student_code.add_task_tuple
        remove_tuple = student_code.remove_task_tuple
        update_tuple = student_code.update_task_tuple
        sort_tuple = student_code.sort_tasks_tuple
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    tests = [
        # List tests
        ("Add Task (list)", add_list, ([], "Distillation column design"), ["Distillation column design"]),
        ("Remove Task (list)", remove_list, (["Heat exchanger sizing"], "Heat exchanger sizing"), []),
        ("Update Task (list)", update_list, (["Pump selection"], 0, "Compressor selection"), ["Compressor selection"]),
        ("Sort Tasks (list)", sort_list, (["Reactor design", "Absorption study", "Catalyst testing"],), ["Absorption study", "Catalyst testing", "Reactor design"]),

        # Tuple tests
        ("Add Task (tuple)", add_tuple, ([], "Distillation column design", 2), [("Distillation column design", 2)]),
        ("Remove Task (tuple)", remove_tuple, ([("Heat exchanger sizing", 1)], ("Heat exchanger sizing", 1)), []),
        ("Update Task (tuple)", update_tuple, ([("Pump selection", 3)], 0, "Pump selection", 1), [("Pump selection", 1)]),
        ("Sort Tasks (tuple)", sort_tuple, ([("A", 3), ("B", 1), ("C", 2)],), [("B", 1), ("C", 2), ("A", 3)]),
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

    # Only generate token if ALL tests passed
    if result['score'] == result['total']:
        token = generate_token("Practical_2_Task_1")
        print("\nToken:", token)
        print("Paste this ID into the Google Form/Excel sheet for verification.")
    else:
        print("\n⚠️ Token not generated because not all tests passed.")