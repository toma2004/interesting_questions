'''
Created on May 29, 2015

@author: Chris Tran

Problem:
Given is an array containing N numbers, A[0], A[1], ... A[N-1]. Compute the  array B of length N, such that B[i] =  A[0]*A[1]*...A[i-1]*A[i+1]...*A[N-1]. 
Algorithm should work in time  O(N), memory O(N) and can't use division.

'''

def solve(arr):
    '''In order to solve this problem, need to create 2 new arrays
       p[i] = A[0]*A[1]*...*A[i]
       s[i] = A[i]*....*A[n-1]'''
    n = len(arr)
    p = [0 for i in range(n)]
    p[0] = arr[0]
    for i in range(1,n,1):
        p[i] = p[i-1]*arr[i]
        
    s = [0 for i in range(n)]
    s[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        s[i] = arr[i]*s[i+1]
        
    sol = [0 for i in range(n)]
    for i in range(0,n,1):
        if i == 0:
            sol[i] = s[i+1]
        elif i == n-1:
            sol[i] = p[i-1]
        else:
            sol[i] = s[i+1]*p[i-1]
    
    '''Better solution to use only 1 extra array'''  
    sol2 = [0 for i in range(n)]
    temp = arr[0]
    for i in range(0,n,1):
        if i == 0:
            sol2[i] = s[i+1]
        elif i == n-1:
            sol2[i] = temp
        else:
            sol2[i] = s[i+1]*temp
            temp *= arr[i]
    print sol
    print sol2
    
myarr = [0 for i in range(10)]
for i in range(len(myarr)):
    myarr[i]=i+1
print myarr
solve(myarr)
