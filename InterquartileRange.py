/*
Tutorial: https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/interquartile-range-iqr/a/interquartile-range-review?modal=1

Here's how to find the IQR:
Step 1: Put the data in order from least to greatest.
Step 2: Find the median. If the number of data points is odd, the median is the middle data point. If the number of data points is even, the median is the average of the middle two data points.
Step 3: Find the first quartile (Q1). The first quartile is the median of the data points to the left of the median in the ordered list.
Step 4: Find the third quartile (Q3(. The third quartile is the median of the data points to the right of the median in the ordered list.
Step 5: Calculate IQR by subtracting Q3-Q1

*/
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def median(sorted_arr,n):
    print(sorted_arr)
    if(n%2!=0):
        return sorted_arr[(n//2)]
    else:
        res=(sorted_arr[(n//2)-1]+sorted_arr[(n//2)])/2
        if (round(res)==res):
            return round(res)
        else:
            return res


def quartiles(arr):
    # Write your code here
    arr.sort()
    arrlen=len(arr)
    
    Q2=median(arr,arrlen)
    
    medianpos=arrlen//2
    
    if(arrlen%2!=0):
        Q1arr=arr[:medianpos]
        Q3arr=arr[medianpos+1:]
        
    else:
        Q1arr=arr[:medianpos]
        Q3arr=arr[medianpos:]
        
    Q1=median(Q1arr,len(Q1arr))
    Q3=median(Q3arr,len(Q3arr))
    
    return [Q1,Q2,Q3]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
