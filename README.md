# Udemy: Cyber Security - Python and Web Applications

This course is taught by Mashrur Hossain and Evgeny Rahman on [Udemy](https://www.udemy.com/course/cyber-security-python-web-applications/). It is a only a good course if you are prepared to go beyond the course material to adapt it to your workflow and setup. For instance I didn't use the repl as in the videos, I used Atom and GitBash to run the scripts and I had to figure out why things weren't working which is more of a beneficial exercise as you are learning more than the material provided.

The course itself doesn't go into much detail on the actual scripting. It kind of just shows you what they do and you have to go off and reconfigure it to your own needs.

## Requirements
scapy
npcap

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
