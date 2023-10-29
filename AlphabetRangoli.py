



def print_rangoli(size):
    
    alphabets = list(map(chr,range(97,123)))
    mid_line_arr = alphabets[n-1::-1] + alphabets[1:n]
    mid_line = "-".join(mid_line_arr)
    length = len(mid_line)
    
    for i in range(1,size):
        print("-".join(alphabets[size-1:size-i:-1] + alphabets[size-i:size] ).center(length,"-"))
    for j in range(size,0,-1):
        print("-".join(alphabets[size-1:size-j:-1] + alphabets[size-j:size] ).center(length,"-"))

if __name__ == '__main__':
