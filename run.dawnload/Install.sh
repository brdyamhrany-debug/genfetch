#!/bin/bash
# install.sh - check python and install packages from packages.txt
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
NC='\033[0m'

PKG_FILE="packages.txt"

echo -e "${CYAN}[*] Checking python...${NC}"
if ! command -v python >/dev/null 2>&1 && ! command -v python3 >/dev/null 2>&1; then
  echo -e "${RED}[X] Python not found!${NC}"
  echo -ne "${CYAN}[?] Do you want to install it now? [Y/n]: ${NC}"
  read answer
  answer=${answer:-Y}
  if [[ "$answer" =~ ^[Yy]$ ]]; then
    echo -e "${CYAN}[*] Installing python...${NC}"
    if [[ "$PREFIX" == *"com.termux"* ]]; then
      pkg update -y && pkg install -y python
    else
      sudo apt update && sudo apt install -y python3
    fi
    if ! command -v python >/dev/null 2>&1 && ! command -v python3 >/dev/null 2>&1; then
      echo -e "${RED}[X] Python install failed${NC}"
      exit 1
    fi
    echo -e "${GREEN}[OK] Python installed${NC}"
  else
    echo -e "${YELLOW}Skip python install${NC}"
  fi
else
  echo -e "${GREEN}[OK] Python found, skip prompt${NC}"
fi

if [ ! -f "$PKG_FILE" ]; then
  echo -e "${YELLOW}File $PKG_FILE not found${NC}"
  exit 1
fi

if [[ "$PREFIX" == *"com.termux"* ]]; then
  echo -e "${CYAN}[*] Termux detected, updating...${NC}"
  pkg update -y
  while read -r pkg || [ -n "$pkg" ]; do
    [[ -z "$pkg" || "$pkg" =~ ^# ]] && continue
    echo -e "${CYAN}[*] installing $pkg ...${NC}"
    pkg install -y "$pkg"
  done < "$PKG_FILE"
else
  echo -e "${CYAN}[*] Linux detected, updating...${NC}"
  sudo apt update
  while read -r pkg || [ -n "$pkg" ]; do
    [[ -z "$pkg" || "$pkg" =~ ^# ]] && continue
    echo -e "${CYAN}[*] installing $pkg ...${NC}"
    sudo apt install -y "$pkg"
  done < "$PKG_FILE"
fi

echo -e "${GREEN}[OK] All packages installed${NC}"
