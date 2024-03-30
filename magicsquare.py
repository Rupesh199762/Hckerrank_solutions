from re import X
from tkinter import N


def magicsquare(n):
    
    a = []
    for r in range(n):
        a.append([])
        for _ in range(n):
            a[r].append(0)

       
    x = n//2
    y = n-1
    i = 1

    while(i <= n*n):
        if x == -1 and  y == n:
            x = 0
            y = n -2

        elif x == -1:
            x = n - 1
        
        elif y == n:
            y = 0

        if a[x][y] != 0:
            x = x +  1
            y = y -  2
            continue
           
        else:
            a[x][y] = i
            
        x = x - 1
        y = y + 1 
        i = i + 1

    sum = n*(n * n + 1)//2

    return sum, a
 

        
            
print(magicsquare(3))
print(magicsquare(5))



