import random
import time
import threading
class Semaforo():
    color=''
    def __init__(self, conta=0):
        self.locked = threading.Lock()
        self.conta_send= conta
    
    def pasa(self,num):
        self.locked.acquire()

        try:
            color="verde"
            print(num,"en ",color)
        finally:
            self.locked.release()
    def para(self,num):
            self.locked.acquire()
            try:
                color='rojo'
                print(num,"en ",color)
            finally:
                    self.locked.release()


def func_conta(x,y):
    for i in range(4):
        if(i%2==0):
            time_f = random.random()
            time.sleep(time_f)
            x.pasa("semaforo a")
            y.para('semaforo b')
            print("______________________")
        elif(i%2==1):
            y.pasa("semaforo b")
            x.para('semaforo a')
            print("______________________")
            #print(i)

if __name__ =="__main__":
    semaforo = Semaforo()
    semaforo2 = Semaforo()
    for i in range(4):
        tstart = threading.Thread(target=func_conta,args=(semaforo,semaforo2,))
        tstart.start()
