from datetime import datetime
import os

# ---------------- Calculator ----------------
def calculate(expression: str):
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Invalid mathematical expression."

# ---------------- Current Time ----------------
def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---------------- List Files ----------------
def list_files(folder="."):
    try:
        return os.listdir(folder)
    except Exception as e:
        return str(e)

# ---------------- Read File ----------------
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except Exception as e:
        return str(e)