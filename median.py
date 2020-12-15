""" Author: Jan Jelinek

    Problem: Let A and B be distinct arrays, each containing n elements.
    Find the median of A and B in Theta(log n).

    Precondition: Two arrays each containing n distinct elements.
    Postcondition: The median of all 2n elements.
"""
import math

def divideAndConquer(A,B):

    if len(A) == len(B) == 1:
        return (A[0]+B[0])/2

    splitA = math.floor(len(A)/2)
    A1 = A[0:splitA]
    A2 = A[splitA:]
    
    splitB = math.ceil(len(B)/2)
    B1 = B[0:splitB]
    B2 = B[splitB:]
    
    if (A1[-1] > B2[0]) and (len(A1) > 1) and (len(B2) > 1):
        return divideAndConquer(A1,B2)
    if (B1[-1] > A2[0]) and (len(A2) > 1) and (len(B1) > 1):
        return divideAndConquer(A2,B1)
    
    return ( max(A1[-1],B1[-1]) + min(A2[0],B2[0]) )/2

def mergeAndSort(A,B): # For comparison
    merged = A+B
    merged.sort()
    if len(merged)%2 == 0:
        return (merged[int(len(merged)/2)]+merged[int(len(merged)/2-1)])/2
    else:
        return merged[math.floor(len(merged)/2)]

inputA = [int(x) for x in input("A: ").split()]
inputB = [int(x) for x in input("B: ").split()]

print( "D&C: ",divideAndConquer(inputA,inputB) )
print( "M&S: ",mergeAndSort(inputA,inputB) )
