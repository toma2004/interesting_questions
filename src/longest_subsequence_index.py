'''
Created on May 29, 2015

@author: Chris Tran

problem: Given is an array containing N numbers, which are either 1, 0 or -1. 
Find out the length of the longest contiguous subsequence going from index i to j, such that A[i]+A[i+1]..+A[j-1]+A[j] == 0.

'''
from __future__ import division
import sys

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
            
    print "solution for problem 1: ",longest_sub
    
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
    print "solution for problem 2: ",sol[n1][n2]
    
def max_sum_contiguous_subsequence(arr):
    '''Given an array, find the subsequence in the array that gives the maximum sum
       Use DP, we can construct a recurrence formula as below:
       at sub problem i, we can either include i to make sum bigger or keep i since it's already bigger than the sum'''
    n = len(arr)
    sol = [0 for i in range (n)]
    
    for i in range(1,n,1):
        sol[i] = max(sol[i-1]+arr[i],arr[i])
    
    print "solution for problem 3: ",sol[n-1]
    
def longest_increasing_subsequence(arr):
    '''Given an array with lenth n, find the maximum length of longest increasing subsequence (not necessarily contiguous)
       Big O (n2)'''
    n = len(arr)
    if n == 0:
        print 0
    sol = [0 for i in range(n)]
    toprint = [0 for i in range(n)]
    sol[0] = 1
    temp = 0
    for i in range(1,n,1):
        mymax = -sys.maxint-1
        for j in range(i):
            if arr[i] > arr[j]:
                if mymax < sol[j]+1:
                    mymax = sol[j]+1
                    temp = j
        if mymax < 1:
            sol[i] = 1 #start new subsequence, consider this array [3,1,0,2] where the first element is not part of LIS
            toprint[i] = i
        else:
            sol[i]=mymax
            toprint[i] = temp #predecessor number
    
    print "solution for problem 4: ", max(sol[i] for i in range(n))
    max_index = sol.index(max(sol))
    print "longest increasing subsequence for problem 4: "
    atemp = 0
    while max_index >= 0:
        print arr[max_index]
        if max_index == 0:
            max_index -= 1
            continue
        max_index = toprint[max_index]
        if max_index == atemp:
            break
        atemp = max_index

def findIndex(arr,f,l,val):
    '''Binary search'''
    while l>f:
        m = (l-f)//2
        if arr[m] >= val:
            f = m
        else:
            l = m
    return l
    
def efficient_LIS(arr):
    n = len(arr)
    if n == 0:
        print 0
    lastElem = [0 for i in range(n)]
    lastElem[0] = arr[0]
    mylen = 1
    
    for i in range(n):
        if arr[i] < lastElem[0]:
            lastElem[0] = arr[i]
        elif arr[i] > lastElem[mylen-1]:
            lastElem[mylen] = arr[i]
            mylen += 1
        else:
            myindex = findIndex(lastElem,0,mylen,arr[i])
            lastElem[myindex] = arr[i]
    
    print "Solution for efficient longest subsequence: ",mylen

if __name__ == "__main__":
    myarr = [1,-1,1,0,1,1,-1,1,1,1,-1]
    #myarr = [1,4,-3,-4,6,-7,8,-5]
    solve(myarr)
    
    str1 = ['A','G','G','T','A','B']
    str2 = ['G','X','T','X','A','Y','B']
    longest_common_subsequence(str1, str2)
    
    anArr = [1,3,-4,9]
    max_sum_contiguous_subsequence(anArr)
    anArr1 = [1,3,2,7,4,5,3]
    #anArr1 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    longest_increasing_subsequence(anArr1)
    efficient_LIS(anArr1)