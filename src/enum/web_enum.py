from src.shell.fake_shell import fake_shell
import os

class web_enum():

    def __init__(self, addr, intensity, terminal_type):
        self.addr = addr
        self.intensity = intensity
        self.terminal_type = terminal_type

    def nmap_scan(self):
        shell = fake_shell(f"NMAP Scan - {self.addr} - Kharon", os.getcwd(), self.terminal_type)

        if self.intensity == 1:
            shell.set_command(f"nmap -A {self.addr} -oN ressources/output/{self.addr}-{self.intensity}/nmap.txt")
        elif self.intensity == 2:
            shell.set_command(f"nmap -p 1-20000 -A {self.addr} -oN ressources/output/{self.addr}-{self.intensity}/nmap.txt")
        elif self.intensity == 3:
            shell.set_command(f"nmap -p- -A {self.addr} -oN ressources/output/{self.addr}-{self.intensity}/nmap.txt")

        shell.append_command(f"echo kharon_scan_complete_nmap >> ressources/output/{self.addr}-{self.intensity}/completed.txt")
        return os.system(shell.make())
    
    def ffuf_scan(self):
        shell = fake_shell(f"Ffuf Scan - {self.addr} - Kharon", os.getcwd(), self.terminal_type)
        shell.set_command(f"ffuf -u http://{self.addr}/FUZZ -w ressources/wordlists/dir-enum-int-{self.intensity}.txt -o ressources/output/{self.addr}-{self.intensity}/ffuf.txt -c")
        shell.append_command(f"echo kharon_scan_complete_ffuf >> ressources/output/{self.addr}-{self.intensity}/completed.txt")
        shell.append_command(f"python src/enum/ffuf_json_converter.py {self.addr} {self.intensity}")
        return os.system(shell.make())
    
    def nikto_scan(self):
        shell = fake_shell(f"Nikto Scan - {self.addr} - Kharon", os.getcwd(), self.terminal_type)
        shell.set_command(f"nikto -host {self.addr} -output ressources/output/{self.addr}-{self.intensity}/nikto.txt")
        shell.append_command(f"echo kharon_scan_complete_nikto >> ressources/output/{self.addr}-{self.intensity}/completed.txt")
        return os.system(shell.make())