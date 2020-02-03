# -*- coding: utf-8 -*-
"""
@Exercise - Recursion
@author: Efrain Retana
@professor: Olac Fuentes
@TA: Oscar Galindo

"""

import math

# PROBLEM 1
def sum_list(L):
    if len(L) == 0: #Base case, L is empty
        return 0
    else:
        return L[0] + sum_list(L[1:])
#-------------------------
# PROBLEM 2
def is_in_list(A,a):
    if len(A) == 0:
        return False
    if A[0] == a:
        return True
    return is_in_list(A[1:],a)
#------------------------
# PROBLEM 3
def smallest(L):
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]
    return min(L[0],smallest(L[1:]))
#----------------------------------
# PROBLEM 4
def binary(n):
    if n>1:
        return binary(int(n//2)) + str(n%2)
    return str(n % 2)
#-----------------------------------    
# PROBLEM 5
def identical(L1,L2):
    if len(L1) == 0 and len(L2)==0:
        return True
    elif len(L1) != len(L2):
        return False
    if L1[0] != L2[0]:
        return False
    return identical(L1[1:],L2[1:])
#----------------------------------
# PROBLEM 6
def reverse(L):
    if len(L) == 0:
        return []
    return [L[-1]] + reverse(L[:-1])
#----------------------------------
# PROBLEM 7
def reverse_in_place(L,first,last):
    if len(L) == 0:
        return []
    if first == last:
        return L
    swap = L[first]
    L[first] =L[last]
    L[last] = swap
    return reverse_in_place(L,first+1,last-1)
    
                
def is_sorted(L):
    return True

def print_binary(string_so_far,digits_left):
    return

def permutations(word_so_far, chars_left):
    return 

def meals(choice_so_far,starter,main,desert):
    return

if __name__ == "__main__":  
    L = [4,1,7,9,3,0,6,5,2,8]
    print(L)

    print(sum_list(L))
    print(sum_list(L[2:6]))
    
    print(is_in_list(L,3))
    print(is_in_list(L,13))
    
    print(smallest(L))
    print(smallest(L[:5]))
    
    print(binary(8))
    print(binary(15))
    
    print(identical([2,4,5],[2,4,5,7]))
    print(identical([2,4,5],[2,4,6]))
    print(identical([2,3,5],[2,5,5]))
    print(identical([2,4,5],[2,4,5]))
   
    print(reverse(L))
    print(L)
    reverse_in_place(L,0,len(L)-1)
    print(L)
    
    print(is_sorted(L))
    print(is_sorted([10,20,45,77]))
    print(is_sorted([]))
    print(is_sorted([2302]))
    
    print_binary('',2)
    print_binary('',3)
    print_binary('',4)
    
    permutations('','UTEP')
    
    meals([],['salad', 'soup', 'pasta'],['steak', 'fish','lasagna'], ['cake', 'ice cream'])
    
'''
Program Output
[4, 1, 7, 9, 3, 0, 6, 5, 2, 8]
45
19
True
False
0
1
1000
1111
False
False
False
True
[8, 2, 5, 6, 0, 3, 9, 7, 1, 4]
[4, 1, 7, 9, 3, 0, 6, 5, 2, 8]
[8, 2, 5, 6, 0, 3, 9, 7, 1, 4]
False
True
True
00
01
10
True
11
000
001
010
011
100
101
110
111
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
UTEP
UTPE
UETP
UEPT
UPTE
UPET
TUEP
TUPE
TEUP
TEPU
TPUE
TPEU
EUTP
EUPT
ETUP
ETPU
EPUT
EPTU
PUTE
PUET
PTUE
PTEU
PEUT
PETU
['salad', 'steak', 'cake']
['salad', 'steak', 'ice cream']
['salad', 'fish', 'cake']
['salad', 'fish', 'ice cream']
['salad', 'lasagna', 'cake']
['salad', 'lasagna', 'ice cream']
['soup', 'steak', 'cake']
['soup', 'steak', 'ice cream']
['soup', 'fish', 'cake']
['soup', 'fish', 'ice cream']
['soup', 'lasagna', 'cake']
['soup', 'lasagna', 'ice cream']
['pasta', 'steak', 'cake']
['pasta', 'steak', 'ice cream']
['pasta', 'fish', 'cake']
['pasta', 'fish', 'ice cream']
['pasta', 'lasagna', 'cake']
['pasta', 'lasagna', 'ice cream']
'''   
