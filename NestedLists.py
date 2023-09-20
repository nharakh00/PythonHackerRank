
# This line of code generates the list 
n_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    n_list.append([name, score])

# This is just a test to see the list we have generated         
#print(n_list)
list_len = len(n_list)

# setting up indices
min_grade = 10000
sec_min = 10000
name_arr = []
sec_min_arr = []

# iterating through our array to find minimum_grade
for i in range(0, list_len):
    if(n_list[i][1] < min_grade):
        min_grade = n_list[i][1]


for j in range(0, list_len):
    if(n_list[j][1] > min_grade and n_list[j][1] < sec_min):
        sec_min = n_list[j][1]

for k in range(0, list_len):
    if(n_list[k][1] == sec_min):
        sec_min_arr.append(n_list[k][0])

sec_min_arr.sort()
for l in range(0, len(sec_min_arr)):
    print(sec_min_arr[l])
    
        
