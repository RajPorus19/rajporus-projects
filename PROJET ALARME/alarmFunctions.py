import datetime as dt
import os,time,sys

def launchAlarm():
    tuple1 = timeStamps()
    while True:
        t0 = dt.datetime.now().isoformat()
        time2 = t0.split('T')
        if time2[1].startswith(tuple1):
            if str(dt.datetime.now().weekday()) in list(readSettings()[2][1].split(',')) == True:
                time.sleep(int(readSettings()[0][1]))
                continue
            startAlarm(int(readSettings()[0][1]))
            continue
        
def startAlarm(sec):
    os.startfile(readSettings()[1][1])
    time.sleep(int(sec))
    os.system("taskkill /f /im "+readSettings()[3][1])

def readSettings():
    textFile = open("settings.txt","r")
    liste1 = textFile.read().split('\n')
    liste2 = []
    textFile.close()
    for i in liste1:
        liste2.append(list(i.split('=')))
    return(liste2) 

def timeStamps():
    text = open("times.txt","r")
    tuple1 = tuple(text.read().split(" "))
    text.close()
    return(tuple1)

def addTime():
    num = input("Quel horaire voulez vous ajouter ? (Utiliser le format heure:minute:secondes. ==> 08:20:00.): ")
    text = open("times.txt","r")
    newTime = text.read() + " " + num
    text.close()
    text = open("times.txt","w")
    text.write(newTime.strip())
    text.close()
    
def removeTime():
    x = 0
    timeDisplay = ""
    for i in timeStamps():
        timeDisplay += "["+str(x)+"]"+" "+str(i)
        x+=1
    print(timeDisplay)
    x2 = int(input("Quel horaire voulez vous supprimer ? (Entrez la le nombre entre crochets correspondant à l’horaire que vous voulez retirer): "))
    word = ''
    for i in timeStamps():
        if i == timeStamps()[x2]:
            continue
        word += str(i) + " "
    word = word.strip()
    text = open("times.txt","w")
    text.write(word.strip())
    text.close()

