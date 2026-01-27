# autograder_3_9.py

import importlib
import hashlib
import platform
import datetime
import builtins
import io
import sys

def run_tests():
    try:
        student_code = importlib.import_module("student_code_3_9")
        start_func = student_code.start_game
        game_func = student_code.guessing_game
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    feedback = []
    score = 0
    total = 30  # 3 tests worth 10 points each

    # Test 1: start_game should initialize the secret number
    try:
        start_func()
        secret_number = getattr(student_code, "_secret_number", None)
        if secret_number is None:
            feedback.append("❌ start_game did not initialize the secret number")
        elif not (1 <= secret_number <= 100):
            feedback.append("❌ start_game initialized secret number outside 1–100")
        else:
            feedback.append("✅ start_game initialized secret number correctly")
            score += 10
    except Exception as e:
        feedback.append(f"❌ start_game failed: {e}")

    # Test 2: guessing_game should give correct feedback for low/high/correct guesses
    secret_number = getattr(student_code, "_secret_number", None)
    if secret_number is None:
        feedback.append("❌ guessing_game skipped because secret number not set")
    else:
        # Prepare simulated guesses: low, high, correct
        low_guess = secret_number - 1 if secret_number > 1 else secret_number
        high_guess = secret_number + 1 if secret_number < 100 else secret_number
        inputs = [str(low_guess), str(high_guess), str(secret_number)]

        def fake_input(prompt=""):
            return inputs.pop(0)

        original_input = builtins.input
        builtins.input = fake_input

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            game_func()
            output = captured_output.getvalue()
            sys.stdout = sys.__stdout__
            builtins.input = original_input

            if "Too low" in output and "Too high" in output and "Correct!" in output:
                feedback.append("✅ guessing_game gave correct feedback for low/high/correct guesses")
                score += 10
            else:
                feedback.append("❌ guessing_game did not print expected feedback messages")
        except Exception as e:
            sys.stdout = sys.__stdout__
            builtins.input = original_input
            feedback.append(f"❌ guessing_game raised error: {e}")

    # Test 3: guessing_game without start_game should warn user
    student_code._secret_number = None
    inputs = ["50"]
    builtins.input = lambda prompt="": inputs.pop(0)

    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        game_func()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        builtins.input = original_input

        if "No game in progress" in output:
            feedback.append("✅ guessing_game handled missing start_game correctly")
            score += 10
        else:
            feedback.append("❌ guessing_game did not warn when no game started")
    except Exception as e:
        sys.stdout = sys.__stdout__
        builtins.input = original_input
        feedback.append(f"❌ guessing_game failed when no game started: {e}")

    return {"score": score, "total": total, "feedback": "\n".join(feedback)}

def generate_unique_id(assignment_tag: str):
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
        unique_id = generate_unique_id("Practical_3_Task_9")
        print("\nUnique ID:", unique_id)
        print("Paste this ID into the Excel sheet for verification.")
    else:
        print("\nUnique ID not generated because not all tests passed.")