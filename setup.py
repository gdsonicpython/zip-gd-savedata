import os
from datetime import datetime

gdsavelocation = "C:\\Users\\cooper\\AppData\\Local\\GeometryDash"
lastestfilelocation = "C:\\Users\\cooper\\AppData\\Local\\GeometryDash\\latestfile.txt"

os.chdir(gdsavelocation)

os.system("mkdir savedata.old")



now = datetime.now()
now = str(now)
now = now.replace(":", "-")

os.system(f'tar -a -c -f "savedata { now }.zip" *.dat')

data = [f"savedata { now }.zip\n", "DO NOT CHANGE THIS FILE!!!"]

os.system("echo > latestfile.txt")

with open(lastestfilelocation, "+w") as file:
        file.writelines(data)

os.remove(f"{os.getcwd()}\\setup.py")