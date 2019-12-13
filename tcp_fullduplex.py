#@author:: Ashish Kulai
#@program:: Full duplex TCP/IP point to point communication [python implementation]

#========================IMPORTS=====================#
import time
import threading
import socket
#========================IMPORTS=====================#

def threadrxn():
    print("-------------RXN :: from RPi :: TCP----------------")
    
    HOST1 = '192.168.0.106' # Standard loopback interface address (localhost = our computer)
    PORT1 = 65400 # Port to listen on (non-privileged ports are > 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # transmit object -> s is local scope will not matter in operation of prog
      
      s.bind((HOST1, PORT1))
      s.listen()
      conn, addr = s.accept()
      
      with conn:
        print('\n\nRXN :: TCP :: Connected by ::-------->', addr)
        while True:
          data = conn.recv(1024)
          data_p = data.decode(encoding='utf-8')
          print("\n\n-RXN[recived] :: from RPi :: TCP----> ",data_p)
          
          if not data:
            break
        
          #conn.sendall(data) ## TESTING :: echo
          #print("---server returned the same data :",data_p)  ## TESTING :: echo    
    
def send_tcp(mystring):
    b = bytes(str(mystring), 'utf-8')
    s.sendall(b)
    
    print("-TXN[sent] :: to RPi :: TCP-> ",mystring)
    
    
#========================MAIN============================================#
t2 = threading.Thread(target=threadrxn)
t2.start()

#========================================================================================#
#---------------------------------transmit :: connect :: area----------------------------#
print("--------------ENTER :: CONNECT :: TCP ---------------")
#HOST = '192.168.0.111' # The server's hostname or IP address (the other computer)
HOST = '192.168.0.150' # The server's hostname or IP address (the other computer)
PORT = 65432 # The port used by the server


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # we want transmit object -> s as global scope
while 1:
    print("------------CONECTING :: TCP--------------->>>>>>>>>>")
    try:
        s.connect((HOST, PORT))
        print("----------TCP :: CONNECTED ---------------------")
        break   
    except:
         print("-----------------TCP :: ERROR :: in CONNECTION-------------------")
         time.sleep(1)
#---------------------------------transmit :: connect :: area----------------------------#
         
while 1:  #testing::
    send_tcp("status:2") #testing:: send message any where in program :: global scope
    time.sleep(1)  #testing::

#========================================================================================#
#========================MAIN============================================#
    