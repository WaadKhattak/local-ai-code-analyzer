import os

def run_user_input(user_data):
    # Vulnerable to code execution
    exec(user_data)

def remove_log_file(log_name):
    # Vulnerable to command injection
    os.system("rm -f /var/logs/" + log_name)
