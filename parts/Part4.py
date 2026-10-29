from part1 import GENTOO_LOGO, PURPLE, GREEN, CYAN, YELLOW, BOLD, RESET

def print_fetch(info_lines):
    max_lines = max(len(GENTOO_LOGO), len(info_lines))
    print()
    for i in range(max_lines):
        left = GENTOO_LOGO[i] if i < len(GENTOO_LOGO) else ""
        right = info_lines[i] if i < len(info_lines) else ""
        print(f"{PURPLE}{BOLD}{left:<20}{RESET}  {right}")
    print()
    print(f"{PURPLE}â– â– â– â– â– {RESET} {GREEN}â– â– â– â– â– {RESET} {CYAN}â– â– â– â– â– {RESET} {YELLOW}â– â– â– â– â– {RESET}")
