import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
        rightDig= [arr[i][i] for i in range(len(arr))]
        rightDigSum = sum(rightDig)
        leftDig=([arr[i][len(arr)-i-1] for i in range(len(arr))])
        leftDigSum= sum(leftDig)
        Digdiff = rightDigSum - leftDigSum
        return abs(Digdiff)

                

    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
  