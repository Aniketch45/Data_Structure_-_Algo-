class Node:
    def __init__(self,info,prev = None,next = None):
        self.prev = prev
        self.data = info
        self.next = next

class CricularLL:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self,value):
        temp = Node(value)

        if self.head != None:
            t1 = self.head
            while(t1.next !=None):
                t1 = t1.next
            t1.next = temp
            # temp.prev = t1
            # temp.next = self.head
            self.head = temp
        else:
            self.head = temp
            temp.next = temp
            temp.prev = temp
        
    def printDLL(self):
        t = self.head
        while(t.next != self.head):
            print(t.data)
            t = t.next
        print(t.data)


# def inseratBeg


c = CricularLL()
c.InsertAtEnd(10)
c.InsertAtEnd(34)
c.InsertAtEnd(88)
c.InsertAtEnd(55)
c.InsertAtEnd(67)
c.InsertAtEnd(44)
c.printDLL()

