import os, sys
os.system("git pull")
try:
    __import__("riddu").Main()
except Exception as e:
    exit(str(e))
