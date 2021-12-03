#!/usr/bin/env python
# coding: utf-8


# Ans 2 -> Fuzzy Implementation.

def  union(a,b):
    u = dict()
    for i in a:
        if i in b:
            u[i] = max(a[i],b[i])
        else:
            u[i] = a[i]
    for i in b:
        if i not in a:
            u[i] = b[i]
    return u


def intersection(a,b):
    inter=dict()
    for i in a:
        if i in b:
            inter[i]=min(a[i],b[i])
        else:
            inter[i] = a[i]
    for i in b:
        if i not in a:
            inter[i] = b[i]
    return inter


def complement(a):
    comp = {}
    for i in a:
        comp[i] = round(1-a[i],1)
    return comp



def difference(a,b):
    comp_b = complement(b)
    dif  = intersection(a,comp_b)
    return dif


def de_morgan(a,b):
    p = intersection(a,b)
    p_comp = complement(p)
    a_comp = complement(a)
    b_comp = complement(b)
    q = union(a_comp,b_comp)
    
    if(p_comp == q):
        print("(A n B)' =",p_comp)
        print("A' u B = ",q)
        print("Thus, (A n B)' = A' u B'")
        
    print()

    p = union(a,b)
    p_comp = complement(p)
    q = intersection(a_comp,b_comp)
    if(p_comp == q):
        print("(A u B)' = ",p_comp)
        print("A' n B' = ",q)
        print("Thus (A u B)' = A' n B'")
    
print()


a = []
n=input("Enter the elements of set A = ")
a=n.split(',')
print("Enter the membership value for each element")
mem_a = {}
for i in a:
    mem_a[i] = float(input(f"{i}: "))
print("A = ",mem_a)


b=[]
n=input("Enter the elements of set B = ")
b=n.split(',')
print("Enter the membership value for each element")
mem_b = {}
for i in b:
    mem_b[i] = float(input(f"{i} : "))
print("B = ",mem_b)



print("Union is ",union(mem_a,mem_b))
print()
print("Intersection is ",intersection(mem_a,mem_b))
print()
print("Difference is  ",difference(mem_a,mem_b))
print()
print("Complement of A is  ",complement(mem_a))
print()
print("Complement of B is   ",complement(mem_b))
print()
print("De Morgan's Law Verification")
print()
de_morgan(mem_a,mem_b)

#Ans 1. Hebbian Learning Implementation


def hebbian_learning(samples):
     print(f'{"INPUT":^8} {"TARGET":^16}{"WEIGHT CHANGES":^15}{"WEIGHTS":^25}')
     w1, w2, b = 0, 0, 0
     print(' ' * 45, f'({w1:2}, {w2:2}, {b:2})')
     for x1, x2, y in samples:
         w1 = w1 + x1 * y
         w2 = w2 + x2 * y
         b = b + y
         print(f'({x1:2}, {x2:2})         {y:2}     ({x1*y:2}, {x2*y:2}, {y:2})          ({w1:2}, {w2:2}, {b:2})')

AND_samples = {
    'binary_input_binary_output': [
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],
    'binary_input_bipolar_output': [
        [1, 1, 1],
        [1, 0, -1],
        [0, 1, -1],
        [0, 0, -1]
    ],
    'bipolar_input_bipolar_output': [
        [ 1, 1, 1],
        [ 1, -1, -1],
        [-1, 1, -1],
        [-1, -1, -1]
    ]
}
OR_samples = {
    'binary_input_binary_output': [
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ],
    'binary_input_bipolar_output': [
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, -1]
    ],
    'bipolar_input_bipolar_output': [
        [ 1, 1, 1],
        [ 1, -1, 1],
        [-1, 1, 1],
        [-1, -1, -1]
    ]
}
XOR_samples = {
    'binary_input_binary_output': [
        [1, 1, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ],
    'binary_input_bipolar_output': [
        [1, 1, -1],
        [1, 0, 1],
        [0, 1, 1],
        [0, 0, -1]
    ],
    'bipolar_input_bipolar_output': [
        [ 1, 1, -1],
        [ 1, -1, 1],
        [-1, 1, 1],
        [-1, -1, -1]
    ]
}


print('\n\nHebbian Learning Implementation')
print('AND with Binary Input and Binary Output')
hebbian_learning(AND_samples['binary_input_binary_output'])
print('AND with Binary Input and Bipolar Output')
hebbian_learning(AND_samples['binary_input_bipolar_output'])
print('AND with Bipolar Input and Bipolar Output')
hebbian_learning(AND_samples['bipolar_input_bipolar_output'])


print('OR with binary input and binary output')
hebbian_learning(OR_samples['binary_input_binary_output'])
print('OR with binary input and bipolar output')
hebbian_learning(OR_samples['binary_input_bipolar_output'])
print('OR with bipolar input and bipolar output')
hebbian_learning(OR_samples['bipolar_input_bipolar_output'])


print('XOR with binary input and binary output')
hebbian_learning(XOR_samples['binary_input_binary_output'])
print('XOR with binary input and bipolar output')
hebbian_learning(XOR_samples['binary_input_bipolar_output'])
print('XOR with bipolar input and bipolar output')
hebbian_learning(XOR_samples['bipolar_input_bipolar_output'])

