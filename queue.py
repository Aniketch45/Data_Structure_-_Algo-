class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def insert(self,value):
        self.items.append(value)

    def delete(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            return self.items.pop(0)
        
    
q = Queue()
q.insert(11)
q.insert(22)
q.insert(33)

print(q.delete())
print(q.delete())
print(q.delete())
print(q.delete())