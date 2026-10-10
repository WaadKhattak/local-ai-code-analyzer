import os

def process_file(user_path):
    # Vulnerable to path traversal / command injection
    os.system("cat " + user_path)

def evaluate_formula(user_code):
    # Arbitrary code execution vulnerability
    return eval(user_code)
