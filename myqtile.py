#! /bin/python3
#JulenCamps
#https://github.com/julencamps/myqtile
#I'm not a professional programmer so don't expect support for
#this script. You are running it UNDER YOUR OWN RESPONSABILITY.

import os

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

software = [
"firefox", #Browser 
"alacritty", #Terminal
"picom", #Compositor
"libreoffice-fresh", #Office suit
"nemo", #File manager 
"vlc", #Video player
]


def hello():
    global username
    #Detect if the user is running the script as root
    uid = os.getuid()

    if uid == 0:
        print("Warning: Do not run this script as root user. It is dangerous!")
        quit()

    os.system("sudo pacman -Syu | 1>/dev/null")
    username = os.getlogin()    

def basic_packages():
    os.system("sudo pacman --noconfirm -S xorg lightdm lightdm-gtk-greeter qtile base-devel | 1>/dev/null")

def yay():
    global username
    os.system("sudo pacman --noconfirm -S go | 1>/dev/null")
    os.system("sudo mkdir /opt/yay")
    os.system("sudo git clone https://aur.archlinux.org/yay.git /opt/yay")
    os.system("sudo chown {} /opt/yay".format(username))
    os.system("cd /opt/yay && makepkg -si --noconfirm && cd")

def extra_software():
    #Audio
    os.system("sudo pacman --noconfirm -S pulseaudio pavucontrol | 1>/dev/null")

    #Systray applets
    os.system("sudo pacman --noconfirm -S volumeicon cbatticon network-manager-applet udiskie | 1>/dev/null")

    #Wallpaper
    os.system("sudo pacman --noconfirm -S feh | 1>/dev/null")
    
    for i in software:
        os.system("sudo pacman --noconfirm -S {} | 1>/dev/null".format(i))

def fonts():
    os.system("yay --noconfirm -S nerd-fonts-ubuntu-mono | 1>/dev/null")

def config():
    global username
    #Clone config_files in "$HOME"
    os.system("git clone https://github.com/JulenCamps/config_files.git ~/config_files | 1>/dev/null")
    #Create needed directories
    os.system("mkdir -p ~/.config")

    #Qtile
    os.system("cp -r ~/config_files/.config/qtile ~/.config")
    os.system("chmod {} +x ~/.config/qtile/autostart.sh".format(username))
    os.system("sudo pacman --noconfirm -S python-psutil | 1>/dev/null")
    
    #Alacritty
    os.system("cp -r ~/config_files/.config/alacritty ~/.config")

    #Autostart
    os.system("cp ~/config_files/.xsession ~/")
    os.system("sudo chmod +x ~/.xsession")

    #Lightdm
    os.system("sudo systemctl enable lightdm")

def reboot():
    reboot = input("Do you want to reboot the system now?[Y/n]")

    if reboot == Y or reboot == y:
        os.system("reboot")
    else:
        pass

def main():
    hello() 
    basic_packages()
    yay()
    extra_software()
    fonts()
    config()
    reboot()

main()