# ActiveInfoGathering
#PenTesting Class
Nmap, NetCat and OpenVas

Active information gathering is the process in which occurs direct interaction with the system to learn about it using tools specifically designed to analyze the target.
The information obtained covers from state of the ports, OS version, services running, banner grabbing, active hosts, and/or vulnerabilities in the applications.
It is useful to automate the tools, in order to make the process of obtaining information more efficient, saving time to  the person in charge of performing this task, 
due to the repetitive approach that can be involved. 
The code was made using Python, due to the facilities it offers. In this case using libraries that come by default with the installation of the programming language. 
Needles to say, is necessary to have python installed on the system. 
To run the program, the code must be saved as a .py file. It can be run by opening and running it from an IDE such as PyCharm, or from the console. 
For this last method it is necessary to open the console and go to the location of the program. Then, execute:
> python [name of the script].py
The script uses the path to a folder where the results of the tools will be stored in individual text files, allowing the user to
clearly visualize the information pertaining to each one. This path must be present in the system (the text files will be created automatically in case they don’t exist),and 
the program needs to have permission to access the locations specified. 
The automated tools used were nmap and netcat. This was done through a script in which there is interaction with the user. 
The program will prompt the user to enter whether to use nmap or netcat. This is because the first one is a tool that can produce more noise on the network 
compared to the latter. The user is also offered the opportunity to do both, because repeatedly, until he/she indicates the desire to finish the program,
it will be asked whether he/she wants to implement nmap or netcat. It is a mechanism that also allows the tools to be used in different IP ranges,
without having to execute the program again.
The perspective is that this process will be carried out to obtain information about the objectives with some recurrence, 
so two text files will have the information and, each time the program is executed, the information in them will be updated. 
If, according to the user's needs, it is required to archive the results each time, it can be easily modified in the code.
In the case of OpenVAS, it is not necessary to automate it through a script, as Greenbone offers the Security Assistant, 
which offers the possibility to schedule vulnerability scans against specified targets on a scheduled basis. 
This schedule can be hourly, daily, weekly, monthly, etc. or it can be with a recurrence specified by the user, according to the needs.
