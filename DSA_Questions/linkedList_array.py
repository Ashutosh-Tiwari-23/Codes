class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next 
class LinkedList:
    def __init__(self):
        self.head=None
    
#function to convert singly linked list to array
def linkedList_arr(linkedlist):
    arr = []
    curr = linkedlist.head
    while curr is not None:
        arr.append(curr.data)
        curr = curr.next
    return arr 

# function tp print an array
def printArr(arr):
    for x in arr:
        print(x, end=" ")

l1 = LinkedList()

l1.head = Node(45)
l1.head.next = Node(56)
l1.head.next.next = Node(90)

