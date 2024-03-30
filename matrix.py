def elements(N):
    ele = []
    for i in range(1,N**2 + 1):
        ele.append(i)
    return ele

def generatematrix(N):
    numbers = elements(N)
    M = []
    factor = 0
    for i in range (0,N):
        row = [] 
        for j in range(factor * N, (factor + 1)*N):
            row.append(numbers[j])        
        factor += 1
        M.append(row)
        i += 1
    return M

print(generatematrix(3))
print(generatematrix(5))
print(generatematrix(4))
print(generatematrix(30))




