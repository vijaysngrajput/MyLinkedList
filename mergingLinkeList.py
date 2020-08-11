class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def pushDataAtFront(self,value):
        newnode = node(value)

        if self.head == None:
            self.head = newnode
            return

        newnode.next = self.head
        self.head = newnode

    def pushDataAtEnd(self,value):
        newnode = node(value)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = newnode

    def pushDataAtPostion(self,position,value):
        
        if position == 0:
            linkedList.pushDataAtFront(self,value)
            return
        
        newnode = node(value)

        count = 0
        temp = self.head
        while(temp):
            count += 1
            if count == position:
                temp2 = temp.next
                temp.next = newnode
                newnode.next = temp2
                return
            temp = temp.next
   
   
   
    def printMyLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next
        print(" ")



    def merge(self,list1 , list2):
        head1 = list1.head
        head2 = list2.head
        while (head1):
            print(head1.data)
            list2.pushDataAtEnd(head1.data)
            head1 = head1.next
        list2.printMyLinkedList()



a = linkedList()
a.pushDataAtFront(8)
# a.printMyLinkedList()    
a.pushDataAtFront(83)
# a.printMyLinkedList()    
a.pushDataAtFront(82)
# a.printMyLinkedList()    
a.pushDataAtFront(81)
a.printMyLinkedList()



b = linkedList()
b.pushDataAtFront(833)
# b.printMyLinkedList()    
b.pushDataAtFront(8344)
# b.printMyLinkedList()    
b.pushDataAtFront(8255)
  
b.pushDataAtFront(8166)
b.printMyLinkedList()      
b.pushDataAtEnd(8166222)
b.printMyLinkedList()      

c = linkedList()
c.merge(a,b)
# def merge(list1 , list2):
#     head1 = list1.head
#     head2 = list2.head
#     while (head1):
#         print(head1.data)
#         list2.pushDataAtEnd(head1.data)
#         head1 = head1.next
#     list2.printMyLinkedList()

# merge(a,b)



















#==============================
    # def deleteAtFront(self):
    #     self.head = self.head.next

    # def deleteAtEnd(self):
    #     temp = self.head
    #     temp2 = self.head.next
    #     while(temp2.next):
    #         temp = temp.next
    #         temp2 = temp2.next
    #     temp.next = None

    # def deleteAtPosition(self,position):
    #     count = 0
    #     temp = self.head
    #     while(temp):
    #         count += 1
    #         if count == position:
    #             temp.next = temp.next.next