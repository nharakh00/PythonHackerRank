if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    i_list = list(integer_list)
    t = tuple(i_list)
    
    
    print(hash(t))
