import notify2
import datetime
from datetime import *
import time
import json
from tkinter import *
import tkinter as tk
from multiprocessing import Process
def sendNoti(txt):
	notify2.init('app name')
	n = notify2.Notification("Reminder",
						f"{txt}",
			            "notification-message-im"   # Icon name
			            )
	n.show()
def clock():
    while True:
        current_time = datetime.now().strftime("%d%H:%M")
        time.sleep(60)
        return current_time





def Reminder():
	file = open('data.json','r+')
	data = json.load(file)
	while True:
		x = clock()
		Stime = x.replace(":","")
		Itime = int(Stime)
		# print(Itime)
		for task,Ctime in data.items():
			X = Ctime.replace(":","")
			y = int(X)
			if y == Itime:
				sendNoti(task)				
			else:
				pass
	file.close()

	

def Window():
	canvas = Tk()
	canvas.geometry("500x500")
	canvas.title("Reminder")
	file = open("data.json","r+")
	data = json.load(file)
	RTList = Listbox(canvas,width=50)
	RTList.pack(pady=15)
	for task, time in data.items():
		RTList.insert(END,f"{task} {time}")
	
	def Remove():
		x = RTList.get(ANCHOR)
		l = x.replace(":","").replace(" ","")
		ftask = ''
		for i in l:
			try:
				int(i)
				pass
			except:
				ftask = ftask + i
		Ltask = ""
		file = open("data.json","r+")
		data = json.load(file)
		for i in data.copy():
			x = i.replace(" ","")
			if ftask == x:
				data.pop(i,None)
				x = data 
				RTList.delete(ANCHOR)
				file.seek(0)
				file.truncate(0)
				file.write(json.dumps(x))
				file.close()
	Delete = Button(canvas, text="Remove", command=Remove)
	Delete.pack(pady=10)
	def AddTextbox(name,placeholder):
		def click(*args):
			name.delete(0, 'end')
		name.insert(0, f'{placeholder}')
		name.pack(pady=10)
		name.bind("<Button-1>", click)
	EnterTask = Entry(canvas, width=45)
	EnterDate = Entry(canvas, width=45)
	EnterHour = Entry(canvas, width=45)
	Entermin = Entry(canvas, width=45)
	AddTextbox(EnterTask, "Enter the Task")
	AddTextbox(EnterDate, "Enter the date(this Month):- ")
	AddTextbox(EnterHour, "Enter the Hour")
	AddTextbox(Entermin, "Enter the Mins")
	def AddTask():
		Task = EnterTask.get()
		Date = EnterDate.get()
		Hour = EnterHour.get()
		Mins = Entermin.get()
		RTList.insert(END,f"{Task} {Date}:{Hour}:{Mins}")
		DHM = f"{Date}:{Hour}:{Mins}"
		EtextTime = {Task:DHM}
		Writepass(EtextTime)
	def Writepass(txt):
		outfile = open("data.json", 'r+')
		data = json.load(outfile)
		data.update(txt)
		outfile.seek(0)
		json.dump(data, outfile)	


	Add = Button(canvas,text="Add",command=AddTask)
	Add.pack(pady=10)
	file.close()
	canvas.mainloop()
	
def RestartReminder():
	while True:
		process = Process(target= Reminder)
		process.start()
		time.sleep(250)
		process.terminate()

def myFunc():
	if __name__=='__main__':
		p1 = Process(target = Window)
		p1.start()
		p2 = Process(target = RestartReminder)
		p2.start()

myFunc()
