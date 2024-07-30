from modules.get_latest_lts_version import latest_lts_version
from modules.get_installed_lts_version import installed_version
from colorama import Fore as color, init as start_colorama

start_colorama()

# Compare the latest LTS version with the installed version
if latest_lts_version == installed_version:
    print(color.GREEN + "[+] Node.js LTS version is up to date :D")
else:
    print(color.RED + "[-] Node.js LTS version is outdated :(")
