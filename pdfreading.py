from copy import copy
from math import floor


letter = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4,'e' : 5,'f' : 6,'g' : 7,'h' : 8, 'i' : 9, 'j' : 10,'k' : 11, 'l' : 12,'m' : 13, 'n' : 14, 'o' : 15,'p' : 16, 'q' : 17,'r' : 18,'s' : 19,'t' : 20,'u' : 21, 'v' : 22,'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26}

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = 'abc'
l = len(word)
l1 = []
for i in word:
    if i in letter.keys():
       ind_value =  letter[i]
       l1.append(h[ind_value-1])

m = max(l1)

result = m * l

#print(result)
    


def utopianTree(n):
    height = 1
    if n == 0:
        return height
    
    for i in range(1,n+1):
        print(i)
        if i % 2 == 0:
            height = height + 1      
        else: 
            height = height * 2    

    return height 

#print(utopianTree(4))







def angryProfessor(k, a):
    count = 0  
    for s in a:
        if s <= 0:
            count = count + 1

    
    print(count)
    
    if count >= k:
        return 'NO'
    else: 
        return 'YES'


k = 2
a= [0, -1, 2, 1]




#print(angryProfessor(k, a))

def beautifulDays(i, j, k):
    count = 0
    for n in range(i,j+1):
        n1 = n
        rev = 0 
        while n > 0:
            rem = n % 10
            rev = (rev * 10) + rem
            n = n // 10

        if (abs(n1 - rev))% k == 0 or (abs(n1 - rev))/ k == 0:
            count += 1
                
    return count


#print(beautifulDays(20,23,6))

def viralAdvertising(n):
    total_like = 0 
    like = 2 
    for i in range(1,n+1): 
        if i == 1:
            total_like = total_like + like
        else:
            shared = like * 3
            like = floor(shared / 2)
            total_like = total_like + like
            
    return total_like

#(viralAdvertising(5))


def saveThePrisoner(n, m, s): 
    
    return 1 + (s+m-2) % n
    
 
#print(saveThePrisoner(4, 6, 2))

def circularArrayRotation(a, k, queries):
    while k > 0:
        a.insert(0, a.pop(len(a)-1))
        k -= 1

    for i in queries:    
        result = a[i]        
    return result
    
        


            

a = [3,4,5]
queries=[0,1,2]

#print(circularArrayRotation(a,2,2))
            
def permutationEquation(p):
    x = len(p)
    y = []
    for i in range(1,x+1):
        idx = p.index(i) + 1
        y.append(p.index(idx) + 1)
    
    return y

p = [4, 3, 5, 1, 2]
print(permutationEquation(p))
        
        


        



    