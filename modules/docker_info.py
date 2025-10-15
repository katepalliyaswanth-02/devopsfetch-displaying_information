import subprocess
import platform

def list_docker(container="all", current_os=None):
    """
    List Docker images/containers.
    Works on Linux and Windows.
    """
    if current_os is None:
        current_os = platform.system()

    try:
        if container == "all":
            cmd = ["docker", "ps", "-a"]
        else:
            cmd = ["docker", "ps", "-a", "--filter", f"name={container}"]

        result = subprocess.getoutput(" ".join(cmd))
        print(result)
    except Exception as e:
        print("Error accessing Docker:", e)
        if current_os == "Windows":
            print("Make sure Docker Desktop is running.")
