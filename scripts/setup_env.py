"""
setup_env.py
------------
Automates environment setup (installs packages, etc.).
"""

import subprocess

def setup_environment():
    subprocess.run(["pip", "install", "--upgrade", "pip", "setuptools", "wheel"])
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

if __name__ == "__main__":
    setup_environment()
