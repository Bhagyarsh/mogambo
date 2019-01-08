import os
import subprocess

class pacman:
    def __init__(self):
        pass

    def install(pakageName):
        cmd = "sudo pacman -S " + pakageName
        p = subprocess.run(cmd,
                           shell=True, stdout=subprocess.PIPE)
        output = str(p.stdout.decode("utf-8")).strip()
        return output
print(pacman.install("blender"))
