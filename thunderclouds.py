#n = 8
#k = 2
#c = [0, 0, 1, 0, 0, 1, 1, 0]

import math


n=16
k=1
c= [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# time limit excided
def jumpingOnClouds(c, k):
    n = len(c)
    i = 0
    e = 100
    while i < n:
        v = (i+k)%n
        print(i,'---------------------',v)
        if v >= 0:
            if c[v] == 0:
                e -= 1
            else:
                e = e - 1 - 2

        if i == n-1 or v !=0:
            i = v
        else:
            i = i + k

    return e
    
    
def jumpingcloud(c, k):
    cur = 0
    e = 100
    while True:
        if c[cur]==1:
            e-=2
        e-=1
        cur = (cur+k)%n
        if cur==0:
            break
    print(e)



#jumpingcloud(c, k)
    


        
#n= 10 
#k = 3
#c = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]

#print(jumpingOnClouds(c, k))



def findDigits(n):
    c= 0
    num = n
    while n > 0:
        rem = n % 10
        if rem != 0:
            if(num%rem == 0):
                c += 1    
        n = n//10    
    return c

#print(findDigits(124))

def extraLongFactorials(n):
    i = 1
    val = n
    while i < n:
        val = val * (n-i)
        i += 1 
        
    return val

#print(extraLongFactorials(45))


#print(math.sqrt(24).is_integer)

def squares(a, b):
    l = []
    for i in range(a, b+1):
        sqrt_num = math.sqrt(i)
        if sqrt_num.is_integer():
            l.append(i)
    return len(l)

        


print(squares(24,49))

