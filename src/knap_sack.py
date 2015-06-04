'''
Created on Jun 3, 2015

@author: Chris Tran

Problem: Given n items with value v and weight w, find the optimal way to have maximum value in knapsack

'''

def solve_knapsack(arr,C):
    '''We can use multiple copies of an item - consider easy problem requires less space O (C) space to re-construct the optimal array
       divide this problem into smaller problem with capacity i.'''
    n = len(arr)
    
    sol = [0 for i in range(C+1)]
    item = [(0,0) for i in range(C+1)]
    for i in range(1,C+1,1):
        mymax = -1
        for j in range(n):
            if arr[j][0] <= i:
                if sol[i-arr[j][0]] + arr[j][1] > mymax:
                    mymax = sol[i-arr[j][0]] + arr[j][1]
                    myitem = arr[j]
        sol[i] = max(sol[i-1],mymax)
        if sol[i] == mymax:
            item[i] = myitem
    
    print sol[C]
    index = C
    while index >= 0:
        if item[index] != (0,0):
            print item[index]
        if index == 0:
            break
        index = index-item[index][0]
    

def zeroOne_knapsack(arr,C):
    '''For this knapsack problem, we can't use duplicate items. 0-1 means that we either use that item or we don't
       The time complexity of this problem is the same as the problem above O (nC), but the space complexity is much more O (nC)
       The trick to solve this problem is to use 2D array as oppose to using 1D array like other DP problems'''
    n = len(arr)
    sol = [[0 for i in range(C+1)] for j in range(n)]
    item = [[(0,0) for i in range(C+1)] for j in range(n)]
    
    for i in range(n):
        for j in range(1,C+1,1):
            if i == 0 and arr[i][0] <= j: #Since there is only 1 element in the array, it does not matter how much capacity we have, we can only fill in 1 item. Also make sure that the item can fit in knapsack
                sol[i][j] = arr[i][1]
                item[i][j] = arr[i]
            if arr[i][0] <= j and i != 0:
                sol[i][j] = max(sol[i-1][j], sol[i-1][j-arr[i][0]] + arr[i][1])
                if sol[i][j] == sol[i-1][j-arr[i][0]] + arr[i][1]:
                    item[i][j] = arr[i]
            else: #an item can't fit in the knapsack with capacity j
                sol[i][j] = sol[i-1][j]
    print sol[n-1][C]
    
    index1 = n-1
    index2 = C
    while index1 >= 0 and index2 >=0:
        if item[index1][index2] != (0,0):
            print item[index1][index2] 
        if index1 == 0:
            break
        index2 = index2 - item[index1][index2][0]
        index1 -= 1

myarr = [(1,1),(3,5),(4,1),(5,5)]
solve_knapsack(myarr,8)
zeroOne_knapsack(myarr,8)
