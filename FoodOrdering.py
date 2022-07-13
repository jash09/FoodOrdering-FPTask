from time import sleep
from threading import Thread
import Queue
queue = Queue.Queue()
def placeOrder(*items):
    for i in items:
        print("Order Placed for ",queue.enqueue(i),"\n")
        
        sleep(0.5)
def serveOrder():
    while not queue.isEmpty():
        order = queue.dequeue()
        print(order," has been served \n")
        sleep(2)

if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = Thread(target=placeOrder, args=orders)
    t2 = Thread(target=serveOrder)
    t1.start()
    sleep(1)
    t2.start()