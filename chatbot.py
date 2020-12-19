from datetime import datetime
import webbrowser
import os,glob
chat = True
helloIntent = ["hi","hello","hey","hey buddy","hie"]
byeIntent = ["bye","good bye"]
dateIntent = ["date","show me the date","date please"]
timeIntent = ["time","show me the time","time please"]
dt=datetime.now()
musicIntent = ["music","play music"]
while chat:
    msg = input("Enter message :").lower()
    if msg in helloIntent:
        print("Hello Sir....")
    elif msg in dateIntent:
        print(dt.strftime("%d-%m-%y,%a"))
    elif msg in timeIntent:
        print(dt.strftime("%H-%M-%S,%p"))
    elif msg.startswith("open"):
        url = msg.split()[-1]+".com"
        webbrowser.open(url)
    elif msg in byeIntent:
        print("See you later..")
        chat = False
    elif msg in musicIntent:
        os.chdir('C:/Users/sahil/Downloads')
        fileList = glob.glob("*.mp3")
        print("Playlist")
        for i in range(len(fileList)):
            print(f"{i}--> {fileList[i]}")
        choice = int(input("enter music index"))
        os.startfile(fileList[choice])
    else:
        print("Sorry..i dont understand")
