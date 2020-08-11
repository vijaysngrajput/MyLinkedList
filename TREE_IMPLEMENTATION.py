class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class linkedList:
    def __init__(self):
        self.head = None

    def insert(self,value):
        if self.head == None:
            self.head = node(value)
            return
        
        if self.head !=None:
            linkedList.insertPlease(self,value,self.head)

    def insertPlease(self,value,currentNode):
        if value > currentNode.data:
            if currentNode.next == None:
                currentNode.next = node(value)
            else:
                linkedList.insertPlease(self,value,currentNode.next)

        elif value < currentNode.data:
            if currentNode.prev == None:
                currentNode.prev = node(value)
            else:
                linkedList.insertPlease(self,value,currentNode.prev)
        else:
            print("value exist")

    def printTree(self):
        if(self.head != None):
            self._printTree(self.head)
    
    def _printTree(self,node):
        if(node != None):
            self._printTree(node.prev)
            print(node.data)
            self._printTree(node.next)

a = linkedList()
a.insert(12)

a.insert(3)

a.insert(10)

a.insert(4)

a.insert(14)

a.insert(5)

a.insert(16)

a.insert(1)

a.insert(22)

a.insert(2)


a.printMyList()

print("=======")
a.printMyList2()
print("=======")
a.printTree()