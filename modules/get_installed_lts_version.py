import subprocess
import re


# Get the current version of node with "node -v" command and save the decoded result
version = subprocess.check_output(["node", "-v"]).decode("UTF-8")

# Then clean the result
installed_version = re.sub("[\sv]", "", version)
