#CREATE LINKED LIST

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
#======================================================================    
    def pushInFront(self,value):
        newnode = node(value)

        newnode.next = self.head
        self.head = newnode
    
    def pushInEnd(self,value):
        newnode = node(value)

        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newnode

    def pushInPosition(self,value,position):
        
        if position == 0:
            linkedlist.pushInFront(self,value)
            return
        newnode = node(value)
        count = 0

        temp = self.head
        while (temp):
            count += 1
            if count == position:
                temp2 = temp.next
                temp.next = newnode
                newnode.next = temp2 
                return
            temp = temp.next

#======================================================================
    def printMyLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next
        print(" ")
#======================================================================
    def deleteFromFront(self):
        self.head = self.head.next
    

    def deleteFromEnd(self):
        temp = self.head
        if temp.next == None:
            temp.data = None
        if temp.data == None:
            print("nothing here")
            return
        temp2 = self.head.next

        while(temp2.next != None ):
            temp2 = temp2.next
            temp = temp.next
        temp.next = None

    def deleteAtPosition(self,position):
        position = int(position)
        count = 0
        if position == 0:
            linkedlist.deleteFromFront(self)
            return
        temp = self.head

        while(temp):
            count += 1
            if count == position:
                temp.next = temp.next.next
                return
            temp = temp.next
#======================================================================
a = linkedlist()

a.pushInFront(21)
a.pushInFront(29)


a.pushInEnd(77)
a.pushInEnd(33)

a.printMyLinkedList()

a.deleteAtPosition(0)
a.printMyLinkedList()

a.pushInPosition(999,4)
a.printMyLinkedList()

# a.deleteFromEnd()
# a.printMyLinkedList()
# a.deleteFromEnd()
# a.printMyLinkedList()
# a.deleteFromEnd()
# a.printMyLinkedList()
# a.deleteFromEnd()
# a.printMyLinkedList()