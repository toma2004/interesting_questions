'''
Created on Jun 5, 2015

@author: Chris Tran

Problem: Given a string of True & False and these expressions: AND, OR, XOR. Count how many number of ways to make the string to evaluate to TRUE

'''

def solve(arr):
    '''In order to solve the problem, we need to split it into subproblems like the following:
       for string i to j, how many total number of ways to evaluate this subproblem to TRUE.
       In order to know the answer, we will have a variable k running from i to j-1 and we will evaluate to
       see how many number of ways we can evaluate the expression i..k and k+1..j to be TRUE
       Time complexity is O (n3) and space is O (n2)'''
    n = len(arr)
    
    t = [[0 for i in range(n)] for j in range(n)]
    f = [[0 for i in range(n)] for j in range(n)]
    
    #initialize step. There is no k in between, so there is only one way to express this subproblem.
    for i in range(n):
        if arr[i] == "T":
            t[i][i] = 1
            f[i][i] = 0
        else:
            t[i][i] = 0
            f[i][i] = 1
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(i,j,1):
                # t[i][j] = sum( t[i][k]*t[k+1][j] AND operator
                #                total[i][k]*total[k+1][j] - f[i][k]*f[k+1][j] => OR operator, only 1 of 2 expression to be TRUE. total[i][k] = t[i][k] + f[i][k]
                #                t[i][k]*f[k+1][j] + f[i][k]*t[k+1][j]) => XOR
                
                # f[i][j] = sum( total[i][k]*total[k+1][j] - t[i][k]*t[k+1][j] => AND operator
                #                f[i][k]*f[k+1][j] OR operator
                #                t[i][k]*t[k+1][j] + f[i][k]*f[k+1][j]) => XOR
                total_ik = t[i][k] + f[i][k]
                total_kj = t[k+1][j] + f[k+1][j]
                
                temp_true = (t[i][k]*t[k+1][j])+ (total_ik*total_kj - f[i][k]*f[k+1][j]) + (t[i][k]*f[k+1][j] + f[i][k]*t[k+1][j])
                temp_false = (total_ik*total_kj - t[i][k]*t[k+1][j]) + (f[i][k]*f[k+1][j]) + (t[i][k]*t[k+1][j] + f[i][k]*f[k+1][j])
                
                t[i][j] += temp_true
                f[i][j] += temp_false
    
    print t[0][n-1]
    
myarr = ["T","F","T"]
solve(myarr)