import json
import os
import sys

addr = sys.argv[1]
intensity = sys.argv[2]

file = json.load(open(f"ressources/output/{addr}-{intensity}/ffuf.txt"))
temp = open(f"ressources/output/{addr}-{intensity}/temp-ffuf.txt", "a")

for res in file["results"]:
    temp.write(res["url"] + " : [" + str(res["status"]) + "]\n")
temp.close()
os.system(f"rm ressources/output/{addr}-{intensity}/ffuf.txt")
os.system(f"mv ressources/output/{addr}-{intensity}/temp-ffuf.txt ressources/output/{addr}-{intensity}/ffuf.txt")