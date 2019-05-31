from multiprocessing import Process
import time

def loop_a():
    while 1:
        print("a")
        sleep(1)

def loop_b():
    while 1:
        print("b")
        sleep(1)

if __name__ == '__main__':
    Process(target=loop_a).start()
    Process(target=loop_b).start()
