# Udemy: Cyber Security - Python and Web Applications

This course is taught by Mashrur Hossain and Evgeny Rahman on [Udemy](https://www.udemy.com/course/cyber-security-python-web-applications/). It's a very good course if you are prepared to go beyond the course material to adapt it to your workflow and setup. For instance I didn't use the repl as in the videos, I used Atom and GitBash to run the scripts and I had to figure out why things weren't working which is more of a beneficial exercise as you are learning more than the material provided. The course itself has a lot of great tips and tricks woven in and I really recommend taking it.  

I have a lot of files from the course in *.gitignore* because there are a lot of projects in the tutorials and I wanted to showcase those that made an impact on me and secondly, out of respect for the authors I didn't want to showcase their entire course in my Git repo. If you are interested in learning more about those not uploaded go check our their course in the link above.

## Requirements
Used a virtual environment to install certain libraries. Please see requirements.txt.

### network_traffic.py

Ran into an issue where the program wouldn't run. At first I thought it was an issue when using scapy on the Python virtual environment, but was still having the issue when I installed scapy on host machine.

So I then ran scapy in the terminal thinking I might have the wrong interface indicated, so I tried both *conf.route* and *conf.iface* and both came back with the same iface name. I dug around the [documentation](https://scapy.readthedocs.io/en/latest/introduction.htm) and wasn't able to find the appropriate solution.  

I thought there might be a problem with the compatibility using Python 3.8 as the notes suggest using up to Python 3.7, but I wasn't finding this issue anywhere else.

Finally, under [StackOverflow](https://stackoverflow.com/questions/49065489/scapy-sniff-doesnt-accept-the-iface-strings) I was able to narrow the problem further and identify that the issue was because there was a conflict between my windows computer version of npcap and the version I had through nmap. I resolved by uninstalling ncpap.dll and Packet.dll under Windows/System32 of my computer and installing the latest version of npcap.

Once I did that it worked perfectly. However, I could just do this on nmap with KaliLinux.

### wireless_finder.py

I do not have a Mac computer like the instructor so what I had to do was find my equivalent to his call command. I have a Windows, and what I discovered was that the AirPort utility that the instructor was using looked like a command line argument, and after digging around I discovered that I was right. So what I did was searched for some Git Bash command line arguments that would ultimately give me the same result. I discovered

```
call('netsh wlan show networks mode=Bssid')
```

I imported scapy so I could ensure that I was getting a more verbose response because when I tried this outside my virtual environment I didn't get the right response.

Resources:
[How to manage wireless networks using Command Prompt in Windows 10](https://www.windowscentral.com/how-manage-wireless-networks-using-command-prompt-windows-10)


### Log Analyzer

I completed this project as a report, because any log analysis would really be called using CLI. For instance, if I was to search for plain text passwords or passwords in a log file I would use the command:

```
 cat log_analyzer/original.log | grep 'password'| awk '{print$7}'
```

If I were to generate a report into a text file for myself or a supervisor than I could do:

```
 cat log_analyzer/original.log | grep 'password'| awk '{print$7}' > log_analyzer.txt
```

This is why I decided that it might be better to use Python to clean the data and make a more readable report. There are a lot of things you could do with the information, which is why I appreciated the freedom that this exercise gave. For instance, I originally submitted the project with the following code:

```
with open('log_analyzer/passcodes.txt', 'a') as write_log:
write_log.write('username,password,'+username +','+passphrase+',')
```
This was to be able to write the information to a text file and append that file as needed.

### Encryption

Module walks student through creating a program to encrypt a password. 

Reference:

https://developers.google.com/search/reference/robots_txt

last updated 5/8/2020
