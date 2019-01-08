import os
import subprocess

pacman = "pacman"
emerge = "emerge"
zypp = "zypp"
apt = "apt-get"
yum = "yum" 
def get_pakage_name():
    pakage = subprocess.run("./pkgi.sh",
                            shell=True, stdout=subprocess.PIPE)
    pName = str(pakage.stdout.decode("utf-8")).strip()
    return pName


def get_os_info():

    pName = get_pakage_name()
    os_info = os.uname()

    return {"pakageName": pName, "sysname": os_info[0],
            "release": os_info[2], "version": os_info[3],
            "machine": os_info[4]}


def get_pakage_installed_list():
    Pname = get_pakage_name()
    # manjaro
    if Pname == "pacman":
        print("pacman")
        p = subprocess.run("pacman -Q",
                           shell=True, stdout=subprocess.PIPE)
        installed_pkg = str(p.stdout.decode("utf-8")).strip()
        print(installed_pkg)

    #Fedora
    elif Pname == "yum":
        pass
    #gentoo
    elif Pname == "emerge":
        pass
    #OpenSUSE
    elif Pname == "zypp":
        pass
    #debian
    elif Pname == "apt-get":
        pass
    else :
        return("Error: Pakage Manager not found")

print(get_pakage_installed_list())
