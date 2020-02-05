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
    # grabs a list and sums all of its elements
    if len(L) == 0: #Base case, L is empty
        return 0
    else:
        return L[0] + sum_list(L[1:])
#-------------------------
# PROBLEM 2
def is_in_list(A,a):
    #
    if len(A) == 0: # Base case, if A is empty
        return False
    if A[0] == a:
        return True
    return is_in_list(A[1:],a)
#------------------------
# PROBLEM 3
def smallest(L):
    # grabs a list and returns the smallest element in the list
    if len(L) == 0: # if L is empty
        return 0
    elif len(L) == 1:
        return L[0]
    return min(L[0],smallest(L[1:]))
#----------------------------------
# PROBLEM 4
def binary(n):
    if n>1: # base case to run while n > 1
        # split n by a (floor) int then find modulus then add the modulus of n
        # to the return
        return binary(int(n//2)) + str(n%2)
    return str(n % 2)
#-----------------------------------    
# PROBLEM 5
def identical(L1,L2):
    #
    if len(L1) == 0 and len(L2)==0: # base case to check when both lists are the same size
        return True
    elif len(L1) != len(L2): # if both are not the same size then false
        return False
    # checks each element through each recursive call
    if L1[0] != L2[0]:
        return False
    return identical(L1[1:],L2[1:])
#----------------------------------
# PROBLEM 6
def reverse(L):
    if len(L) == 0: # base case to check when L is empty
        return []
    # return the last element of each recursive call
    return [L[-1]] + reverse(L[:-1])
#----------------------------------
# PROBLEM 7
def reverse_in_place(L,first,last):
    if len(L) == 0: # when L is empty
        return []
    # when both pointers cross, reverse should end
    if first >= last:
        return L
    # swap the first and last elements, then increase the first pointer and decrease
    # the last pointer
#    swap = L[first]
#    L[first] =L[last]
#    L[last] = swap
    L[first],L[last] = L[last],L[first]
    return reverse_in_place(L,first+1,last-1)
#--------------------------------------
# PROBLEM 8
def is_sorted(L):
    if len(L) <= 1: # base case to check when there is 1 element or less
        return True
    # compare first and last element and if they are sorted continue check from L[1:]
    return L[0] < L[1] and is_sorted(L[1:])
#--------------------------------------
# PROBLEM 9
def print_binary(string_so_far,digits_left):
    if digits_left == 0:
        print(string_so_far)
    else:
        print_binary(string_so_far + '0' ,digits_left - 1)
        print_binary(string_so_far + '1',digits_left - 1)
    # once the string is equal to the number of digits, display the possible combination
#    if len(string_so_far) == digits_left:
#        print(string_so_far)
#        return
#    # run a loop to add a '0' or '1' to all possible positions in strings_so_far
#    for num in '01':
#        print_binary(string_so_far + num,digits_left)
#------------------------------------
# PROBLEM 10
def permutations(word_so_far, chars_left):
    if len(chars_left) == 0: # when the amount of characters left is 0, display the word_so_far
        print(word_so_far)
        return
    # run a loop for the len of chars_left to create a combination of n-1 (amount of letters)
    # then create a recursive call to permutate the element in each pos
    for letter in range(len(chars_left)):
        combination = chars_left[0:letter] + chars_left[letter + 1:]
        permutations(word_so_far + chars_left[letter:letter+1],combination)
    
#-------------------------------------
# PROBLEM 11

def meals(choice_so_far,starter,main,desert):
    if len(choice_so_far) == 0:
        for i in range(len(star))
        

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
