# Import the needed libraries.
import ipaddress  # Allows us to handle IP addresses in its original format.
import datetime
import subprocess

# Variables are declared.
# Location 1 and Location 2 are the two text files where the results will be stored.
# The program needs to have permission to access those locations.
location1 = "/home/andreidysa/Documents/Programs/Results/Nmap.txt"  # Nmap
location2 = "/home/andreidysa/Documents/Programs/Results/Netcat.txt"  # Netcat
module = " 0 "  # Variable declared to store the user's option.


# Nmap function. It receives the first and the last IP of the range the user wants.
# If it is just one, the user needs to enter the same IP for both.
def nmap_cmd(first_ip, last_ip):
    timedate = datetime.datetime.now()  # Current date and time when the function is being executed.
    timedate = str(timedate)  # Converted to string.
    # Next, the file for nmap is opened. If it doesn't exist, it will be automatically created.
    file = open(location1, "w")  # In write mode, to erase results from previous executions.
    file.write("Results: " + timedate + '\n\n')  # Add the date and time to the file.
    file.close()  # Good practice.

    if first_ip == last_ip:  # If both IPs are the same, then the user just wants to scan one target.
        # The file is open again in "append" mode, to add the results respective to the current date and time.
        file = open(location1, "a")
        # Subprocess is used to send a command to the system.
        # First, it concatenates the received IP to execute the nmap command.
        # Then, the output of the command is passed to 'sed' to extract from line 5 to the next blank line.
        # It will use the user's shell, and the output will be directed to the file previously opened.
        subprocess.run(f"nmap {first_ip} -sV| sed -n '5,/^$/p'", shell=True, stdout=file)
        file.close()  # Good practice.

    if first_ip != last_ip:  # If the received IPs are different, then it is a range.
        # The file is open again in "append" mode, to add the results respective to the current date and time.
        file = open(location1, "a")
        # Because it is a range, a for loop is necessary to analyze all the IPs between the first and the last.
        # Add 1 to the last IP so that the for can evaluate the IP entered by the user as the last one.
        # The for evaluates between values.
        # If the 1 is not added, it will evaluate only up to the IP before the desired one.
        for ip in range(int(first_ip), int(last_ip+1)):
            ip = ipaddress.ip_address(ip)  # IP so far is just a number. So it is converted to IPv4 format.
            subprocess.run(["echo", f"IP: {ip}"], stdout=file)  # A command is sent to print the current IP in the file.
            # As previously explained, the output of the command is passed to 'sed' to extract the wanted parts.
            # It will use the user's shell, and the output will be directed to the file previously opened.
            subprocess.run(f"nmap {ip} -sV| sed -n '5,/^$/p'", shell=True, stdout=file)

        file.close()  # Good practice.


def netcat(first_ip, last_ip, ports):
    # As explained above, the date and time at which the function is being executed is obtained.
    # Then it is written into the file, deleting previous information in it.
    timedate = datetime.datetime.now()
    timedate = str(timedate)
    file = open(location2, "w")
    file.write("Results: " + timedate + '\n\n')
    file.close()
    if first_ip == last_ip:  # If it's just one IP
        # The file is open again in "append" mode, to add the results respective to the current date and time.
        file = open(location2, "a")
        # The nc (netcat) command is sent, using the user's shell, with the different flags to use.
        # Also, the IP and the ports the user want to analyze are specified.
        # Generally, nc is used to connect remotely through a port.
        # nc is generally used to connect remotely through a port.
        # So the stdoutput is not exactly what is required in this command, but the ports' information.
        # That is diagnostic information that netcat stores in stderr. So stderr results are sent to the file.
        # Text = true means that the output will be string.
        subprocess.run(["nc", "-v", "-n", "-z", "-w1", str(first_ip), ports], stderr=file, text=True)
        file.close()  # Good practice.
    if first_ip != last_ip:
        file = open(location2, "a")  # The file is opened to append the results.
        # AS previously explained, a for loop is used to analyze all the IPs in the range.
        # And the one is added to include the last IP entered by the user.
        for ip in range(int(first_ip), int(last_ip+1)):
            ip = ipaddress.ip_address(ip)  # Convert to IP format.
            subprocess.run(["echo", f"IP: {ip}"], stdout=file) # A command is sent to print the current IP in the file.
            # As mentioned before, the command is sent with the IP being analyzed at the moment, the respective flags,
            # and the ports.
            subprocess.run(["nc", "-v", "-n", "-z", "-w1", str(ip), ports], stderr=file, text=True)

        file.close()  # Good practice.


while module != "3":  # 3 is the option to end the program. If the user doesn't want to end it,
    # it will be asked what to do.
    # The options are: nmap, netcat (less noisy than nmap), and exit.
    module = input("\nEnter your option\n1) NMAP\n2) NetCat\n3) Exit\n\nOption: ")

    if module == "1":
        # If the user selects 1, the program will ask about the targets.
        start_ip = input("Enter the starting IP address: ")  # First IP of the range
        end_ip = input("Enter the final IP address: ")  # Last IP of the range.
        # If it is just one IP, the user will enter the same IP both times.
        # Next, the strings received are converted to IP format.
        start_ip = ipaddress.ip_address(start_ip)
        end_ip = ipaddress.ip_address(end_ip)
        nmap_cmd(start_ip, end_ip)  # nmap is called.

    if module == "2":
        # If the user selects 1, the program will ask about the targets.
        start_ip = input("Enter the starting IP address: ")  # First IP of the range.
        end_ip = input("Enter the final IP address: ")  # Last IP of the range.
        ports = input("Enter the port or port range (E.g.,100-1000): ")  # Ports to scan.
        # Next, the strings received are converted to IP format.
        start_ip = ipaddress.ip_address(start_ip)
        end_ip = ipaddress.ip_address(end_ip)

        netcat(start_ip, end_ip, ports)  # netcat function is called.

    if module == "3":
        # If the user selects 3, it means to end the program.
        exit()
    # If the option entered is different from the ones allowed, the user will be informed.
    if module not in ["1", "2", "3"]:
        print("Option not valid")

# Greenbone Security Assistant provides the opportunity of scheduled OpenVAS scans.
# For this, click "Scans" > "Tasks" > "New Task" 
# Specify the corresponding information and, in the Schedule field, select "New Schedule" 
# This option allows to specify a name, Timezone, time when it will be run for the first time, 
# and also provides the option to leave an open end until it finishes on its own or to give a duration to the scan. 
# Also, you can select a recurrence or to customize one. 
# The report will be automatically generated.
