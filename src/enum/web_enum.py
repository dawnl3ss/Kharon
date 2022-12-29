from src.shell.fake_shell import fake_shell
import os

def nmap_scan(addr, intensity):
    fake = fake_shell(f"NMAP Scan - {addr} - Kharon", os.getcwd())
    fake.set_command(f"nmap -A {addr} -oN ressources/output/nmap-{addr}-{intensity}.txt")
    fake.append_command(f"echo kharon_scan_complete >> ressources/output/nmap-{addr}-{intensity}.txt")
    return os.system(fake.make())

def gobuster_scan(addr, intensity):
    fake = fake_shell(f"Gobuster Scan - {addr} - Kharon", os.getcwd())
    fake.set_command(f"gobuster dir -u http://{addr} -w ressources/wordlists/dir-enum-int-{intensity}.txt -o ressources/output/gobuster-{addr}-{intensity}.txt")
    fake.append_command(f"echo kharon_scan_complete >> ressources/output/gobuster-{addr}-{intensity}.txt")
    return os.system(fake.make())
