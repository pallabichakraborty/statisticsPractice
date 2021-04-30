/*
Compute Sample Variance
*/

#!/bin/python3

import statistics

def sampleVariance(list, listitemcount):
    mean=statistics.mean(list)
    
    sampleVariance=0
    
    for item in list:
        sampleVariance+=(item - mean) **2
        
    sampleVariance=sampleVariance/(listitemcount-1)
    
    print("Sample Variance : {}".format(sampleVariance))
    
    return sampleVariance

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))
    
    sampleVariance(vals, n)
