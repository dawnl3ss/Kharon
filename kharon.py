from src.utils.ascii import get_ascii
from src.utils.colors import colors
import os

def main():
    display_menu()
    print("┌──────────────────────────────────────────────────")
    print("│")
    addr = str(input("└──────⮞ IP-Adress : "))

def display_menu():
    os.system("clear")
    print(colors.FAIL+ "💀" + colors.WARNING + " Starting Kharon...")
    print(colors.OKORANGE + get_ascii())
    print(colors.FAIL + "💀" + colors.WARNING + " Basic & automated Web-Server CTF enumeration.")

if __name__ == "__main__":
    main()