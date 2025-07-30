# get-pip.py (for installing pip)
# Source: https://bootstrap.pypa.io/get-pip.py

import os
import tempfile
import urllib.request
import runpy

url = "https://bootstrap.pypa.io/pip/get-pip.py"
print("Downloading get-pip.py from PyPA...")

with urllib.request.urlopen(url) as response:
    data = response.read()

with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp_file:
    tmp_file.write(data)
    tmp_path = tmp_file.name

print("Running installer...")
runpy.run_path(tmp_path)
os.remove(tmp_path)
print("✅ pip installed successfully.")
