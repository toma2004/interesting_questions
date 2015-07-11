'''
Created on Jul 10, 2015

@author: Chris Tran

Problem: counting inversion in a given array of integer

'''

def merge_sort (arr, first, last):
        num_inversion = 0
        if (first >= last):
            return num_inversion
        
        mid = (first+last)/2
        num_inversion = merge_sort(arr, first, mid)
        num_inversion += merge_sort(arr, mid+1, last)
        num_inversion += merge(arr,first,mid,last)
    
        return num_inversion
    
def merge (arr, first, mid, last):    
    left = first
    right = mid + 1
    temp = [0 for i in range(last+1)]
    index = first
    num_inversion = 0
    
    while (left <= mid) and (right <= last):
        if (arr[left] <= arr[right]):
            temp[index] = arr[left]
            left += 1
        else:
            temp[index] = arr[right]
            right += 1
            num_inversion += (mid+1-left)
        index += 1
            
    while left <= mid:
        temp[index] = arr[left]
        index += 1
        left += 1
    
    while right <= last:
        temp[index] = arr[right]
        index += 1
        right += 1
        
    for i in range(first,last+1):
        arr[i] = temp[i]
          
    return num_inversion
    
arr=[1,4,3,5,10,2]
print merge_sort(arr,0,len(arr)-1)
print arr
