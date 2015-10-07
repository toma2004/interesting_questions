#!/usr/bin/env python
'''
Created on Oct 7, 2015

@author: Chris Tran
'''
from __future__ import division

class hash_map:
    def __init__(self, size):
        self.mytable = [[] for i in range(size)] #initialize table
        self.numEle = 0 #total number of element in my hash table
        self.tableSize = size
        
    def set(self,key,value):
        #since table is fixed in size, we can't add anything to the table if it is already fully filled up
        if (self.numEle >= self.tableSize):
            return False
        key_hash_val  = hash(key)
        #store key into table
        self.mytable[(key_hash_val%self.tableSize)].append((key,value))
        self.numEle += 1
        return True
    
    def get(self,key):
        key_hash_val = hash(key)
        #Now go to the index of this list and go through all elements of the list to find the key
        for i in self.mytable[(key_hash_val%self.tableSize)]:
            if (i[0] == key):
                return i[1]
        return None
    
    def delete(self,key):
        key_hash_val = hash(key)
        #Now go to the index of this list and go through all elements of the list to delete the key
        for i in self.mytable[(key_hash_val%self.tableSize)]:
            if (i[0] == key):
                return_val = i[1]
                self.mytable[(key_hash_val%self.tableSize)].remove(i)
                self.numEle -= 1
                return return_val
        return None
    
    def load(self):
        #return load based on number of element/table size
        return self.numEle/self.tableSize
    
    def print_hash(self):
        print self.mytable;
    
#Test case
if __name__ == "__main__":
    #Ask user input for table size
    print "Test case 1 is an example of a normal hash table where the number of inputs are less than the table size"
    print "Test case 2 is an example of a saturated hash table where the number of inputs are equal or more than the table size"
    ans = raw_input("Please select test case (1 or 2): ")
    tableSize = 0
    if (ans == "1"):
        tableSize = 10
    elif (ans == "2"):
        tableSize = 2
    else:
        print "Please enter a valid test case"
        exit(1)
        
    #constructor a new hash table
    myhashtable = hash_map(tableSize)
    
    print "Now begin set operations"
    #sample (key,value) pair to be added
    sample_list = [('apple',100), ('orange', 50), ('banana',15), ('tangerine', 22)]
    
    for i in sample_list:
        print "Adding key %s into my hash table..." % (i[0])
        if not myhashtable.set(i[0],i[1]):
            print "ERROR: Could not add to the hash table since it is already full. Please consider to increase the table size"
        else:
            print "Added successfully"
    
    #Print after set operation
    print "After set operations, our hash table looks like:"
    myhashtable.print_hash()
    #print load
    print "Current load of hash table = %.2f" % (myhashtable.load())
    
    print "Now begin get operations"
    print "Getting value for key string apple... \n", myhashtable.get('apple')
    print "Getting value for key string banana... \n", myhashtable.get('banana')
    print "Getting value for key string notInTable... \n", myhashtable.get('notInTable')
    #print after get operation
    print "After get operations, our hash table looks like:"
    myhashtable.print_hash()
    
    print "Now begin delete operations"
    print "Deleting value that has key string tangerine... \n", myhashtable.delete('tangerine')
    print "Deleting value that has key string notInTable... \n", myhashtable.delete('notInTable')
    #print after delete operation
    print "After delete operations, our hash table looks like:"
    myhashtable.print_hash()
    
    #print load
    print "Current load of hash table = %.2f" % (myhashtable.load())