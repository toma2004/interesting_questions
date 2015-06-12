'''
Created on Jun 11, 2015

@author: NguyenTran

Given a string, print out all of its permutation

'''


def str_perm(str1):
    print str1
    if len(str1) == 1:
        return [str1]
    
    perms = str_perm(str1[1:])
    print perms
    mychar = str1[0]
    #print mychar
    result = []
    for perm in perms:
        for i in range(len(perms) + 1):
            result.append(perm[:i] + mychar + perm[i:])

    return result


def str_perm2(str1,first,last,count=0):
    if first == last:
        print (str1)
    else:
        for i in range(first,last+1,1):
            str1[first],str1[i] = str1[i],str1[first]
            str_perm2(str1,first+1,last,)
            str1[first],str1[i] = str1[i],str1[first]
            
#print str_perm("abc")

str_perm2(['a','b','c','d'],0,3)