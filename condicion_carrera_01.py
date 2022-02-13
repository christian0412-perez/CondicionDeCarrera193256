import random
import time
import threading
class Semaforo():
    def __init__(self, conta=0):
        self.locked = threading.Lock()
        self.conta_send= conta
    
    def pasa(self,num):
        self.locked.acquire()

        try:
            print(num,"en verde")
        finally:
            self.locked.release()
    def para(self,num):
            self.locked.acquire()
            try:
                print(num,"en rojo")
            finally:
                self.locked.release()

def func_conta(x):
    for i in range(2):
        if(i%2==0):
            time_f = random.random()
            time.sleep(time_f)
            x.pasa("semaforo a")
            x.para('semaforo b')
            print("______________________")
        elif(i%2==1):
            x.para("semaforo a")
            x.pasa('semaforo b')
            print("______________________")
            #print(i)

if __name__ =="__main__":
    semaforo = Semaforo()
    for i in range(2):
        tstart = threading.Thread(target=func_conta,args=(semaforo,))
        tstart.start()
