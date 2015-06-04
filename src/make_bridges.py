'''
Created on Jun 3, 2015

@author: Chris Tran

Problem: Given n cities on a northern bank and their corresponding n cities on a southern bank of a river.
Find the maximum number of bridges that can be built to connect 2 corresponding cities with the condition that no two bridge can cross

'''
import longest_subsequence_index as lsi

def solve(south,north):
    '''This is a variable of longest increasing subsequence problem
       First of all sort cities by coordinates in either north or south banks. Then find its corresponding 
       coordinate on another bank. Then find the longest increasing subsequence'''
    
    south.sort()
    mydict = {}
    
    ns = len(south)
    nn = len(north)
    
    sol = []
    
    for i in range (nn):
        mydict[north[i]] = i
    
    for i in range (ns):
        sol.append(mydict[south[i]])
    
    #find longest increasing subsequence on sol array
    lsi.longest_increasing_subsequence(sol)
    
arr1 = [1,3,2,4]
arr2 = [3,2,4,1]

solve(arr1,arr2)