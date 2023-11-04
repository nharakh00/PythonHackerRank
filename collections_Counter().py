# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())
N = list(map(int,input().split()))
n_c = int(input())
# This turns our Counter Object into a regular dictionary
stock = dict(Counter(N))
tot = 0 
temp = 0 

for i in range(n_c):
    c = list(map(int,input().split()))
    
    for j in range(len(stock.keys())):
        if c[0] == list(stock.keys())[j]:
            temp = list(stock.keys())[j]
            if stock[temp] > 0:
                tot = tot + c[1]
                stock[temp] = stock[temp] - 1         
print(tot)



