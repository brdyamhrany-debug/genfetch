import subprocess

PURPLE = "\033[95m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

GENTOO_LOGO = [
    "         _-----_",
    "        (       \\ ",
    "         \\    0   \\ ",
    "          \\        )",
    "          /      _/",
    "         (     _-",
    "          \\____-",
    "         Gentoo",
    "       Linux ARM",
    "      on Termux",
]

def run(cmd):
    try:
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
        return out.stdout.strip()
    except Exception:
        return ""

def get_prop(name):
    return run(f"getprop {name}")
