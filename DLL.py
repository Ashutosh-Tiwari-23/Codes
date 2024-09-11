class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class LinkedLlist:
    def __init__(self):
        self.head = None
    
    def printListVal(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.data}", end = " ")
            curr = curr.next 
    def insertNodeBegining(self, val):
        newNode = Node(val)
        if self.head is None:
            print("list is empty")
            self.head = newNode
            return 
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return self.head
    
    def insertNodeIndex(self, index, val):
        newNode = Node(val)
        if index<0:
            raise IndexError("index can't be neghative")
        
        lenList = self.lengthList()

        if index==0:
            return self.insertNodeBegining(val)
        
        #check index out of bound error
        if index>=lenList:
            print("node does not exist at the given index, inserting at the end")
            index = lenList

        curr = self.head
        for i in range(index - 1):
            if curr is not None:
                curr = curr.next
            else:
                raise IndexError("Index out of bound")
        
        #Insertion logic
        newNode.next = curr.next
        newNode.prev = curr

        if curr.next is not None:
            curr.next.prev = newNode
        else:
            raise IndexError("Index out of bound")
        
        curr.next  = newNode
        return self.head
    def insertNodeEnd(self, val):
        newNode = Node(val)
        if self.head is None:
            print("List is empty, the node added will be the end node")
            self.head = newNode
            return 
        else:
            #traverse to the last node
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            newNode.prev = curr 
            curr.next = newNode
            return self.head
    
    def deleteFirstNode(self):
        if self.head is None:
            return "list is empty"
        else:
            self.head = self.head.next
            return self.head 
        

    def deleteNthNode(self, n):
        if self.head is None:
            return "list is empty"
        
        if n==0:
            return self.deleteFirstNode()
        
        lenList = self.lengthList() 
        if n<0:
            raise IndexError("index can not be negative")
        
        if n>=lenList:
            raise IndexError("Index out of bound")
        
        curr = self.head 
        for i in range(n - 1):
            if curr is not None:
                curr = curr.next
            else:
                raise IndexError("Out of bound index")
        #handling delettion of last node
            
        if curr.next.next is None:
            curr.next = None
        else:
            curr.next.next.prev = curr
            curr.next = curr.next.next
        
        return self.head

        