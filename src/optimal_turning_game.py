'''
Created on Jun 5, 2015

@author: Chris Tran

Problem: Given n coins (assuming n is an even number) with value v(1)..v(n), compute the maximum amount of money I can get if I play the game where if it's my turn I can take either
the first coin or the last coin

'''

def solve(arr):
    '''This problem involves the opponent, so we have to make some assumptions
       Of course we will try to maximize our total by picking the larger value of first or last coin. But we also need to consider what we have left AFTER our opponent pick
       We assume our opponent is smart and pick the maximum in his turn, this will leave us the minimum for our next turn'''
    n = len(arr)
    sol = [[0 for i in range(n)] for j in range(n)]
    item = [[0 for i in range(n)] for j in range(n)]
    
    for gap in range(n):
        i = 0
        for j in range(gap,n,1):
            if i == j:
                sol[i][j] = arr[i]
                item[i][j] = arr[i]
           
            if j > i:
                if j - i == 1:
                    sol[i][j] = max(arr[i],arr[j])
                    
                    if sol[i][j] == arr[i]:
                        item[i][j] = arr[i]
                    else:
                        item[i][j] - arr[j]
                else:
                    sol[i][j] = max(arr[i] + min(sol[i+1][j-1],sol[i+2][j]), arr[j] + min(sol[i+1][j-1],sol[i][j-2]))
                   
                    if sol[i][j] == arr[i] + min(sol[i+1][j-1],sol[i+2][j]):
                        item[i][j] = arr[i]
                    else:
                        item[i][j] = arr[j]  
            i += 1
            
    print sol[0][n-1]
    
myarr = [8,15,3,7]
solve(myarr)