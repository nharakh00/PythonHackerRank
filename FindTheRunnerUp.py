n = int(input())
arr = map(int, input().split())
larr = list(arr)

max_1 = -1000000
runner_up = -1000000



for i in range(0, len(larr)):
    if(larr[i] > max_1):
        max_1 = larr[i]

for j in range(0, len(larr)):
    if(larr[j] > runner_up and larr[j] < max_1):
        runner_up = larr[j]

print(runner_up)

