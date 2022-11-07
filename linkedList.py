class Node:
    def __init__(self, data=None):
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
            print("->", end="")
            print(current.value, end="")
            current = current.next

    def append(self, data=None):
        newNode = Node(data)
        if self.count == 0:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.count += 1

    def prepend(self, data=None):
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
LL.append(20)
LL.append(21)
LL.prepend(31)
LL.printLL()
LL.removeHead()
print()
LL.printLL()
LL.removeTail()
print()
LL.printLL()
LL.removeTail()
print()
LL.printLL()
