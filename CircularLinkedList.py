class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def checkCircular(self):
        temp1 = self.head
        temp2 = self.head.next.next
        while (temp1.next):
            if temp1 == None:
                print("NO LOOP")
                break
            if temp2 == None:
                print("NO LOOP")
                break
            if temp1.data == temp2.data:
                print("there is a loop")
                break 
            temp1 = temp1.next
            
            temp2 = temp2.next

llist = linkedlist()
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third
third.next = second
llist.checkCircular()