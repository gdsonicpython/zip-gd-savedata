import os, time
from datetime import datetime

gdsavelocation = "C:\\Users\\cooper\\AppData\\Local\\GeometryDash"
lastestfilelocation = "C:\\Users\\cooper\\AppData\\Local\\GeometryDash\\latestfile.txt"
gdsavelocationold = "C:\\Users\\cooper\\AppData\\Local\\GeometryDash\\savedata.old"

os.chdir(gdsavelocation)

def removeold():
    os.chdir(gdsavelocationold)
    os.system("del *")
    os.chdir(gdsavelocation)
    os.system("cls")

def createzip():
    now = datetime.now()

    now = str(now)

    now = now.replace(":", "-")

    print("saved as: " + now + ".zip")

    with open(lastestfilelocation) as file:
        data = file.readlines()
    
    data[0] = data[0].replace("\n", "")
    
    print(f'MOVE "{data[0]}" "{gdsavelocationold}\\{data[0]}"')
    os.system(f'MOVE "{data[0]}" "{gdsavelocationold}\\{data[0]}"')

    os.system(f'tar -a -c -f "savedata { now }.zip" *.dat')
    data[0] = f"savedata { now }.zip\n"

    with open(lastestfilelocation, "+w") as file:
        file.writelines(data)
    
    os.system("cls")

def restorezip():
    with open(lastestfilelocation) as file:
        data = file.readlines()

    os.system(f'tar -xf "{ data[0] }"')
    os.system("cls")

while True:
    print("pls dont steal")
    ok = input("1> save your data\n2> restore your data\n3> remove old savedata\n> ")
    if ok == "1":
        createzip()
    elif ok == "2":
        restorezip()
    elif ok == "3":
        removeold()
    else:
        print("please input a valid choice")
        time.sleep(1)
        os.system("cls")