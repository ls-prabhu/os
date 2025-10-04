import threading
import time
class ReaderWriterProblem():
    def __init__(self):
        self.mutex = threading.Semaphore()
        self.wrt = threading.Semaphore()
        self.r_c=0
    def reader(self):
        while True:
            self.mutex.acquire()
            self.r_c+=1
            if self.r_c==1:
                self.wrt.acquire()
            self.mutex.release()
            print(f"\nReader{self.r_c} is reading")
            self.mutex.acquire()
            self.r_c-=1
            if self.r_c==0:
                self.wrt.release()
            self.mutex.release()
            time.sleep(3)
    def writer(self):
        while True:
            self.wrt.acquire()
            print("writng data.....")
            print("-"*20)
            self.wrt.release()
            time.sleep(3)
    def main(self):
        t1=threading.Thread(target = self.reader)
        t1.start()
        t2=threading.Thread(target = self.writer)
        t2.start()
        t3=threading.Thread(target = self.reader)
        t3.start()
        t4=threading.Thread(target = self.reader)
        t4.start()
        t6=threading.Thread(target = self.writer)
        t6.start()
        t5=threading.Thread(target = self.reader)
        t5.start()
if __name__=="__main__":
    c= ReaderWriterProblem()
    c.main()