'''
Created on May 30, 2015

@author: Chris Tran

Problem: Given a stream of unsorted integer, find the median element in SORTED order at any given time

This problem tests data structure reasoning (array, linked list, heap, tree, which to use?)

'''

import mydatastructure as dt

N=0
#Create 2 heaps
max_heap = dt.BinaryHeap()
min_heap = dt.BinaryHeap()

def insert_to_heaps(num):
    '''The strategy for this problem is to use 2 heaps - 1 max-heap and 1 min-heap
       why heap? Quick insertion O (log n) and don't have to move items like array
                 constant O (1) to get min and max => calculate the median
        Utilize the concept of median:
        1/ Largest of the smaller half and Smallest of the bigger half.
        2/ Those will form our median depending on the number of N'''
    
    global N
    if N % 2 == 0: #N is an even number
        max_heap.insert(-1*num)
        N += 1
        if min_heap.heap_length() <= 1:
            return #Done if there is no element in min heap
        #if there are some elements in the min_heap, need to check root
        if -1*max_heap.peek() > min_heap.peek():
            #Need to swap
            toMin = -1*max_heap.delMin()
            toMax = min_heap.delMin()
            max_heap.insert(-1*toMax)
            min_heap.insert(toMin)
    else: #if N is an odd
        max_heap.insert(-1*num)
        N += 1
        min_heap.insert(-1*max_heap.delMin())
        
def get_median():
    global N
    
    if N % 2 == 0:
        return ((-1*max_heap.peek()) + min_heap.peek()) / 2
    else:
        return (-1*max_heap.peek())
    
myarr = [4,6,8,9,3,10,2]

for i in range(len(myarr)):
    insert_to_heaps(myarr[i])
    print get_median()
    
    
            
    