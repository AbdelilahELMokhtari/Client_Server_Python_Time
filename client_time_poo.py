from tkinter import *
import socket
import datetime

win=Tk()
win.geometry('450x260')

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9999))
class frame_time:
    def __init__(self,root):
        self.__win=root
    def creation_frame(self):
        self.__frm=Frame(self.__win,width=450,height=260,background='#85C1E9')
        self.__frm.pack()
    def clear_frm(self):
        for widget in self.__frm.winfo_children():
            widget.destroy()     
    def getframe(self):
        return self.__frm

class Lable_time:
    def __init__(self,frm,txt):
        self.__frm=frm
        self.__txt=txt
    def creation_lable(self):
        self.__lable=Label(self.__frm,text=self.__txt,font=('Arial',15))
        self.__lable.place(x=140,y=3)
    def settxt(self,txt):
        self.__txt=txt

class Butten_time:
    def __init__(self,frm,txt,x,y,comond=None):
        self.__cmnd=comond
        self.__frm=frm
        self.__txt=txt
        self.__x=x
        self.__y=y
    def creation_butten(self):
        self.__butten=Button(self.__frm,text=self.__txt,command=self.__cmnd)
        self.__butten.place(x=self.__x,y=self.__y,width=170,height=30)
    
frame_start=frame_time(win)
frame_start.creation_frame()
  
  
def Time_now():
    client.send('TIME'.encode('utf-8'))
    reponse=client.recv(1024).decode('utf-8')
    lable_start.settxt(reponse)
    lable_start.creation_lable()
  
def clear():
    frame_start.clear_frm()
    lable_start.settxt('Server Listing ...')
    lable_start.creation_lable()    
    butten_get_time=Butten_time(frame_start.getframe(),'Get Time',70,200,Time_now)
    butten_get_time.creation_butten()
    butten_by=Butten_time(frame_start.getframe(),'EXIT',250,200)
    butten_by.creation_butten()
       
       
lable_start=Lable_time(frame_start.getframe(),'Hello Welcome To\n the server for Time ...')
lable_start.creation_lable()
butten_start=Butten_time(frame_start.getframe(),'START',155,160,clear)
butten_start.creation_butten()



        









win.mainloop()