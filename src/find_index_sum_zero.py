'''
Created on May 30, 2015

@author: Chris Tran

Problem: Given  is array A containing N numbers. Find three different indexes i,j,k,  such that A[i]+A[j]+A[k] == 0. 
Algorithm should work in time O(N^2).

'''

def solve(arr):
    '''Fix i, then let j = i+1 and k = N-1.
       if sum > 0 => k--, else if sum < 0, j++. if sum == 0, done!
       if j==k and sum is not yet zero, fix i to the next value'''
    n = len(arr)
    arr.sort() # O (n log n)
    k = n - 1
    for i in range(n): # O (n2)
        j = i + 1
        while j != k:
            sum = arr[i]+arr[j]+arr[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                print i,j,k
                return
            
myarr = [5,8,6,7,-11]
solve(myarr)