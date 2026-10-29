import os
import platform
from part1 import run, GREEN, CYAN, PURPLE, BOLD, RESET
from part2 import get_android_info, get_kernel_info, get_uptime
from part3 import count_home_files, get_ips, get_open_ports, get_packages, get_disk_home
from part4 import print_fetch

def main():
    user = os.environ.get("USER", "")
    if not user:
        user = run("whoami") or "u0"

    android = get_android_info()
    kernel = get_kernel_info()
    uptime = get_uptime()

    home, n_files, n_dirs = count_home_files()
    ips = get_ips()
    ports = get_open_ports()
    pkgs = get_packages()
    disk = get_disk_home(home)

    shell = os.environ.get("SHELL", "bash")
    term = os.environ.get("TERM", "termux")
    pyver = platform.python_version()
    host = kernel["node"] if kernel["node"] else android["model"]

    info = []
    info.append(f"{BOLD}{GREEN}{user}{RESET}@{BOLD}{CYAN}{host}{RESET}")
    info.append("------------------")
    info.append(f"{BOLD}{PURPLE}OS:{RESET} Android {android['android_ver']} (SDK {android['sdk']}) + Termux")
    info.append(f"{BOLD}{PURPLE}Host:{RESET} {android['manuf']} {android['model']}".strip())
    info.append(f"{BOLD}{PURPLE}Build:{RESET} {android['build']}")
    info.append(f"{BOLD}{PURPLE}Kernel:{RESET} {kernel['release']}")
    info.append(f"{BOLD}{PURPLE}Kernel Full:{RESET} {kernel['full'][:80]}")
    info.append(f"{BOLD}{PURPLE}Uptime:{RESET} {uptime}")
    info.append(f"{BOLD}{PURPLE}Shell:{RESET} {shell}")
    info.append(f"{BOLD}{PURPLE}Python:{RESET} {pyver}")
    info.append(f"{BOLD}{PURPLE}Terminal:{RESET} {term}")
    info.append(f"{BOLD}{PURPLE}Packages:{RESET} {pkgs}")
    info.append(f"{BOLD}{PURPLE}HOME:{RESET} {home}")
    info.append(f"{BOLD}{PURPLE}Files:{RESET} {n_files} file, {n_dirs} dir")
    info.append(f"{BOLD}{PURPLE}Disk HOME:{RESET} {disk}")
    info.append(f"{BOLD}{PURPLE}Local IP:{RESET} {ips.get('local', 'N/A')}")
    info.append(f"{BOLD}{PURPLE}wlan0 IP:{RESET} {ips.get('wlan0', 'N/A')}")
    info.append(f"{BOLD}{PURPLE}Open Ports:{RESET} {len(ports)} open")
    if ports:
        info.append(f"{BOLD}{PURPLE}Ports:{RESET} {', '.join(sorted(ports, key=lambda x: int(x))[:15])}")
    else:
        info.append(f"{BOLD}{PURPLE}Ports:{RESET} none / need ss")

    print_fetch(info)

if __name__ == "__main__":
    main()
