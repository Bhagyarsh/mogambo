import os
import subprocess

class apt:
    def __init__(self):
        pass

    def install(pakageName):
        cmd = "sudo apt-get install " + pakageName
        p = subprocess.run("",
                           shell=True, stdout=subprocess.PIPE)
        output = str(p.stdout.decode("utf-8")).strip()
        return output

print(apt.install("blender"))
