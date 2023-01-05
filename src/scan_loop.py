import os

def is_scan_complete(addr, intensity_lev):
    statements = []
    complete = []

    if os.path.exists(f"ressources/output/{addr}-{intensity_lev}/completed.txt"):
        file = open(f"ressources/output/{addr}-{intensity_lev}/completed.txt", "r")

        for f_line in file.readlines():
            if "kharon_scan_complete_nmap" in f_line:
                statements.append(True)
                complete.append("nmap")
            elif "kharon_scan_complete_ffuf" in f_line:
                statements.append(True)
                complete.append("ffuf")
            elif "kharon_scan_complete_nikto" in f_line:
                statements.append(True)
                complete.append("nikto")
        file.close()

    return (statements.count(True) == 3, complete)

