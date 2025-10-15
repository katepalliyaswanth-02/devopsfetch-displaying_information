import platform
import os
import subprocess   

def list_nginx(domain="all", current_os=None):
    """
    List Nginx server blocks or domain info.
    Linux only; Windows fallback.
    """
    if current_os is None:
        current_os = platform.system()

    if current_os == "Windows":
        print("Nginx info not supported on Windows.")
        return

    nginx_conf_dir = "/etc/nginx/sites-available"

    if domain == "all":
        try:
            sites = os.listdir(nginx_conf_dir)
            print("Nginx sites:")
            for site in sites:
                print(site)
        except Exception as e:
            print("Error accessing Nginx config:", e)
    else:
        site_file = os.path.join(nginx_conf_dir, domain)
        if os.path.exists(site_file):
            print(f"Details for {domain}:")
            with open(site_file) as f:
                print(f.read())
        else:
            print(f"Domain {domain} not found.")
