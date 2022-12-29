from src.enum.web_enum import nmap_scan, gobuster_scan
from src.tool_check import get_list, check_if_exist
from src.scan_loop import is_scan_complete
from src.utils.ascii import get_ascii
from src.utils.colors import colors
import time
import os

intensity_lev = None
complete = False
n = 1

def main():
    global intensity_lev, complete, n
    display_menu()
    list = get_list()

    for tool in list:
        if check_if_exist(tool) == False:
            display_menu()
    addr = str(input("└──────⮞ IP-Address : "))
    
    display_menu()
    print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
    print("│")
    intensity_lev = int(input("└──────⮞ Scan intensity (1-3) : "))

    nmap_scan(addr, intensity_lev)
    gobuster_scan(addr, str(intensity_lev))

    while complete != True:
        display_menu()
        do_graphic_loop(addr)
        if is_scan_complete(addr, intensity_lev):
            complete = True
        time.sleep(1)

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