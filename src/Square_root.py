'''
Created on May 29, 2015

@author: Chris Tran

Problem: Given is number N. Create a function that calculates sqrt(N)

'''
from __future__ import division
import math
import time

print math.sqrt(1000)


def cal_sqrt(number):
    '''Binary search approach'''
    #guess number by x^2 - c =~ 0
    initial = 0
    last = number
    epsilon = 0.00001
    mid_prev = 0

    while 1:
        mid = (last + initial)/2
        p = mid * mid
        if p == number:
            return mid
        elif p > number:
            last = mid
        else:
            initial = mid
        
        if abs(mid - mid_prev) < epsilon: #approximate
            return mid
        mid_prev = mid
        
def newton_cal_sqrt(number):
    '''this use Newton's method to calculate a square root
       s < sqrt(x) < x/s => find (s+x/s)/2'''
    s_prev = 0
    s = 1
    while 1:
        s = (s + number/s) * 0.5
        if s == s_prev:
            return s
        s_prev = s
start = time.clock()
print cal_sqrt(1000)
print time.clock() - start, "seconds"
start = time.clock()
print newton_cal_sqrt(1000)
print time.clock() - start, "seconds"
