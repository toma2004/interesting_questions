'''
Created on Jun 4, 2015

@author: Chris Tran

Problem: Given n integers in range 0..K. Partition this set into 2 subsets so that the difference of sums between 2 subsets is minimized.
That is min |Sum(S1) - Sum(S2)|

'''
from __future__ import division
import sys

def solve(arr,k):
    '''Initially, construct an array p(i,j) so that p(i,j) = 1 if there is a sum of a1..ai = j, else p(i,j) = 0
       let s = (sum of (S1) + sum of (S2)) / 2. Search through the array p(n,j) = 1 to find mymin = min(s-j).
       Based on mathematics, |Sum(S2) - Sum(S1)| = 2*mymin
       Time complexity is O (n2k) since i = 1..n and j = 1..nk'''
    n = len(arr)
    C = n*k
    
    p = [[0 for i in range(C+1)] for j in range(n)]
    
    #This part is somewhat similar to 0-1 knapsack problem
    #If we have a sum j, are there elements that can add up to j?
    for i in range(n):
        for j in range(C+1):
            if i == 0 and arr[i] == j: #if there is 1 item, then it is sufficient for the sum of its size
                p[i][j] = 1
                continue
            if j >= arr[i] and i != 0:
                p[i][j] = max(p[i-1][j],p[i-1][j-arr[i]]) #if the previous item already add up to j, condition satisfied. If at the previous item, we need exactly arr[i] to have sum j, condition also satisfied by adding arr[i]
            else:
                p[i][j] = p[i-1][j]

    halfsum = sum(arr[i] for i in range(n)) / 2
    mymin = sys.maxint
    
    #try to find the closest to half sum of original array
    for j in range(C+1):
        if j <= halfsum and p[n-1][j] == 1: #there is a sum to j
            if halfsum - j < mymin:
                mymin = halfsum - j
            
    print 2*mymin #based on mathematics

myarr = [1,3,4,5]
solve(myarr,5)                
    
    
     
