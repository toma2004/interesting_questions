'''
Created on May 29, 2015

@author: Chris Tran

problem: Given is an array containing N numbers, which are either 1, 0 or -1. 
Find out the length of the longest contiguous subsequence going from index i to j, such that A[i]+A[i+1]..+A[j-1]+A[j] == 0.

'''

def solve(arr):
    '''Construct a new array where each element = sum of previous elements + itself
       in the original array.
       Then if there is a 0 in the new array, it indicates that subsequence from (0,k) has sum 0
       If there is a match in the array, it also indicates that subsequence from (i+1,k) has sum 0
       EX: input array = 1  4 -3 -4  6  -7  8 -5
           new array   = 1  5  2  -2  4  -3  5  0'''
    n = len(arr)
    p = [0 for i in range(n)]
    mydict = {}
    longest_sub = 0
    
    p[0] = arr[0]
    for i in range(1,n,1):
        p[i] = p[i-1]+arr[i]
     
    print p   
    for i in range(len(p)):
        if p[i] == 0:
            if longest_sub < (i-0+1):
                longest_sub = i-0+1
        else:
            try:
                val = mydict[p[i]]
                if longest_sub < (i-(val[1]+1)+1):
                    longest_sub = i-(val[1]+1)+1
            except KeyError:
                mydict[p[i]] = (p[i],i)
            
    print longest_sub
    
def longest_common_subsequence(str1,str2):
    '''The idea in for loop is that we divide the string into small substrings and check
       if last characters in both strings match, remove that last character (as it will be part of LCS) and plus 1
       else we know that either the character in str1 or character in str2 will be part of LCS. We don't know which one,
       so we will take max to see which one gives longer LCS'''
    n1 = len(str1)
    n2 = len(str2)
    sol = [[0 for i in range(n2+1)] for j in range(n1+1)]
    
    for i in range(1,n1+1,1):
        for j in range(1,n2+1,1):
            if str1[i-1] == str2[j-1]:
                sol[i][j] = sol[i-1][j-1]+1
            else:
                sol[i][j] = max(sol[i-1][j],sol[i][j-1])
    print sol[n1][n2]
    
    
    
myarr = [1,-1,1,0,1,1,-1,1,1,1,-1]
#myarr = [1,4,-3,-4,6,-7,8,-5]
solve(myarr)

str1 = ['A','G','G','T','A','B']
str2 = ['G','X','T','X','A','Y','B']
longest_common_subsequence(str1, str2)