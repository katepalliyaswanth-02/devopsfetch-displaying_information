#!/usr/bin/env python3
"""
DevOpsFetch — Server Information Retrieval and Monitoring Tool
Author: Your Name
"""

import argparse
import platform
from modules.ports_info import list_ports
from modules.docker_info import list_docker
from modules.nginx_info import list_nginx
from modules.users_info import list_users
from modules.time_activity import show_time_logs
from modules.monitor import monitor_loop


def main():
    parser = argparse.ArgumentParser(
        description="DevOpsFetch — A DevOps tool for system information retrieval and monitoring."
    )

    parser.add_argument(
        "-p", "--port", nargs="?", const="all",
        help="Display all active ports or details for a specific port."
    )
    parser.add_argument(
        "-d", "--docker", nargs="?", const="all",
        help="List Docker images/containers or details for a specific container."
    )
    parser.add_argument(
        "-n", "--nginx", nargs="?", const="all",
        help="Display all Nginx domains or details for a specific domain."
    )
    parser.add_argument(
        "-u", "--users", nargs="?", const="all",
        help="List users and last login times or details for a specific user."
    )
    parser.add_argument(
        "-t", "--time", nargs=2, metavar=("START", "END"),
        help="Display activities within a specified time range (YYYY-MM-DD)."
    )
    parser.add_argument(
        "-m", "--monitor", action="store_true",
        help="Start continuous monitoring mode."
    )

    args = parser.parse_args()

    # Detect platform
    current_os = platform.system()  # 'Windows', 'Linux', 'Darwin'

    # Route commands to corresponding modules
    if args.port is not None:
        list_ports(args.port, current_os)
    elif args.docker is not None:
        list_docker(args.docker, current_os)
    elif args.nginx is not None:
        list_nginx(args.nginx, current_os)
    elif args.users is not None:
        list_users(args.users, current_os)
    elif args.time is not None:
        show_time_logs(args.time[0], args.time[1])
    elif args.monitor:
        monitor_loop()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
