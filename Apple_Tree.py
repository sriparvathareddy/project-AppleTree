from array_queue import ArrayQueue
from array_stack import ArrayStack

class AppleTree():
    def __init__(self):
        self.appleTreeQueue = ArrayQueue()
        for i in range(100):
            self.appleTreeQueue.enqueue("apple")

    def applesLeft(self):
        return len(self.appleTreeQueue)

    # def loseApple(self):
    #     self.appleTree.dequeue()
        
class Worker():
    def __init__(self, name, gender, type):
        self.name = name
        self.gender = gender
        self.type = type

        print("\nName of worker: " + name + "\nGender: " + gender + "\nType: " + type)

    def treeToBasket(self):
        
        if self.type == "basketworker" and len(appleTree1.appleTreeQueue) >= 0:
            # do something
            for i in range(5):
                basket1.basketstack.push(appleTree1.appleTreeQueue.dequeue())
                print("\n" + basketWorker.name + " picked an apple")

            print("\n*******************************************************")
            print("\tBasket has " + str(len(basket1.basketstack)) + " apples")
            self.basketToWagon()
        elif len(appleTree1.appleTreeQueue) <= 0:
            print("No apples left.")
        else:
            print("Must be a basketworker to use this function")
            
    def basketToWagon(self):
        if self.type == "basketworker":
            for i in range(len(basket1.basketstack)):
                wagon1.wagonstack.push(basket1.basketstack.pop())

            print("\n*******************************************************")
            print("\tWagon has " + str(len(wagon1.wagonstack)) + " apples")
            print("\n*******************************************************")
            print("\tBasket has " + str(len(basket1.basketstack)) + " apples")

            if len(wagon1.wagonstack) >= 40:
                self.wagonToStorage()
            self.basketToWagon()
        else:
            print("Must be a basketworker to use this function")

    def wagonToStorage(self):
        if self.type == "wagonworker":
            for i in range(len(wagon1.wagonstack)):
                storage1.storagequeue.enqueue(wagon1.wagonstack.pop())


                print("\nAfter all that:\n")
                print(basket1.basketstack.is_empty())
                print(len(wagon1.wagonstack))
        else:
            print("Must be a wagonworker to use this function")
     

class Basket():
    def __init__(self):
        self.capacity = 5
        self.basketstack = ArrayStack()

class Wagon():
    def __init__(self):
        self.capacity = 50
        self.wagonstack = ArrayStack()

class Storage():
    def __init__(self):
        self.capacity = 500
        self.storagequeue = ArrayQueue()

# initiates the important classes
appleTree1 = AppleTree()
storage1 = Storage()
wagon1 = Wagon()
basket1 = Basket()
basketWorker = Worker("John", "M", "basketworker")
wagonWorker = Worker("Emily", "F", "wagonworker")

#work functions
print("\nThere are " + str(appleTree1.applesLeft()) + " apple(s) left in the tree")

basketWorker.treeToBasket()
appleTree1.applesLeft()

#(apple tree, basket, worker, wagon, storage).