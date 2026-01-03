#how to measure time complexity

# 1) Constant time
num = 4
print(num)
if(num==5):                       # y=4
    print("Hi")                   # O(1)
else:
    print("Welcome")

# 2) Linear Time
n = 4 # 1 unit              1 + 1 + n + n
print(n)  # 1 unit         #y = 2n+10  = O(n)
for i in range(n):  # n unit
    print("Hello")  # n unit          


n = 5      # 1 unit
m = 9      # 1 unit
print(n)     # 1 unit                         1+1+1+n+n+n+n = O(n)
for i in range(0,n):  # n unit
    print(i)          # n unit
for i in range(0,m):  # n unit
    print(i)          # n unit
for i in range(0,n/2): # O(n/2)
    print(i)            # O(n/2)

# 3) Quadratic time complexity
n = 6         # 1 unit
m = 8       # 1 unit                            n*n = O(n^2)
print(n)     # 1 unit
for i in range(n):       # n times       6 times
    for j in range(m):  # m times        
        print(i)        # n * m times     48 times

# 4) Cubic Time complexity
n = 6         # 1 unit
m = 8       # 1 unit                            n*n*n times = O(n^3)
print(n)     # 1 unit       ->O(1)
for i in range(n):       # n times       6 times
    for j in range(m):  # m times   
        for k in range(n):  #n times
            print(i)        # n * m * n times       -> O(n^3)   Highest dominating time Complexity we consider

for k in range(n):  #n times
            print(i)       # ->O(n)

#example
n = 5
if(n==5):
     # O(n^2)
else:              # O(n^3)      we consider highest worst case because user can give any input
     # O(n^3)


# 5) Logarithmic Time
num2 = 10             # n=10, n=5, n=2, n=1, n=0
while(num2>=1):       # hi, hi, hi, hi
     print("hi")    # k times
     num2//=2                       # O (log n)   loop is getting half then time complexity always (log n)

     # n/2^1, n/2^2, n/2^3,........., n/2^k = 1
     # n = 2^k
     # log n = log 2^k
     # log n = k log 2
     # k = log n / log 2 #ignore constant
     # k = log n 

