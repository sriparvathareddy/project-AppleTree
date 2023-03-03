from array_queue import ArrayQueue
from array_stack import ArrayStack

class AppleTree:
    def __init__(self):
        self.appleTree = ArrayQueue()
        for i in range(100):
            self.appleTree.enqueue("apple")

    def applesLeft(self):
        print("There are " + str(len(self.appleTree)) + " left in the tree")

    def takeApple(self):
        self.appleTree.dequeue()
        
appleTree1 = AppleTree()
appleTree1.takeApple()
appleTree1.applesLeft()
    
#(apple tree, basket, worker, wagon, storage).