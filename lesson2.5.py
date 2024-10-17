def get_matrix (n,m, value):
    matrix = []
    if n <= 0 or m <=0 or value <= 0:
        return matrix
    for i in range (n):
        matrix.append([])
        for j in range (m):
            matrix [i].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)




















    #n = [1,2,3,4,5,6]
    #win1 = random.choice(n)
    #n.remove(win1)
    #win2 = random.choice(n)
    #print(n,m,value)
    #return win1, win2

#win1, win2 = get_matrix('n', 'm', 'value')
#print(win1, win2)

