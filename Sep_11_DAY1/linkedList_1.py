class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        current = self.head
        while current is not None:
            print(f"{current.data}", end= " ")
            current = current.next
    ''' INSERT OPERATIONS'''
    def insertNodeBegining(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return self.head
        else:
            newNode.next = self.head 
            self.head = newNode
            return self.head
    def insertNodeEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            print("List is empty, node will be added as the first node")
            return self.insertNodeBegining(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
            return self.head
    def insertNodeAtIndex(self, index, value):
        if index < 0:
            raise IndexError("Index cannot be negative")
        
        newNode = Node(value)
        if self.head is None:
            if index ==0:
                return self.insertNodeBegining(value)
            else:
                raise IndexError("list is empty, node can't be inserted at any index except 0")
        listLen = self.listLength()
        if index > listLen:
            print("index not found as node does not exist , node will be inserted at the end")
            index = listLen
        current = self.head 
        for i in range(index - 1):
            if current is not None:
                current = current.next 
            else:
                raise IndexError("index out of bound")
        newNode.next = current.next 
        current.next = newNode
        return self.head
    def deleteFirstNode(self):
        if self.head is None:
            return "list is empty"
        # handling if the list has just one node
        if self.head.next is None:
            self.head = None
            return self.head
        else:
            self.head = self.head.next 
            return self.head 
    def deleteKthNode(self, k):
        listLen = self.LengthList() 
        if self.head is None:
            return "list is empty"
        if k==0:
            return self.deleteFirstNode()
        
        #check index out of bound errror
        if k>=listLen:
            print("kth node does not exist in the list")
            return
        else:
            current = self.head
            for i in range(k - 1):
                if current is not None:
                    current = current.next 
            current.next = current.next.next 
            return self.head 
        
            