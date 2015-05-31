'''
Created on May 30, 2015

@author: Chris Tran

problem: Given  is matrix M of size X*Y, filled with integers. Rows and columns of the  matrix are sorted in ascending order. 
Find the number of zeros in the  matrix in time O(X+Y).

'''

def solve(matrix,x,y):
    '''In order to find how many zeros are there in each ROW, we find:
       Ai = first element that is >= 0
       Bi = first element that is > 0 => number of zero = |Bi - Ai|
       
       How do we efficiently find Ai and Bi in each ROW without doing O (X*Y)?
       initialize row 1 with A1 and B1 in O (Y). Starting row 2, use A1 move to the left until find A2. Same for B2
       This will be amortized time complexity since we can move at most A1 for 2nd row (A2 for 3rd row and so on) => Total time complexity O (X + Y)'''
    
    num_zero = 0
    
    #Find A1 and B1
    a = []
    b = []
    for i in range(y):
        if not a and matrix[0][i] >= 0:
            a.append(i)
        elif not b and matrix[0][i] > 0:
            b.append(i)
            break
    if not a:
        a.append(y)
    if not b:
        b.append(y)

    num_zero += abs(b[0]-a[0])

    #go through the rest of rows to find zeros
    temp_a = 0
    temp_b = 0
    isSetA = 0
    isSetB = 0
    for i in range(1,x,1):
        #Check if index out of bound
        if a[i-1] == y:
            ja = a[i-1] - 1
        else:
            ja = a[i-1]
            
        if b[i-1] == y:
            jb = b[i-1] - 1
        else:
            jb = b[i-1]
        
        #While loop starts to move left
        while ja >= 0:
            if matrix[i][ja] >= 0:
                temp_a = ja
                isSetA = 1
            ja -= 1
        if not isSetA:
            temp_a = y
            
        
        while jb >= 0:
            if matrix[i][jb] > 0:
                temp_b = jb
                isSetB = 1
            jb -= 1
            
        if not isSetB:
            temp_b = y

        num_zero += abs(temp_b - temp_a)
        
        isSetA = 0
        isSetB = 0
        a.append(temp_a)
        b.append(temp_b)
    
    print num_zero
    
mymatrix = [[0 for i in range(4)] for j in range(3)]
mymatrix[0][0] = -6
mymatrix[0][1] = -5
mymatrix[0][2] = -4
mymatrix[1][0] = -5
mymatrix[1][1] = -3
mymatrix[1][2] = -1
print mymatrix
solve(mymatrix,3,4)
            