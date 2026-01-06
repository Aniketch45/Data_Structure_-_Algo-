# class stack:
#     def __init__(self):
#         self.li = []

#     def length(self):
#         return len(self.li)
    
#     def push(self,value):
#         self.li.insert(0,value)

#     def peek(self):
#         if len(self.li) == 0:
#             raise Exception("Stack is Empty")
#         else:
#             return self.li[0]
        
#     def pop(self):
#         if len(self.li) == 0:
#             raise Exception("Stack is Empty")
#         else:
#             return self.li.pop(0)
        
# stk = stack()
# stk.push(20)
# stk.push(90)
# stk.push(30)
# stk.push(88)
# print(stk.peek())
# print(stk.pop())
# print(stk.pop())

class stack():
    def __init__(self):
        self.s = []

    def lenght(self):
        return len(self.s)

    def push(self,value):
        self.s.append(value)

    def pop(self):
        if(len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
            return self.s.pop()
        
    def peek(self):
        if(len(self.s) == 0):
            raise Exception("Stack is Empty")
        else:
            return self.s[-1]
        
stk = stack()
stk.push(20)
stk.push(30)
stk.push(40)
print(stk.peek())
print(stk.pop())

