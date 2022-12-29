from src.shell.fake_shell import fake_shell
import os
    
class web_enum():

    def __init__(self, addr, intensity, shell_type):
        self.addr = addr
        self.intensity = intensity
        self.shell_type = shell_type
        
    def nmap_scan(self):
        shell = fake_shell(f"NMAP Scan - {self.addr} - Kharon", os.getcwd())
        shell.set_command(f"nmap -A {self.addr} -oN ressources/output/nmap-{self.addr}-{self.intensity}.txt")
        shell.append_command(f"echo kharon_scan_complete >> ressources/output/nmap-{self.addr}-{self.intensity}.txt")
        return os.system(shell.make())
    
    def gobuster_scan(self):
        shell = fake_shell(f"Gobuster Scan - {self.addr} - Kharon", os.getcwd())
        shell.set_command(f"gobuster dir -u http://{self.addr} -w ressources/wordlists/dir-enum-int-{self.intensity}.txt -o ressources/output/gobuster-{self.addr}-{self.intensity}.txt -x php,js,html,txt,py,sh")
        shell.append_command(f"echo kharon_scan_complete >> ressources/output/gobuster-{self.addr}-{self.intensity}.txt")
        return os.system(shell.make())
    
    def nikto_scan(self):
        shell = fake_shell(f"Nikto Scan - {self.addr} - Kharon", os.getcwd())
        shell.set_command(f"nikto -host {self.addr} -output ressources/output/nikto-{self.addr}-{self.intensity}.txt")
        shell.append_command(f"echo kharon_scan_complete >> ressources/output/nikto-{self.addr}-{self.intensity}.txt")
        return os.system(shell.make())
