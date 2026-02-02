# autograder_4_4.py

import importlib
import hashlib
import platform
import datetime
import subprocess
import sys
import os

def run_tests():
    feedback = []
    score = 0
    total = 20

    # Step 1: Import student code
    try:
        student_code = importlib.import_module("student_code_4_4")
        func = getattr(student_code, "main", None)
        if func:
            feedback.append("✅ Found main() function")
            score += 5
        else:
            feedback.append("❌ No main() function found")
    except Exception as e:
        feedback.append(f"❌ Error importing student code: {e}")
        return {"score": 0, "total": total, "feedback": "\n".join(feedback)}

    # Step 2: Ensure PyInstaller is installed
    try:
        subprocess.run([sys.executable, "-m", "pip", "show", "pyinstaller"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller", "--quiet"])
        feedback.append("✅ PyInstaller installed or already present")
        score += 5
    except Exception as e:
        feedback.append(f"❌ Failed to install PyInstaller: {e}")
        return {"score": score, "total": total, "feedback": "\n".join(feedback)}

    # Step 3: Run PyInstaller to build executable
    try:
        subprocess.run(["pyinstaller", "--onefile", "student_code_4_4.py"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        exe_path = os.path.join("dist", "student_code_4_4.exe")
        if os.path.exists(exe_path):
            feedback.append("✅ Executable created successfully")
            score += 10
        else:
            feedback.append("❌ Executable not found in dist/")
    except Exception as e:
        feedback.append(f"❌ PyInstaller build failed: {e}")

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
        token = generate_token("Practical_4_Task_4")
        print("\nToken:", token)
        print("Paste this token into the Excel sheet for verification.")
    else:
        print("\nToken not generated because not all tests passed.")