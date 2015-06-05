'''
Created on Jun 4, 2015

@author: Chris Tran

Problem: Given 2 string A with length n and string B with leng m. The following actions are allowed to transform A to B with corresponding cost: delete - Cd, insert, Ci, and change Cc
Find solution that requires minimum cost

'''


def solve(str1,str2,Cd,Ci,Cc):
    '''Divide the problem into subproblem that find the minimum cost to transform str1 from 0..i into str2 from 0..j
       At i and j, here are all possible cases that can happen:
       opt(i,j) = min(1,2,3)
                  1/ Delete a letter in str1 opt(i-1,j) + Cd
                  2/ Insert a letter in str1 by removing that letter from str2 opt(i,j-1) + Ci
                  3/ if str1[i] == str2[j], no cost and continue opt(i-1,j-1)
                     if they are not the same, change them to make them the same! opt(i-1,j-1) + Cc '''
    n = len(str1)
    m = len(str2)

    sol = [[0 for i in range(m)] for j in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                if i == 0 and j == 0:
                    if str1[i] != str2[j]:
                        sol[i][j] = Cc
                elif i == 0:
                    sol[i][j] = sol[i][j-1] + Ci
                elif j == 0:
                    sol[i][j] = sol[i-1][j] + Cd
                continue
            
            if str1[i] == str2[j]:
                sol[i][j] = min(sol[i-1][j] +Cd, sol[i][j-1] +Ci, sol[i-1][j-1])
            else:
                sol[i][j] = min(sol[i-1][j] +Cd, sol[i][j-1] +Ci, sol[i-1][j-1] +Cc)
    
    print sol[n-1][m-1]
    
    
str1 = "bdeilkj"
str2 = "bcefg"
solve(str1,str2,5,2,1)
        