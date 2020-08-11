class node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class linkedList:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if(self.root == None):
            self.root = node(value)
        else:
            self._insert(value,self.root)
    
    
    
    
    def _insert(self,value,cur_node):
        if (value < cur_node.value):
            if cur_node.left == None:
                cur_node.left = node(value)
            else:
                self._insert(value,cur_node.left)
        elif (value > cur_node.value):
            if cur_node.right == None:
                cur_node.right = node(value)
            else:
                self._insert(value,cur_node.right)
        else:
            print("value exist")
    


    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)
    
    def _printTree(self,node):
        if(node != None):
            self._printTree(node.left)
            print(node.value)
            self._printTree(node.right)


    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0
    
    def _height(self,cur_node,cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left,cur_height+1)
        right_height = self._height(cur_node.right,cur_height+1)
        return max(left_height,right_height)

    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False
    
    def _search(self,value,cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left != None:
            self._search(value,cur_node.left)
        elif value < cur_node.value and cur_node.right != None:
            self._search(value,cur_node.right)
        else:
            return False
# tree = linkedList()
# tree.insert(3)
# tree.insert(4)
# tree.insert(0)
# tree.insert(8)
# tree.insert(2)


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

a.printTree()
print("====")
# print(tree.height())
# print(tree.search(0))

