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
"rofi", #Program Launcher
]


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

    os.system("sudo pacman --noconfirm -Syu | 1>/dev/null")
        

def basic_packages():
    print("[+]Installing basic packages...")
    os.system("sudo pacman --noconfirm -S xorg lightdm lightdm-gtk-greeter qtile base-devel brightnessctl | 1>/dev/null")

def paru():
    global username
    print("[+]Installing paru AUR helper...")
    os.system("sudo pacman --noconfirm -S rust | 1>/dev/null")
    os.system("sudo git clone https://aur.archlinux.org/paru.git /opt/paru")
    os.system("sudo chown {} /opt/paru".format(username))
    os.system("cd /opt/paru && makepkg -si --noconfirm && cd")

def extra_software():
    print("[+]Installing extra software...")
    #Audio
    os.system("sudo pacman --noconfirm -S pulseaudio pavucontrol | 1>/dev/null")

    #Systray applets
    os.system("sudo pacman --noconfirm -S volumeicon cbatticon network-manager-applet udiskie | 1>/dev/null")

    #Wallpaper
    os.system("sudo pacman --noconfirm -S feh | 1>/dev/null")
    
    for i in software:
        os.system("sudo pacman --noconfirm -S {} | 1>/dev/null".format(i))

def fonts():
    print("[+]Downloading fonts...")
    os.system("paru --noconfirm nerd-fonts-ubuntu-mono")

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
    os.system("sudo pacman --noconfirm -S python-psutil | 1>/dev/null")
    
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
    os.system("sudo pacman --noconfirm -S zsh | 1>/dev/null")
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
    basic_packages()
    paru()
    extra_software()
    fonts()
    config()
    nvidia()
    reboot()

main()