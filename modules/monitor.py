import time
from modules.ports_info import list_ports
from modules.docker_info import list_docker

def monitor_loop(current_os=None):
    """
    Simple continuous monitoring loop.
    """
    if current_os is None:
        import platform
        current_os = platform.system()

    try:
        while True:
            print("=== Monitoring ===")
            print("\nPorts:")
            list_ports("all", current_os)
            print("\nDocker:")
            list_docker("all", current_os)
            print("\nNext update in 60 seconds...\n")
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
