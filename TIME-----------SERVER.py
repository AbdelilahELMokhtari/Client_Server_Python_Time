import socket
import threading
import datetime

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',9999))
server.listen()
server.setblocking(1)
print('Mode Lsting ....')
Nicknames=[]
clients_info=[]
def reponse(message,client):
   if message.upper() == 'TIME':

      time_now=datetime.datetime.now()
      #time_now=time_now.split(' ')
      time=time_now.strftime("%H:%M:%S %d/%m/%Y ")
      time=time.split()
      client.send(f'Heure : {time[0]}\nDate Today : {time[1]}'.encode('utf-8'))
      print('time Sending ...')
            #client.close()

   else :
      client.send(f'[+] Tapy TIME Not {message} [+]'.encode('utf-8'))
            #client.close()
    
def recive(client_info):
   while True:
      try:
         message = client_info.recv(1024).decode('utf-8')
         reponse(message,client_info)
      except:
         print('client Left .. !')
         break
def accept():
   while True:
      client_info,address=server.accept()
      print(f"CONNECTION WITH {address}...")
      #client_info.send('[+] Connection to the server [+] Tapy : TIME '.encode('utf-8'))
      #Nickname=client_info.recv(1024).decode('utf-8')
     # Nicknames.append(Nickname)
      #clients_info.append(client_info)
      th=threading.Thread(target=recive,args=(client_info,))
      th.start()            
            #reponse(message,client_info)
accept()
   

    