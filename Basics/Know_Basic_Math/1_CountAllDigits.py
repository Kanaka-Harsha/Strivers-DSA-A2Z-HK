import math
n=int(input())
# Brute Force
'''
count=0
while n!=0:
    count+=1
    n//=10
'''
# Optimal, using math
count=int(math.log10(n)+1)
print(count)