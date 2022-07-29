import os

os.system("cd sustainableGardenBackend/sustainableGardenBackend && docker-compose up -d")
os.system("python checkFileChange.py")