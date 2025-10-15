import subprocess
import platform
from prettytable import PrettyTable

def list_ports(port="all", current_os=None):
    """
    List active ports and connections.
    Works on Linux and Windows.
    """

    if current_os is None:
        current_os = platform.system()  # Detect OS if not provided

    if current_os == "Windows":
        # Windows equivalent using netstat
        if port == "all":
            result = subprocess.getoutput("netstat -ano")
            print(result)
        else:
            result = subprocess.getoutput(f'netstat -ano | findstr :{port}')
            print(f"Details for port {port}:\n{result}")

    else:
        # Linux version
        if port == "all":
            result = subprocess.getoutput("sudo ss -tulpen")
            print(result)
        else:
            result = subprocess.getoutput(f"sudo ss -tulpen | grep :{port}")
            print(f"Details for port {port}:\n{result}")
