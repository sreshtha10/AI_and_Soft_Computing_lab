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


