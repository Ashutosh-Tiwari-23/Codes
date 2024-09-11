class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

def middleNode(linkedlist):
    curr = linkedlist.head
    counter = 0

    # Step 1: Count the number of nodes in the linked list
    while curr is not None:
        counter += 1
        curr = curr.next

    # Step 2: Handle empty list
    if counter == 0:
        print("The list is empty")
        return None

    # Step 3: Calculate the middle index
    middle_index = counter // 2

    # Step 4: Traverse to the middle node
    curr = linkedlist.head
    for i in range(middle_index):
        if curr is not None:
            curr = curr.next
        else:
            print("Index out of bound")
            return None
    
    # Step 5: Return the middle node
    return curr

# Example Usage:
# Create a LinkedList and add nodes
l1 = LinkedList()
l1.head = Node(12)
l1.head.next = Node(45)
l1.head.next.next = Node(67)
l1.head.next.next.next = Node(89)  # Example list with 4 nodes

# Find and print the middle node
middle = middleNode(l1)
if middle:
    print("Middle node data:", middle.data)
