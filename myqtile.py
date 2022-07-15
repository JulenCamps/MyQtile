#! /bin/python3
#JulenCamps
#https://github.com/julencamps/myqtile

import os

from sofware.software import essential, extra, aur

print(
"""              
 __  __                ___    _     _   _
|  \/  |  _   _       / _ \  | |_  (_) | |   ___
| |\/| | | | | |     | | | | | __| | | | |  / _ \ 
| |  | | | |_| |     | |_| | | |_  | | | | |  __/ by JulenCamps
|_|  |_|  \__, |      \__\_\  \__| |_| |_|  \___|
          |___/    
"""
)


def hello():
    global username
    
    #Detect if the user is running the script as root
    uid = os.getuid()
    username = os.getlogin()

    if uid == 0:
        print("Warning: Do not run this script as root. It is dangerous!")
        quit()
    else:
        pass

    #Update the system
    os.system("sudo pacman --noconfirm -Syu | 1>/dev/null")
        

def software_installation():
    print("[+]Installing all the necessary software...")
    
    for i in essential:
        os.system("sudo pacman --noconfirm -S {} > /dev/null 2>&1".format(i))

    for i in extra:
        os.system("sudo pacman --noconfirm -S {} > /dev/null 2>&1".format(i))

    for i in aur:
        os.system("paru --noconfirm -S {} > /dev/null 2>&1".format(i))

def paru():
    global username
    print("[+]Compiling paru AUR helper...")
    os.system("sudo pacman --noconfirm -S rust | 1>/dev/null")
    os.system("sudo git clone https://aur.archlinux.org/paru.git /opt/paru")
    os.system("sudo chown {} /opt/paru".format(username))
    os.system("cd /opt/paru && makepkg -si --noconfirm && cd")


def config():
    global username

    print("[+]Configuring the system...")
    
    #Clone config_files in "$HOME"
    os.system("git clone https://github.com/JulenCamps/config_files.git ~/config_files | 1>/dev/null")
    #Create needed directories
    os.system("mkdir -p ~/.config")

    #Qtile
    os.system("cp -r ~/config_files/.config/qtile ~/.config")
    os.system("chmod {} +x ~/.config/qtile/autostart.sh".format(username))
    
    #Alacritty
    os.system("cp -r ~/config_files/.config/alacritty ~/.config")

    #Autostart
    os.system("cp ~/config_files/.xsession ~/")
    os.system("sudo chmod +x ~/.xsession")

    #Lightdm
    os.system("sudo systemctl enable lightdm")

    #Rofi 
    os.system("sudo cp -r ~/config_files/.config/rofi ~/.config")

    #zsh
    os.system("sudo chsh -s /usr/bin/zsh {}".format(username))
    os.system("sudo cp ~/config_files/.zshrc ~/")


def nvidia():
    nvidia = input("Do you want to install the nvidia propietary drivers?[y/N]")

    if nvidia == "Y" or nvidia == "y":
        print("[+]Installing the nvidia propietary driver...")
        os.system("sudo pacman --noconfirm -S nvidia | 1>/dev/null")
        
        optimus = input("Do you want to install optimus-manager?[y/N]")

        if optimus == "Y" or optimus == "y":
            print("[+]Installing optimus manager...")
            os.system("paru --noconfirm optimus-manager optimus-manager-qt")
        else:
            pass

    else:
        pass


def reboot():
    reboot = input("Do you want to reboot the system now?[Y/n]")

    if reboot == "Y" or reboot == "y" or reboot == "":
        os.system("reboot")
    else:
        pass


def main():
    hello() 
    software_installation()
    paru()
    nvidia()
    config()
    reboot()


main()