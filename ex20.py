# check file existense

import os

filename="student.txt"

if os.path.exists(filename):
    print("file exists")
else:
    print("filr not found")