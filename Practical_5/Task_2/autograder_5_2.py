# autograder_5_2.py

import importlib
import hashlib
import platform
import datetime

def run_tests():
    try:
        student_code = importlib.import_module("student_code_5_2")
        withdraw = student_code.withdraw
        InsufficientFundsError = student_code.InsufficientFundsError
        InvalidAccountError = student_code.InvalidAccountError
        accounts = student_code.accounts
    except Exception as e:
        return {"score": 0, "total": 0, "feedback": f"Error importing student code: {e}"}

    feedback = []
    score = 0
    total = 30

    # Test 1: Valid withdrawal
    try:
        withdraw("12345", 200)
        if accounts["12345"] <= 800:
            feedback.append("✅ Valid withdrawal performed correctly")
            score += 10
        else:
            feedback.append("❌ Withdrawal did not update balance correctly")
    except Exception as e:
        feedback.append(f"❌ Error during valid withdrawal: {e}")

    # Test 2: Invalid account number
    try:
        withdraw("00000", 100)
        feedback.append("❌ Invalid account not handled")
    except InvalidAccountError:
        feedback.append("✅ Invalid account handled correctly")
        score += 10
    except Exception as e:
        feedback.append(f"❌ Wrong exception for invalid account: {e}")

    # Test 3: Insufficient funds
    try:
        withdraw("67890", 1000)
        feedback.append("❌ Insufficient funds not handled")
    except InsufficientFundsError:
        feedback.append("✅ Insufficient funds handled correctly")
        score += 10
    except Exception as e:
        feedback.append(f"❌ Wrong exception for insufficient funds: {e}")

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
        token = generate_token("Practical_5_Task_2")
        print("\nToken:", token)
        print("Paste this Token into the Excel sheet for verification.")
    else:
        print("\nToken not generated because not all tests passed.")