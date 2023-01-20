import subprocess
import re

# Obtiene la versión actualmente instalada de node con comando "node -v" y guarda el resultado decodificado
version = subprocess.check_output(["node", "-v"]).decode("UTF-8")
# Después limpia el resultado
installed_version = re.sub("[\sv]", "", version)
