class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None

def removeDuplicatesFromList(linkedlist):
    set_1 = set()
    curr = linkedlist.head
    prev = None 

    while curr is not None:
        if curr.data in set_1:
            prev.next = curr.next
        else:
            set_1.add(curr.data)
            prev = curr 
        curr = curr.next
        
    return linkedlist

def printSet(setVal):
    for x in setVal:
        print(x)


l1 = LinkedList()

l1.head = Node(12)
l1.head.next = Node(45)
l1.head.next.next = Node(67)

s1 = removeDuplicatesFromList(l1)

printSet(s1)

