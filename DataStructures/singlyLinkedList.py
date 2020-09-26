# tutorial: https://www.youtube.com/watch?v=RhCGA4jlPmQ&t=601s&ab_channel=TheProgrammerinYou
# Create nodes
# Create linked list
# Add nodes to linked list
# print linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def isListEmpty(self):
        if self.head is None:
            return True
        else: 
            return False
    
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length

    def insertHead(self, newNode):
        # data => Matthew, next -> None
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

    def insertAt(self, newNode, position):
        # head=>10->20->None || newNode=>15->NOne || Position=>1
        if position < 0 or position > self.listLength():
            print('Invalid Positions')
            return

        if position == 0:
            self.insertHead(newNode)
            return

        currentNode = self.head  # 10, 20
        currentPosition = 0
        previousNode = None
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def insertEnd(self, newNode):
        # head=>JOhn->None
        if self.head is None:
            self.head = newNode
        else:
            # head=>John->Ben->None || John->Mathew
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print("Linked List is empty. Delete failed")

    def deleteAt(self, position):
        currentNode = self.head
        currentPosition = 0
        previousNode = None
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def deleteEnd(self):
        if self.isListEmpty() is False:
            if self.head.next is None:
                self.deleteHead()
                return
            lastNode = self.head
            previousNode = None
            while lastNode.next is not None:
                previousNode = lastNode
                lastNode = lastNode.next
            previousNode.next = None
        else:
            print('Linked lsit is empty. Delete Failed')

    def printList(self):
        # head=>John->Ben->Matthew
        if self.head is None:
            print('List is empty')
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


# Node => data, next
# firstNode.data => John, firstNode.next => None
firstNode = Node(10)
linkedList = LinkedList()
linkedList.insertEnd(firstNode)
secondNode = Node(20)
linkedList.insertEnd(secondNode)

thirdNode = Node(15)
linkedList.insertAt(thirdNode, 2)

# linkedList.deleteEnd()
# linkedList.deleteHead()

linkedList.deleteAt(1)

linkedList.printList()
