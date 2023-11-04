from itertools import product

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cart_prod = list(product(A,B))
for i in range(0,len(cart_prod)):
    print(cart_prod[i], end = " ")
    



