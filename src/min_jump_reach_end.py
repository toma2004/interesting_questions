'''
Created on Jun 1, 2015

@author: Chris Tran

Problem: Given an array of integers where each element represents the max number of steps that can be made forward from that element. 
Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). 
If an element is 0, then cannot move through that element.

'''
import sys

def solve(arr):
    '''Use DP and recurrence formula
       let OPT(i) be minimum number of steps to reach index i
       Will check in ascending order of index before i to see at which index we can reach i'''
    
    n = len(arr)
    
    sol = [0 for i in range(n)]
    for i in range(1,n,1):
        sol[i] = sys.maxint
        #calculate min number of jump we need to reach i
        for j in range(i):
            if(i <= j+arr[j] and sol[j] != sys.maxint):
                sol[i] = min(sol[i], sol[j]+1)
                break; #don't care about other paths since it will be the same or longer
    
    print sol[n-1]
    
    
myarr = [1,3,5,5,3,2,1,1,1,9]
solve(myarr)