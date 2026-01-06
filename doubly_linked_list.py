class Node():
    def __init__(self,info,prev = None, next = None):
        self.prev = prev
        self.data = info
        self.next = next

class DoublyLL():
    def __init__(self,head = None):
        self.head = head

    def InsertAtEnd(self,value):
        temp = Node(value)
        
        if(self.head != None): 
            t = self.head
            while(t.next != None):
                t = t.next
            t.next = temp
            temp.prev = temp
        else:
            self.head = temp
        
    def InsertAtBeg(self,value):
        temp = Node(value)

        temp.next = self.head
        self.head.prev = temp
        self.head = temp
    
    def InsertAtMid(self,value,x):
        temp = Node(value)
        t = self.head

        while(t.next != None):
            if(t.data == x):
               break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.prev = temp
        t.next = temp
        temp.prev = t
    
    def deleteDLL(self,value):
        if(self.head == None):
            print("list is Empty")
            return
        
        

        t = self.head
        if(t.data == value):
            self.head == t.next
            self.head.prev = None
            return
        
        while(t.next !=None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
        
        if(t.data == value):
            t.prev.next = None
        
        
    def printDLL(self):
        t = self.head
        while(t.next != None):
            print(t.data)
            t = t.next
        print(t.data)


obj = DoublyLL()
obj.InsertAtEnd(30)
obj.InsertAtEnd(20)
obj.InsertAtEnd(50)
obj.InsertAtEnd(90)
obj.InsertAtBeg(6)
obj.InsertAtMid(70,50)
obj.InsertAtMid(99,50)
obj.deleteDLL(50)
obj.printDLL()
        