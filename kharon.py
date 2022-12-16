from src.utils.ascii import get_ascii
from src.utils.colors import colors
from src.tool_check import get_list, check_if_exist
import os

def main():
    display_menu()
    list = get_list()

    for tool in list:
        if check_if_exist(tool) == False:
            display_menu()
    addr = str(input("└──────⮞ IP-Adress : "))

def display_menu():
    os.system("clear")
    print(colors.FAIL+ "💀" + colors.WARNING + " Starting Kharon...")
    print(colors.OKORANGE + get_ascii())
    print(colors.FAIL + "💀" + colors.WARNING + " Basic & automated Web-Server CTF enumeration.")
    print("┌──────────────────────────────────────────────────")
    print("│")
    
if __name__ == "__main__":
    main()