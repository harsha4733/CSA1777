X = [[1,1,1],
    [2 ,2,2],
    [3 ,3,3]]
 
Y = [[3,3,3],
    [2,2,2],
    [1,1,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)
