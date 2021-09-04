#! /bin/python3

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
        print("Warning: Do not run this script as root user!")
        quit()

    os.system("sudo pacman -Syu")
    username = input("Introduce your system username: ")    

def basic_packages():
    os.system("sudo pacman -S install xorg lightdm lightdm-gtk-greeter qtile base-devel")

def yay():
    global username
    os.system("sudo mkdir /opt/yay")
    os.system("sudo git clone https://aur.archlinux.org/yay.git /opt/yay")
    os.system("sudo chown {} /opt/yay".format(username))
    os.system("cd /opt/yay")
    os.system("makepkg -si") ##REVIEW!!!!!
    os.system("cd ~/")

def extra_software():
    #Audio
    os.system("sudo pacman -S pulseaudio pavucontrol")

    #Systray applets
    os.system("sudo pacman -S volumeicon cbatticon network-manager-applet udiskie")

    #Wallpaper
    os.system("sudo pacman -S feh")
    
    for i in software:
        os.system("sudo pacman -S {}".format(i))

def fonts():
    os.system("yay -S ubuntu-mono-nerd-fonts")

def config():
    global username
    #Qtile
    os.system("cp -r ~/config_files/.config/qtile ~/.config")
    os.system("chmod {}+x ~/.config/qtile/autostart.sh".format(username))
    os.system("sudo pacman -S python-psutil")
    
    #Alacritty
    os.system("cp -r ~/config_files/.config/alacritty ~/.config")

    #Autostart
    os.system("cp ~/config_files/.xsession ~/")
    os.system("sudo chown +x ~/.xsession")

    #Lightdm
    os.system("sudo systemctl enable lightdm")


def main():
    hello() 
    basic_packages()
    yay()
    extra_software()
    fonts()
    config()

main()