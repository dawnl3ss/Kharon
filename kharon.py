from src.enum.web_enum import web_enum
from src.tool_check import get_list, check_if_exist
from src.scan_loop import is_scan_complete
from src.utils.ascii import get_ascii
from src.utils.colors import colors
import time
import os
import sys

intensity_lev = None
complete = False
n = 1
report_asking = True
# shell_type = "bash" | set this var to 'bash' if you use bash shell env
shell_type = "zsh" # I personally use 'zsh'

def main():
    global intensity_lev, complete, n, shell_type, report_asking
    display_menu()
    list = get_list()
    sys.stdout.write('\33]0;Kharon - CTF Website Scanner\a')
    sys.stdout.flush()

    for tool in list:
        if check_if_exist(tool) == False:
            display_menu()
    addr = str(input("└──────⮞ IP-Address : "))

    display_menu()
    print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
    print("│")
    intensity_lev = int(input("└──────⮞ Scan intensity (1-3) : "))
    enum = web_enum(addr, intensity_lev, shell_type)

    enum.nmap_scan()
    enum.gobuster_scan()
    enum.nikto_scan()

    while complete != True:
        display_menu()
        do_graphic_loop(addr)
        if is_scan_complete(addr, intensity_lev):
            complete = True
        time.sleep(1)

    while report_asking:
        display_menu()
        print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
        print("│")
        print("├─" + colors.FAIL + "⮞" + colors.WARNING + " Scan intensity : {}".format(intensity_lev))
        print("│")
        report = input("└──────⮞ Choose report (nmap, gobuster, nikto, q) : ")

        if report in ("nmap", "gobuster", "nikto"):
            display_menu()
            print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
            print("│")
            print("├─" + colors.FAIL + "⮞" + colors.WARNING + " Scan intensity : {}".format(intensity_lev))
            print("│")
            print("├─" + colors.FAIL + "⮞" + colors.WARNING + " App report : {}".format(report))
            print("│")
            file = open(f"ressources/output/{report}-{addr}-{intensity_lev}.txt", "r")

            for file_line in file.readlines():
                print("│ " + file_line, end='')
            file.close()
            print("│")
            quit = input("└──────⮞ Press (q) to quit : ")
        elif report == 'q':
            print("")
            print(colors.FAIL + "💀" + colors.WARNING + " Closing Kharon... Bye !")
            report_asking = False
        else:
            continue

def display_menu():
    os.system("clear")
    print(colors.FAIL+ "💀" + colors.WARNING + " Starting Kharon...")
    print(colors.OKORANGE + get_ascii())
    print(colors.FAIL + "💀" + colors.WARNING + " Basic & automated Web-Server CTF enumeration.")
    print("┌──────────────────────────────────────────────────")
    print("│")

def do_graphic_loop(addr):
    global intensity_lev, n
    print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
    print("│")
    print("├─" + colors.FAIL + "⮞" + colors.WARNING + " Scan intensity : {}".format(intensity_lev))
    print("│")
    if n == 1:
        print("└──────⮞ Scan Started ...")
        n += 1
    elif n == 2:
        print("└──────⮞ Scan Started #..")
        n += 1
    elif n == 3:
        print("└──────⮞ Scan Started .#.")
        n += 1
    elif n == 4:
        print("└──────⮞ Scan Started ..#")
        n = 1

    
if __name__ == "__main__":
    main()