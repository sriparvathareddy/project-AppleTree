from array_queue import ArrayQueue
from array_stack import ArrayStack

class AppleTree():
    def __init__(self, StartAppleAmount):
        self.appleTreeQueue = ArrayQueue()
        for i in range(StartAppleAmount):
            self.appleTreeQueue.enqueue("apple")

    def applesLeft(self):
        return len(self.appleTreeQueue)
        
class Worker():
    def __init__(self, name, gender, type):
        self.name = name
        self.gender = gender
        self.type = type

        print("\nName of worker: " + name + "\nGender: " + gender + "\nType: " + type)

    def treeToBasket(self):
        
        if self.type == "basketworker" and len(appleTree1.appleTreeQueue) > 0:
            # for i in range(5):
            basket1.basketstack.push(appleTree1.appleTreeQueue.dequeue())
            print("\n" + self.name + " picked an apple")

        elif len(appleTree1.appleTreeQueue) <= 0:
            print("\n***************************")
            print("Apples left in tree: " + str(len(appleTree1.appleTreeQueue)))
            print("Basket has " + str(len(basket1.basketstack)) + " apples")
            print("Wagon has " + str(len(wagon1.wagonstack)) + " apples")
            print("Storage has " + str(len(storage1.storagequeue)) + " apples")
            print("\n*************************")
            quit()
        else:
            print("Must be a basketworker to use this function")
            
    def basketToWagon(self):
        if self.type == "basketworker":
            for i in range(len(basket1.basketstack)):
                wagon1.wagonstack.push(basket1.basketstack.pop())

            print("\n************************")
            print("John empty basket into wagon\n")
            print("Wagon has " + str(len(wagon1.wagonstack)) + " apples")
            print("Basket has " + str(len(basket1.basketstack)) + " apples")
            print("\n***************************")

        else:
            print("Must be a basketworker to use this function")

    def wagonToStorage(self):
        if self.type == "wagonworker":
            for i in range(len(wagon1.wagonstack)):
                storage1.storagequeue.enqueue(wagon1.wagonstack.pop())

            print("Rachel empty wagon into storage\n")
            print("Wagon has " + str(len(wagon1.wagonstack)) + " apples")
            print("storage has " + str(len(storage1.storagequeue)) + " apples")
            print("\n**************************")
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
appleTree1 = AppleTree(120)
storage1 = Storage()
wagon1 = Wagon()
basket1 = Basket()
basketWorker = Worker("John", "M", "basketworker")
wagonWorker = Worker("Emily", "F", "wagonworker")

#work functions
print("\nThere are " + str(appleTree1.applesLeft()) + " apples left in the tree")

# running function calls everything

for i in range(1, 3600):
    if i % 10 == 0:
        basketWorker.treeToBasket()
        print("time: " + str(i / 10) + " seconds")
    if i % 50 == 0:
        basketWorker.basketToWagon()
    if i % 400 == 0:
        wagonWorker.wagonToStorage()
    if i % 600 == 0:
        print("\n*************************")
        print("Apples left in tree: " + str(len(appleTree1.appleTreeQueue)))
        print("Basket has " + str(len(basket1.basketstack)) + " apples")
        print("Wagon has " + str(len(wagon1.wagonstack)) + " apples")
        print("Storage has " + str(len(storage1.storagequeue)) + " apples")
        print("\n*************************")
