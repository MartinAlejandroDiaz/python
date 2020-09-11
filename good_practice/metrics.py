import os
dir = './dump/'
contentFiles = os.listdir(dir)
list = []
def getFiles(type):
    for file in contentFiles:
        if os.path.isfile(os.path.join(dir, file)) and 
            file.endswith(type):
            list.append(file)
    print(list)