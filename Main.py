import ipaddress
import datetime
import subprocess

location1 = "/home/andreidysa/Documents/Programs/Results/Nmap.txt"
location2 = "/home/andreidysa/Documents/Programs/Results/Netcat.txt"
module = " 0 "


def nmap_cmd (start_ip, end_ip):

    timedate = datetime.datetime.now()
    timedate = str(timedate)
    file = open(location1, "w")
    file.write("Results: " + timedate + '\n\n')
    file.close()

    if start_ip == end_ip:
        file = open(location1, "a")
        subprocess.run(f"nmap {start_ip} | sed -n '5,/^$/p'", shell=True, stdout=file)
        file.close()


    else:

        end_ip = end_ip + 1
        file = open(location1, "a")
        for ip in range(int(start_ip), int(end_ip)):
            ip = ipaddress.ip_address(ip)
            subprocess.run(["echo", f"IP: {ip}"], stdout=file)
            subprocess.run(f"nmap {ip} | sed -n '5,/^$/p'", shell=True, stdout=file)

        file.close()


def netcat(start_ip, end_ip, ports):

    timedate = datetime.datetime.now()
    timedate = str(timedate)
    file = open(location2, "w")
    file.write("Results: " + timedate + '\n\n')
    file.close()
    if start_ip == end_ip:
        file = open(location2, "a")
        subprocess.run(["nc", "-v", "-n", "-z", "-w1", str(start_ip), ports], stderr=file, text=True)
        file.close()
    else:
        end_ip = end_ip + 1
        file = open(location2, "a")
        for ip in range(int(start_ip), int(end_ip)):
            ip = ipaddress.ip_address(ip)
            subprocess.run(["echo", f"IP: {ip}"], stdout=file)
            subprocess.run(["nc", "-v", "-n", "-z", "-w1", str(ip), ports], stderr=file, text=True)

        file.close()


while module != "3":

    module = input("\nEnter your option\n1) NMAP\n2) NetCat\n3) Exit\n\nOption: ")

    if module == "1":
        start_ip = input("Enter the starting IP address: ")
        end_ip = input("Enter the final IP address: ")
        start_ip = ipaddress.ip_address(start_ip)
        end_ip = ipaddress.ip_address(end_ip)
        nmap_cmd(start_ip, end_ip)

    if module == "2":
        start_ip = input("Enter the starting IP address: ")
        end_ip = input("Enter the final IP address: ")
        ports = input("Enter the port or port range (E.g.,100-1000): ")
        start_ip = ipaddress.ip_address(start_ip)
        end_ip = ipaddress.ip_address(end_ip)

        netcat(start_ip, end_ip, ports)

    if module == "3":
        exit()

    if module not in ["1","2","3"]:
        print("Option not valid")



