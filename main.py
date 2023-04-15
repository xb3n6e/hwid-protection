# Imports
import os
import subprocess
import time
import requests

############
# Settings #
############
logs = 2 # 1 = enable logs | 2 = disable logs

# Checking user System HWID
hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
# Checking user HWID
userhwid = requests.get("http://localhost/hwidprotect/hwidcheck.html")

# Language
LINE = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
INVISIBLELINE = " "

CHECKING = "Checking your HWID.."
INVALID_HWID = "Invalid HWID"
VALID_HWID = "Valid HWID"
SUPPORT = "Please contact with support: "

FILE_DOESNT_EXIST = "The log file does not exist! Creating.."
READ_LOG = "Successfully created!\nRead log for more informations."
LOG_MSG = "HWID Error log:\nYour HWID: " + hwid + "\nFor support join our discord server! discord.gg/hwidprotect" # You can use \n to the new line
LOG_FILE = "log.txt"
LOG_TYPE = "a" # !! Don't touch this !!

DISCORD = "discord.gg/hwidprotect"

# Access Language
NOT_HAVE_ACCESS = "You dont have acces to this program!"
HAVE_ACCESS = "You had access to this program!"

# What the time to wait python to leave this program if user don't have access
EXIT_TIME = 3 # In seconds
# What the time to wait python to redirect user to main program if user have access
REDIRECT_TIME = 2 # In seconds

# If System HWID = User HWID python print have access and redirect to the program
if hwid in userhwid.text:
    print(LINE)
    time.sleep(1)
    print(CHECKING)
    time.sleep(2)
    print(VALID_HWID)
    time.sleep(1)
    print(LINE)
    print(HAVE_ACCESS)
    time.sleep(REDIRECT_TIME)
    # Call your project here
    exit()
# If System HWID != User HWID python print don't have access and exit from the program
else:
    print(LINE)
    time.sleep(1)
    print(CHECKING)
    time.sleep(2.5)
    print(INVALID_HWID)
    print(SUPPORT + DISCORD)
    time.sleep(1)
    print(LINE)
    print(NOT_HAVE_ACCESS)
    print(INVISIBLELINE)
    # Create a log file if you added this in Settings menu
    if logs == 1:
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
            time.sleep(2.4)
            f = open(LOG_FILE, LOG_TYPE)
            f.write(LOG_MSG)
            f.close()
            print(READ_LOG)
            time.sleep(EXIT_TIME)
            exit()
        else:
            print(FILE_DOESNT_EXIST)
            time.sleep(2.4)
            f = open(LOG_FILE, LOG_TYPE)
            f.write(LOG_MSG)
            f.close()
            print(READ_LOG)
            time.sleep(EXIT_TIME)
            exit()
    if logs == 2:
        time.sleep(EXIT_TIME)
        exit()
    if logs > 2:
        print("Internal error.")
        f = open("admin-log.txt", "a")
        f.write("Tryed to start program with logs value more than 2 or less than 1!\nPlease use values to disable, or enable the log system!\n \nPlease check SETTINGS section at code! Example use:\n If you want to log your program: logs = 1\n If else: logs = 2")
        f.close()
        print("Please check admin-log.txt file!")
        time.sleep(2)
        print("Force stop started..")
        exit()
    time.sleep(EXIT_TIME)
    exit()