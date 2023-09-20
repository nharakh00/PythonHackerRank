if __name__ == '__main__':
    n = int(input())
    
    num_str = ""
    for value in range(0, n):
        num_str = num_str + str(value + 1)
        
    print(num_str)
