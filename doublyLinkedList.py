class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # Creation of doubly linked lists

    def createDLL(self, nodeValue):
        node = Node(nodeValue)     #O(1)
        node.prev = None            #O(1)
        node.next = None                #O(1)
        self.head = node                #O(1)
        self.tail = node                    #O(1)
        return "The DLL is created successfully"

doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)

print([node.value for node in doublyLL])