class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    #insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:   #O(1)
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  
                newNode.next = self.head  #O(1)
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode   #O(1)
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next    #O(n) total time complexity 
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode    #O(1)
                newNode.next = nextNode


singlyLinkedList = SlinkedList()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(0,0)
print([node.value for node in singlyLinkedList])