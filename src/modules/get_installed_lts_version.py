import subprocess

# Run the 'node -v' command to get the Node.js version
version = subprocess.run(["node", "-v"], capture_output=True, text=True)

# Extract and clean up the version output
installed_version = version.stdout.strip()
