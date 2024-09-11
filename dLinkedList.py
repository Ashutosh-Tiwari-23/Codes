"""Doubly linked list is a type of linked list where each node has two pointers, one pointing to next node and the other to the previous node"""
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  # pointer to next next node
        self.prev = None  # pointer to the previous node
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None # head pointer 
    
    
    #insertion at the begining
    def insertNodeBeg(self, val):
        newNode = Node(val)
        if self.head is None:
            print("list is empty, this node will be the first node")
            newNode.next = self.head 
            self.head.prev = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode   #update the head to the new node inserted 
        return self.head
    
    #insertion of node at the end
    def insertNodeEnd(self, val):
        newNode = Node(val)
        if self.head is None:
            print("list is empty, this node will be the first node")
            self.head = newNode
        else:
            # traversing to the end of the list
            current = self.head 
            while current.next is not None:
                current = current.next
            current.next = newNode
            newNode.prev = current
            
    #insertion at kth index
    def insertNodeIndex(self, index, val):
        if self.head is None:
            return "the list is empty"
        
        if index == 0:
            return self.insertNodeBeg(val)
        
        #checking index bound characterstics
        listLen = self.lenList()
        if index>listLen:
            print("the index value is higher than total nodes in the list, inserting the node at the end")
            index = listLen
        current = self.head
        for i in range(index - 1):
            if current is not None:
                current = current.next 
            else:
                raise IndexError("Index out of bound error")
        newNode = Node(val)
        newNode.next = current.next 
        if current.next is not None:
            current.next.prev = newNode
        newNode.prev = current
        current.next = newNode
    def lenList(self):
        counter = 0
        current  = self.head 
        while current is not None:
            counter += 1
            current = current.next 
        return counter
    # deleting the node
    def deleteFirstNode(self):
        if self.head is None:
            return "list is empty"
        self.head = self.head.next 
        self.head.prev = None 
        return self.head 
    # delete the end node
    def deleteEndNode(self):
        if self.head is None:
            return "list is empty"
        current = self.head 
        while current.next is not None:
            current = current.next
            
    
            
            