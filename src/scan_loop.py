import os

def is_scan_complete(addr, intensity_lev):
    statements = []

    if os.path.exists(f"ressources/output/gobuster-{addr}-{intensity_lev}.txt"):
        gobuster = open(f"ressources/output/gobuster-{addr}-{intensity_lev}.txt", "r")

        for gb_line in gobuster.readlines():
            if "kharon_scan_complete" in gb_line:
                statements.append(True)
        gobuster.close()

    if os.path.exists(f"ressources/output/nmap-{addr}-{intensity_lev}.txt"):
        nmap = open(f"ressources/output/nmap-{addr}-{intensity_lev}.txt", "r")

        for nmap_line in nmap.readlines():
            if "kharon_scan_complete" in nmap_line:
                statements.append(True)
        nmap.close()

    return statements.count(True) == 2