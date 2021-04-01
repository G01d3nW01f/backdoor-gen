#!/usr/bin/python3

import os
import sys

if os.getuid() != 0:
    print("[!]YouMustExecute as root!!!!")
    sys.exit()

print("[+]Now SetUp....")

step1 = "chmod +x bdoor-gen.py"

step2 = "sudo cp bdoor-gen.py /usr/bin/bdoor-gen"

os.system(step1)

os.system(step2)

print("Done...")
