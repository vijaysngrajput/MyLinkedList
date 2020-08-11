class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class linkedList:
    def __init__(self):
        self.head = None

    def pushAtFront(self,value):
        newnode = node(value)

        #Make next of new node as head and previous as NULL
        newnode.next = self.head
        newnode.previous = None
        #change prev of head node to new node
        if self.head is not None:
            self.head.previous = newnode
        #move the head to point to the new node
        self.head = newnode

    def pushAtEnd(self,value):
        newnode = node(value)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = newnode
        newnode.previous = temp

    def pushAtPostion(self,value,position):
        newnode = node(value)

        count = 0
        temp = self.head

        while(temp):
            count += 1
            if count == position:
                temp2 = temp.next
                # temp3 = temp
                temp.next = newnode
                newnode.next = temp2
                newnode.previous = temp
                return
            temp = temp.next

#======================================================        
    def deleteAtFront(self):
        self.head = self.head.next
        self.head.previous = None

    def deleteAtEnd(self):
        temp = self.head
        temp2 = self.head.next
        while(temp2.next):
            temp = temp.next
            temp2 = temp2.next
        temp.next = None
        temp2.previous = None

    def deleteAtPosition(self,position):
        temp = self.head
        count = 0
        while(temp.next):
            count += 1
            if count == position:
                temp.next = temp.next.next
                # temp.next.previous = None
                return
            temp = temp.next
#====================================================== 
    def printMyList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next
        print("")







a = linkedList()
a.pushAtFront(2)
a.pushAtFront(3)


a.pushAtEnd(7)
a.pushAtEnd(8)

a.pushAtPostion(9,2)

a.deleteAtFront()
a.deleteAtEnd()

a.pushAtFront(2)
a.pushAtFront(3)

a.deleteAtPosition(2)
a.printMyList()