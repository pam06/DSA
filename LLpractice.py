class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def printLL(self):
        current = self.head
        print(current.value, end="")
        current = current.next
        while current is not None:
            print("->", current.value, end="")
            current = current.next

    def appendLL(self, data):
        newNode = Node(data)
        if self.count == 0:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.count += 1

    def prepandLL(self, data):
        newNode = Node(data)
        temp = self.head
        newNode.next = temp
        self.head = newNode
        self.count += 1
        if self.count == 1:
            self.tail = self.head

    def removeHead(self):
        if self.count > 0:
            self.head = self.head.next
            self.count -= 1
            if self.count == 0:
                self.tail = None

    def removeTail(self):
        if self.count > 0:
            if self.count == 1:
                self.head = self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current
                self.count -= 1


LL = LinkedList()
LL.appendLL(10)
LL.appendLL(20)
LL.prepandLL(30)
LL.removeHead()
LL.removeTail()
LL.printLL()

