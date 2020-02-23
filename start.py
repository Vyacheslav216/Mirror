#!/usr/bin/python3
from tkinter import *
from tkinter import font
import threading
import time
import weather as fl
from datetime import date, timedelta
from PIL import Image,ImageTk
import sys
from task import quickstart as qs
#import urllib.request
root = Tk()
root.title('Second')
root.geometry('768x1024')
root.configure(bg='#000')
labelpicc=[]
labeltempp=[]
labeldatee=[]
labelr=Label()

def clock(interval):
	 old="25"
	 while True:
	 	ttime['text'] = ''.join((time.strftime('%H:%M ')))
	 	ddate['text']=''.join((time.strftime('%d-%B-%Y ')))
	 	if(old!=time.strftime('%H')):
	 		old=time.strftime('%H')
	 		d = threading.Thread(target=refreshw,daemon=True)
	 		d.start()
	 	time.sleep(interval)
	 		

def refreshw():
	clearw()
	pictur()


def clearw():
	for i in range(0,len(labelpicc)):
		labelpicc[i].destroy()
		labeltempp[i].destroy()
	for i in range(0,len(labeldatee)):
		labeldatee[i].destroy()
	labelpicc.clear()
	labeltempp.clear()
	labeldatee.clear()

def quickstartt():
	while True:
		clearg()
		googletask()
		time.sleep(5) 

def clearg():
	labellist.destroy()

def pictur():
	 pic=fl.gettemp()['pic']
	 path=[]
	 for i in range(0,len(pic)):
	 	b=0
	 	s=str(pic[i])
	 	if((s.find("дождь")!=-1)|(s.find("Дождь")!=-1)|(s.find("Ливень")!=-1)):
	 		b=1
	 	if((s.find("облачно")!=-1)|(s.find("Облачно")!=-1)|(s.find("Пасмурно")!=-1)):#| equal or??
	 		b=2
	 	if((s.find("снег")!=-1)|(s.find("Снег")!=-1)):
	 		b=3	
 		if((s.find("ясно")!=-1)|(s.find("Ясно")!=-1)):
	 		b=4	
	 	try:
	 		result={
	 		1:"imageW/rain.png",
	 		2:"imageW/with_sun.png",
	 		3:"imageW/snow.png",
	 		4:"imageW/sun.png"
	 		}[b]
	 	except:
	 		print('error  '+str(pic[i]))
	 		result="imageW/cloudly.png"
	 	path.append(result)
	 weatherr(path)


#def beatifulpic(path):
	 
	 

def weatherr(path):
	 i=0	 
	 day=fl.gettemp()['day']
	 night=fl.gettemp()['night']
	 img = Image.open(path[i])
	 img =img.resize((75, 75), Image.ANTIALIAS)
	 render = ImageTk.PhotoImage(img)
	 Mylabelpic=Label(root,image=render,bg='#000')	 
	 Mylabelpic.render=render
	 Mylabeltemp=Label(root,text="",fg='#FFF', bg='#000',font=("Sawasdee", 16,"bold"))
	 newdate=date.today()
	 Mylabeltemp['text'] +="".join(day[i])
	 Mylabeltemp['text'] +="".join(' °C / ')
	 Mylabeltemp['text'] +="".join(night[i])
	 Mylabeltemp['text'] +="".join(' °C')
	 Mylabelcity=Label(root,text="Санкт-Петербург",fg='#FFF', bg='#000',font=("Manjari Bold", 17,'bold'))
	 Mylabelpic.place(x=start+xx-70,y=starty)
	 Mylabeltemp.place(x=start+xx*2+15-25-20,y=starty+25)
	 labelpicc.append(Mylabelpic)
	 labeltempp.append(Mylabeltemp)
	 Mylabelcity.place(x=30,y=starty-25,anchor='w')
	 for i in range(1,len(day)):
		 img = Image.open(path[i])
		 img =img.resize((50, 50), Image.ANTIALIAS)
		 render = ImageTk.PhotoImage(img)
		 Mylabelpic=Label(root,image=render,bg='#000')
		 Mylabelpic.render=render
		 Mylabeltemp=Label(root,text="",fg='#FFF', bg='#000',font=("Sawasdee", 12,"bold"))
		 Mylabeldate=Label(root,text="",fg='#FFF', bg='#000',font=("Sawasdee", 12,"bold"))
		 newdate=date.today()+timedelta(days=i)
		 Mylabeldate['text'] +="".join(newdate.strftime('%d %b '))
		 Mylabeltemp['text'] +="".join(day[i])
		 Mylabeltemp['text'] +="".join(' °C / ')
		 Mylabeltemp['text'] +="".join(night[i])
		 Mylabeltemp['text'] +="".join(' °C')
		 #Mylabeldate.grid(column=1, row=5+i, padx=x, pady=y)
		 #Mylabelpic.grid(column=2, row=5+i, padx=x, pady=y)
		 #Mylabeltemp.grid(column=3, row=5+i, padx=x, pady=y)
		 Mylabeldate.place(x=start,y=starty+15+(i*yy)+30)
		 labeldatee.append(Mylabeldate)
		 Mylabelpic.place(x=start+xx,y=starty+(i*yy)+35)
		 Mylabeltemp.place(x=start+xx*2,y=starty+15+(i*yy)+30)
		 labelpicc.append(Mylabelpic)
		 labeltempp.append(Mylabeltemp)
		 
		 
		 
def googletask():
	 listtask=qs.main()
	 labelhead=Label(root,text="Google Tasks",fg='#FFF', bg='#000',font=("Manjari Bold", 20,"bold"))
	 labellist=Label(root,text="",fg='#FFF', bg='#000',font=("Manjari Bold", 14),justify="right")
	 labelhead.place(x=768-30,y=starty-44,anchor='ne')
	 labellist.place(x=768-30,y=starty,anchor='ne')
	 for r in range(0,len(listtask)): 
	 	for i in range(0,len(listtask[r])):
	 		labellist['text']+="".join(str(listtask[r][i]))
	 		labellist['text']+="".join('\n')
	 	s=labellist.cget("text")
	 if(s==""):
	 	labellist['text']='На сегодня задач нет'
	 	#post+=40

#MAIN
xx=75
yy=75
starty=320
start=30
ttime = Label(root, text="",fg='#FFF', bg='#000',font=("Sawasdee", 60,"bold"),justify="center")#Uroob
ttime.place(x=384,y=100,anchor="center")
ddate = Label(root, text="",fg='#FFF', bg='#000',font=("Sawasdee", 16,"bold"),justify="center")
ddate.place(x=384-10,y=170,anchor="center")
list_fonts = list( font.families() )
list_fonts.sort()
#for i in range(0,len(list_fonts)):
	# print(list_fonts[i])
#root.attributes('-fullscreen', True)

threading.Thread()
t = threading.Thread(target=clock, args=(1,),daemon=True)
threading.Thread()
g = threading.Thread(target=quickstartt, args=(),daemon=True)


#pictur()
labellist=Label(root,text="",fg='#FFF', bg='#000',font=("Manjari Bold", 14),justify="right")
t.start()
g.start()
#root.grid_columnconfigure(ALL, minsize=100)
#root.grid_rowconfigure(ALL, minsize=100)
root.mainloop()