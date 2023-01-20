#/usr/bin/env python3

from modules.get_latest_lts_version import latest_version
from modules.get_installed_lts_version import installed_version

from colorama import Fore as color, init as start_colorama

start_colorama()

if latest_version == installed_version:
    print(color.GREEN + "[+] La versión LTS de NodeJS está al día :D")
else:
    print(color.RED + "[-] La versión LTS de NodeJS está desactualizada :(")

