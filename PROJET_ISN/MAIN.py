import tkinter,alarmFunctions,sys,os

master = tkinter.Tk()
master.geometry("300x300")
master.title("Alarme")

def choice1():
    display = tkinter.Label(master, text=alarmFunctions.timeStamps())
    display.pack()
    
def choice2():
    os.startfile("alarmLauncher.py")

def choice3():
    alarmFunctions.addTime()
    
def choice4():
    alarmFunctions.removeTime()
    
def choice5():
    sys.exit()
    
    

b1 = tkinter.Button(master, text="Horaires", command=choice1)
b1.pack()
b2 = tkinter.Button(master, text="Lancer l'alarme", command=choice2)
b2.pack()
b3 = tkinter.Button(master, text="Ajouter un horaire", command=choice3)
b3.pack()
b4 = tkinter.Button(master, text="Retirer un horaire", command=choice4)
b4.pack()
b5 = tkinter.Button(master, text="quitter", command=choice5)
b5.pack()

tkinter.mainloop()
