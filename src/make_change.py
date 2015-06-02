'''
Created on Jun 1, 2015

@author: Chris Tran

problem: Given an amount of money C and some change values for coins. Construct an algorithm that gives the minimum number of coins for change

'''
import sys

def solve(money,coins):
    '''In order to come up with minimum coins for the change of final money, we need find out the minimum number of coins
       for change of some j money.
       To find min number of coins for some j money, we will take the min of the difference between j and every values in coins'''
    n = len(coins)
    
    sol = [0 for i in range(money+1)]
    min = sys.maxint
    mycoin = [0 for i in range(money+1)]
    temp = 0
    
    for i in range(1,money+1,1):
        min = sys.maxint
        for j in range(n):
            if coins[j] <= i:
                if sol[i-coins[j]]+1 < min:
                    min = sol[i-coins[j]]+1
                    temp = coins[j]
        sol[i] = min
        mycoin[i] = temp
    print sol[money]
    print mycoin
    
coins_arr=[1,5,10,25]
my_money = 91
solve(my_money,coins_arr)