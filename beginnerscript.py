#*************************************#
#                                     #       
#   Admin System Control              #
#   Version 1.1.3.1                   #
#   prezident                         #
#   Modified NOV 05-06, 2011          #
#                                     #
#*************************************#                                 
"""
Admin System Control  - Admin System Control 
Copyright (C) 2004-2011 prezident 

Admin System Control  is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Admin System Control  is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
#!/usr/bin/python
#filename:beginnerscript.py

import subprocess

def showoptions():
    print("SYSTEM ADMIN PANEL 3.1.1")
    print("BACK UP EVERYTHING BEFORE YOU LOSE EVERYTHING! - CODE 200")
    print("RUN SCRIPT AS ROOT CODE 200")
    print("")
    print("1 - Quit\t\t2 - Delete a file")
    print("3 - Show disk info\t4 - release")
    print("5 - List Dir\t\t6 - Update")
    print("7 - uname\t\t8 - Cat") 
    print("9 - Install\t\t10 - Start Up")
    print("11 - Add Repository\t12 - Reboot")
    print("13 - Top\t\t14 - pwd")
    print("15 - Wget\t\t16 - usb")
    print("17 - lshw\t\t18 - whoami")
    print("19 - Nano\t\t20 - uptime")
    print("21 - autoclean\t\t22 - crontab")
    print("23 - du\t\t\t24 - free")
    print("25 - dpkg\t\t26 - ps")
    print("27 - kill\t\t28 - mount")
    print("29 - lsusb\t\t30 - ifconfig")
    print("31 - iwconfig\t\t32 - networking")
    print("33 - usb\t\t34 - kernels")
    print("35 - last\t\t36 - macAddress")
    print("37 - Volume\t\t38 - Suspend")
    print("100 - MSG\t\t101 - Shutdown")
    print("")

def deletefile():
    """2 deletefile - Deletes a file or directory you specify"""
    subprocess.call("ls", shell=True)
    filename = raw_input("Enter The Filename You Want to Delete: ")
    result = subprocess.call("rm -vr " + filename, shell=True)

def diskinfo():
    """3 diskinfo estimate disk space in human readable format"""
    subprocess.call("df -h", shell=True)

def release():
    """4 lsb_release prints specific distribution information"""
    subprocess.call("lsb_release -a", shell=True)    
 
def listopt():
    """5 listopt list the files, filesize, modified date, file ownership in the current directory """
    subprocess.call("ls -ltcshaF", shell=True)

def update():
    """6 update and upgrade the system"""
    subprocess.call("sudo apt-get update && sudo apt-get upgrade", shell=True)

def uname():
    """7 cpuinfo - prints system information"""	
    subprocess.call("uname -a", shell=True)

def cat():
    """8 cat concatenate and prints on standard output reads files"""
    subprocess.call("ls", shell=True)
    filename = raw_input("Please Enter the filename you want to cat: ")
    subprocess.call("cat " + filename, shell=True)

def install():    
    """9 install an application on to the system"""
    filename = raw_input("Enter Filename: ")
    result = subprocess.call("sudo apt-get install " + filename, shell=True)

def startup():
    """10 startup - organize items that start up upon login"""
    subprocess.call("gnome-session-properties&", shell=True)

def repo():
    """11 repo add a repository to the source.list"""
    repolist = raw_input("Please Enter Repository: ")
    result = subprocess.call("sudo add-apt-repository ppa: " + repolist, shell=True)

def reboot():
    """12 reboot the system"""
    subprocess.call("sudo reboot", shell=True)
    
def top():
    """13 top - displays linux task - shows you what is running on the system"""
    subprocess.call("top", shell=True)

def pwd():
    """14 pwd - shows your current directory"""
    subprocess.call("pwd", shell=True)

def wget():
    """15 wget - use to download a website"""
    web = raw_input("Enter Website: ")
    result = subprocess.call("wget " + web, shell=True)

def usb():
    """16 usb - shows you all current devices connected to your computer"""
    subprocess.call("lsusb", shell=True)
      
def lshw():
    """17 lshw - give detail information on the hardware configuration"""
    subprocess.call("lshw -json", shell=True)
    
def who():
    """18 who - shows you who is logged on and what there doing"""
    subprocess.call("w", shell=True)
    subprocess.call("who am i", shell=True)

def nano():
    """19 nano - A terminal text editor"""
    subprocess.call("nano", shell=True)
 
def uptime():
    """20 uptime - tell how long the system has been running"""
    subprocess.call("uptime", shell=True)

def autoclean():
    """21 autoclean - cleans files no longer needed"""
    subprocess.call("sudo apt-get autoclean", shell=True)

def crontab():
    """22 crontab - allows you to schedule task"""
    subprocess.call("crontab -e", shell=True)
   
def du():
    """23 du - estimate file space usage"""
    subprocess.call("du -sh", shell=True)
    
def free():
    """24 free - display amount of free and used memory on the system"""
    subprocess.call("free -m", shell=True)

def dpkg():
    """25 dpkg - shows a list of packages on the system"""
    subprocess.call("dpkg -l | less", shell=True)

def ps():
    """26 ps - shows a snapshot of current process"""
    subprocess.call("ps -e | less", shell=True)

def kill():
    """27 kill - send a kill signal to an applications"""
    subprocess.call("ps -e; echo Enter PID to KILL: ; read id ; ps -e | grep $id; kill $id > /dev/null 2>&1", shell=True)
    
def mount():
    """28 mount - mount a filesystem"""
    subprocess.call("mount", shell=True)
    
def usb():
    """29 usb - list usb devices"""
    subprocess.call("lsusb", shell=True)
    
def iwconfig():
    """30 iwconfig - configure a wireless interface"""
    subprocess.call("iwconfig", shell=True)
    
def ifconfig():
    """31 ifconfig - configure your network interfaces"""
    subprocess.call("ifconfig", shell=True)
    
def network():
    """32 network - starts the network use only if your network is down."""
    subprocess.call("service networking start > /dev/null 2>&1", shell=True)

def backup():
    """33 backup - enter your backup drive/dir"""
    subprocess.call("") //put your backup script here

def kernel():
    """34 kernel - shows a list of linux image kernels on the system"""    
    subprocess.call("dpkg -l linux-image*", shell=True)

def last():
    """35 last time you logged on to the system"""
    subprocess.call("last -F | less", shell=True)

def macAddress():
    """36 macAddress - list macAddresses stored in the system"""
    subprocess.call("cat /sys/class/net/*/address | sort -u", shell=True)

def volume():
    """ 37 Volume - Sets the volume"""
    vol = raw_input("Please Enter Volume Number: ")        
    subprocess.call("amixer set Master " + vol + "%", shell=True)
    print("Volume set to " + vol + "%")

def suspend():
    """ 38 - Suspends system"""
    subprocess.call("sudo pm-suspend", shell=True)
    
def msg():
    """100 - Always Remember To BackUp System!!!"""
    print("BACK UP EVERYTHING BEFORE YOU LOSE EVERYTHING CODE 32") 

def shutdown():
    """101 shutdown"""
    subprocess.call("sudo init 0", shell=True)

def sudo():
    """200 sudo - run this script as a superuser"""
    subprocess.call("sudo python codeprez.py", shell=True)
       
x='0'

while (x != '1'):
    subprocess.call("clear", shell=True)
    showoptions()
    x = raw_input("Enter your choice: ").lower()

    if (x == '2' or x == "delete"):
        deletefile()
    elif (x == '3' or x == "diskinfo"):
        diskinfo()
    elif (x == "4" or x == "release"):
        release()
    elif (x == '5' or x == "ls"):
        listopt()
    elif (x == '6' or x == "update"):
        update()
    elif (x == '7' or x == "uname"):
        uname()
    elif (x == '8' or x == "cat"):
        cat()
    elif (x == '9' or x == "install"):
        install()
    elif (x == '10' or x == "startup"):
        startup()
    elif (x == '11' or x == "repo"):
        repo()
    elif (x == '12' or x == "reboot"):
        reboot()
    elif (x == '13' or x == "top"):
        top()
    elif (x == '14' or x == "pwd"):
        pwd()
    elif (x == '15' or x == "wget"):
        wget()
    elif (x == '16' or x == "usb"):
        usb()
    elif (x == '17' or x == "lshw"):
        lshw()
    elif (x == '18' or x == "who"):
        who()
    elif (x == '19' or x == "nano"):
        nano()
    elif (x == '20' or x == "uptime"):    
        uptime()
    elif (x == '21' or x == "autoclean"):
        autoclean()
    elif (x == '22' or x == "crontab"):
        crontab()
    elif (x == '23' or x == "du"):
        du()
    elif (x == '24' or x == "free"):
        free()
    elif (x == '25' or x == "dpkg"):
        dpkg()
    elif (x == '26' or x == "ps"):
        ps()
    elif (x == '27' or x == "kill"):
        kill()
    elif (x == '28' or x == "mount"):
        mount() 
    elif (x == '29' or x == "usb"):
        usb()
    elif (x == '30' or x == "ifconfig"):
        ifconfig()
    elif (x == '31' or x == "iwconfig"):
        iwconfig()
    elif (x == '32' or x == "network"):
        network()
    elif (x == '33' or x == "backup"):
        backup()
    elif (x == '34' or x == "kernel"):
        kernel()
    elif (x == '35' or x == "last"):
        last()
    elif (x == '36' or x == "mac"):
        macAddress()
    elif (x == '37' or x == "vol"):
        volume()
    elif (x == '38' or x == "suspend"):
        suspend()
    elif (x == '100' or x == "msg"):
        msg()
    elif (x == '101' or x == "shutdown"):
        shutdown()
    elif (x == '200' or x == "sudo"):
        sudo()
    else:
        showoptions()	
    print("Press Enter...")
    raw_input()
