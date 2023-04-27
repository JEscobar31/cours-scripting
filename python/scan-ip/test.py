import nmap
import socket

print("""
Option 1 : TCP Connect Scan
Option 2 : UDP Scan
Option 3 : Comprehensive Scan
Option 4 : OS Detection
Option 5 : Version Detection
Option 6 : Ping Scan
""")
input_user = input("Quel scan vous voulez faire [1-6] ?\n")
argument = ""
if input_user == "1":
    argument = "-sS"
elif input_user == "2":
    argument = "-sU"
elif input_user == "3":
    argument = "-sC"
elif input_user == "4":
    argument = "-O"
elif input_user == "5":
    argument = "-sV"
elif input_user == "6":
    argument = "-sP"

nm = nmap.PortScanner()
ip_site = socket.gethostbyname('jeremy057.pythonanywhere.com')
nm.scan(ip_site, arguments = argument)
info_nmap = nm[ip_site]
print(info_nmap)