import os

def nmap_scan(addr, intensity):
    return os.system(f"mate-terminal -e \"nmap -A {addr}\" -t \"NMAP Scan - {addr} - Kharon\"")

def gobuster_scan(addr, intensity):
    current = os.getcwd()
    wl = f"ressources/wordlists/dir-enum-int-{intensity}.txt"
    return os.system(f"mate-terminal --working-directory={current} -e 'gobuster dir -u http://{addr} -w {wl}' -t 'Gobuster Scan - {addr} - Kharon'")
