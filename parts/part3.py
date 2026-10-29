import os
import socket
import re
import shutil
from part1 import run

def count_home_files():
    home = os.path.expanduser("~")
    files = 0
    dirs = 0
    try:
        for root, dnames, fnames in os.walk(home, onerror=lambda *a: None, followlinks=False):
            if "/.git/" in root or "/__pycache__" in root:
                continue
            dirs += len(dnames)
            files += len(fnames)
            if files > 50000:
                break
    except Exception:
        pass
    return home, files, dirs

def get_ips():
    ips = {}
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(2)
        s.connect(("8.8.8.8", 80))
        ips["local"] = s.getsockname()[0]
        s.close()
    except Exception:
        ips["local"] = "N/A"
    ip_a = run("ip -4 addr show 2>/dev/null")
    wlan = "N/A"
    if ip_a:
        m = re.search(r"inet (\d+\.\d+\.\d+\.\d+).*wlan0", ip_a)
        if m:
            wlan = m.group(1)
        else:
            m2 = re.findall(r"inet (\d+\.\d+\.\d+\.\d+)/", ip_a)
            if m2:
                for cand in m2:
                    if not cand.startswith("127."):
                        wlan = cand
                        break
    ips["wlan0"] = wlan
    return ips

def get_open_ports():
    ports = []
    out = run("ss -tln 2>/dev/null")
    if out:
        for line in out.splitlines():
            m = re.search(r":(\d+)\s", line)
            if m and m.group(1) not in ports:
                ports.append(m.group(1))
        if ports:
            return ports
    for path in ["/proc/net/tcp", "/proc/net/tcp6"]:
        try:
            with open(path) as f:
                lines = f.readlines()[1:]
                for ln in lines:
                    parts = ln.split()
                    if len(parts) >= 4 and parts[3] == "0A":
                        local = parts[1]
                        if ":" in local:
                            p_hex = local.split(":")[1]
                            try:
                                p = str(int(p_hex, 16))
                                if p not in ports:
                                    ports.append(p)
                            except Exception:
                                pass
        except Exception:
            pass
    return ports

def get_packages():
    c = run("pkg list-installed 2>/dev/null | wc -l")
    if c and c.strip().isdigit() and int(c.strip()) > 0:
        return c.strip()
    c2 = run("dpkg -l 2>/dev/null | grep -c '^ii'")
    return c2.strip() if c2 else "N/A"

def get_disk_home(home):
    try:
        total, used, free = shutil.disk_usage(home)
        return f"{used//1024//1024}M / {total//1024//1024}M"
    except Exception:
        return "N/A"
