import platform
from part1 import run, get_prop

def get_android_info():
    return {
        "android_ver": get_prop("ro.build.version.release") or "unknown",
        "sdk": get_prop("ro.build.version.sdk") or "?",
        "model": get_prop("ro.product.model") or "unknown",
        "manuf": get_prop("ro.product.manufacturer") or "",
        "build": get_prop("ro.build.display.id") or "N/A",
    }

def get_kernel_info():
    uname = platform.uname()
    kernel_full = run("uname -a")
    if not kernel_full:
        kernel_full = f"{uname.system} {uname.release} {uname.version} {uname.machine}"
    return {
        "node": uname.node,
        "release": uname.release,
        "full": kernel_full,
        "machine": uname.machine,
    }

def get_uptime():
    try:
        with open("/proc/uptime") as f:
            sec = float(f.read().split()[0])
            h = int(sec // 3600)
            m = int((sec % 3600) // 60)
            if h > 0:
                return f"{h}h {m}m"
            return f"{m}m"
    except Exception:
        pass
    u = run("uptime -p")
    return u if u else "unknown"
