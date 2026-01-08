class deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self,value):
        self.items.append(value)

    def deleteAtBeg(self):
        if self.isEmpty():
            print("Deque is Empty")
        else:
            return self.items.pop(0)
    
    def insertAtFront(self,value):
        self.items.insert(0,value)

    def deleteAtRear(self):
        if self.isEmpty():
            print("Deque is Empty")
        else:
            return self.items.pop()
        
dq = deque()
dq.insertAtFront(10)
dq.insertAtFront(20)
dq.insertAtFront(30)
print(dq.deleteAtBeg())
print(dq.deleteAtBeg())
print(dq.deleteAtBeg())
dq.insertAtFront(90)
dq.insertAtFront(80)
print(dq.deleteAtRear())
print(dq.deleteAtRear())
dq.deleteAtRear()
dq.deleteAtBeg()