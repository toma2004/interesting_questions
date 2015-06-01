'''
Created on May 31, 2015

@author: NguyenTran

Problem: Given about 4 billions 32-bit integer. How do determine a number n which has appeared twice in the data set
Try to use as least space as possible

'''

def solve(myfile):
    '''4x10^9 x 4 = 16GB total to save all those integer.
       Let's split the 32-bit integer into prefixes and suffixes with 16-bit each.
       Then we only need 2^16 = 8MB space. If we need less space, decrease the bit size
       with the cost of increasing number of passes through the file
       The algorithm is:
       1/ Count how many integer in the file has each prefix. Stop when we have a prefix that has more than 2^16 counts
       Why? Assuming they are all distinct integer, a prefix can have maximum of 2^16 counts for different suffixes
       2/ Count how many integer with prefix p found in 1/ has each suffix. Return the number of the suffix is re-visited
       '''
    #Create an array with size 2^16 and intialize to ZERO
    limit = 1<<16
    arr = [0 for i in range(limit)]
    print len(arr)
    return
    for n in myfile:
        p=n>>16
        arr[p] += 1
        if arr[p] > limit:
            #found a prefix of the desired integer
            break
    
    arr = [0 for i in range(limit)]
    #second pass through the file to find the integer that has appeared twice
    p <<= 16 #make p becomes 32-bit integer
    for n in myfile:
        #to find correct suffix, n XOR p
        s = n^p
        if s < limit: #this is to check if the number n has the same prefix p
            if arr[s] >= 1:
                return n #found my number
            arr[s] += 1

            