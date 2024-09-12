class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        curr = self.head
        while curr is not None:
            print(f"{curr.data}", end =" ")
            curr = curr.next
        print()

    def insertNodeAtHead(self, val):
        newNode = Node(val)
        if self.head is None:
            print("Empty list")
            self.head = newNode
            return self.head
        else:
            newNode.next = self.head
            self.head = newNode
            return self.head
        
    def insertNodeAtTail(self, val):
        newNode = Node(val)
        if self.head is None:
            print("List is empty")
            self.head = newNode
            return self.head
        else:
            curr = self.head 
            while curr.next is  not None:
                curr = curr.next
            curr.next = newNode
            return self.head
        
    def insertNodeAtIndex(self, index, val):
        newNode = Node(val)

        if index<0:
            raise IndexError("Index out of bound")
        
        if index==0:
            self.insertNodeAtHead(val)
            return self.head
        
        lenList = self.lengthList()

        if index>=lenList:
            print("Index greater than length of the list, inserting the node at the end.")
            index = lenList

        curr = self.head
        for i in range(index - 1):
            if curr is not None:
                curr = curr.next
            else:
                raise IndexError("Index out of bound")
        
        # Insertion logic
        newNode.next = curr.next
        curr.next = newNode
        return self.head
    
    def deleteFirstNode(self):
        if self.head is None:
            return "list is empty"
        else:
            self.head = self.head.next
        return self.head 
    
    def deleteTailNode(self):
        if self.head is None:
            return "list is empty"
        
        # handling single node
        elif self.head.next is None:
            self.head  = None
            return self.head

        else:
            #traverse to the second last node
            curr= self.head
            while curr.next.next is not None:
                curr = curr.next 
            curr.next = None
            return self.head
    
    def deleteKthNode(self, k):
        if k<0:
            raise IndexError("Index out of bound")
        
        if self.head is None:
            return "list  is empty."
        
        if k==0:
            return self.deleteFirstNode()
        
        lenList = self.lengthList()

        if k>=lenList:
            print("Index out of bound")
            raise IndexError("out of bound")
        
        curr = self.head 
        for i in range(k - 1):
            if curr is not None:
                curr = curr.next
            else:
                raise IndexError("Index out of bound")
            
        curr.next = curr.next.next
        return self.head
    
    def lengthList(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count
    

l1 = LinkedList()
n1 = Node(12)
l1.head = n1 
l1.printList()

l1.insertNodeAtHead(45)
l1.insertNodeAtTail(67)
l1.printList()
print()

l1.insertNodeAtIndex(1, 5)
l1.printList()

l1.deleteFirstNode()
l1.printList()

l1.deleteTailNode()
l1.printList() 

l1.deleteKthNode(1)
l1.printList()