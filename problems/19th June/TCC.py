import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
def getans(n,c,m):
    if (n == 0): 
        return 1
    if (n < 0): 
        return 0; 
    if (m <=0 and n >= 1): 
        return 0
    return getans(n,c,m-1)+getans(n-c[m-1],c,m); 

def getWays(n, c):
    m=len(c)
    return getans(n,c,m)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
