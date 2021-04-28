/*
Tutorial: https://www.youtube.com/watch?v=5C9LBF3b65s&ab_channel=TheAnimatedClassroom
          https://www.khanacademy.org/math/statistics-probability

Mean or Average = Sum of all numbers/ Count of all Numbers
Median = Sort the numbers in ascending order
         If odd count of numbers, find the middle number
         If even count of numbers, find the middle 2 numbers, sum them up and divide by 2
Mode = Sort the numbers in ascending order
       Find the number with maximum number of occurences

*/


# Enter your code here. Read input from STDIN. Print output to STDOUT
size = int(input())
inputdata=input()

total=0

inputlist=inputdata.split()
inputlistint=[]

for item in inputlist:
    total+=int(item)
    inputlistint.append(int(item))
    
mean=total/len(inputlist)

print(str(mean))

# Sorting list of Integers in ascending
inputlistint.sort()

if(len(inputlist)%2==0):
    median=(inputlistint[len(inputlistint)//2]+inputlistint[len(inputlistint)//2 -1])/2
else:
    median=inputlistint[len(inputlistint)//2]

print(str(median))

modelist=[]

for item in inputlistint:
    modelist.append(inputlistint.count(item))
    
maxindex=modelist.index(max(modelist))

print(str(inputlistint[maxindex]))




