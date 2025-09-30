from multiprocessing import Process
import os
def info(title):
    print(title)
    print("module name :",__name__)
    print("parent process id :",os.getppid())
    print("child process id :", os.getpid())
def f(name):
    info('function f')
    print("hello ",name)
if __name__ == '__main__':
    info('main line')
    p = Process(target= f, args = ('bob',))
    p.start()
    p.join()
    print("child process name: ",p.name)
    print("child process id ",p.pid)