import platform
import subprocess
from datetime import datetime

def list_users(user="all", current_os=None):
    """
    List users and last login times.
    """
    if current_os is None:
        current_os = platform.system()

    if current_os == "Windows":
        # Windows users
        if user == "all":
            result = subprocess.getoutput("net user")
            print(result)
        else:
            result = subprocess.getoutput(f"net user {user}")
            print(result)
    else:
        # Linux users
        if user == "all":
            result = subprocess.getoutput("cut -d: -f1 /etc/passwd")
            print(result)
        else:
            try:
                last_login = subprocess.getoutput(f"last -n 1 {user}")
                print(last_login)
            except Exception as e:
                print(f"Error retrieving info for {user}:", e)
