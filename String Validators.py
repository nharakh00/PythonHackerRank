if __name__ == '__main__':
    s = input()
    
    aln_flag = False 
    alpha_flag = False 
    digit_flag = False 
    lower_flag = False 
    upper_flag = False
    
    for i in range(0, len(s)):
        if s[i].isalnum():
            aln_flag = True
        if s[i].isalpha():
            alpha_flag = True 
        if s[i].isdigit():
            digit_flag = True 
        if s[i].islower():
            lower_flag = True 
        if s[i].isupper():
            upper_flag = True
            
    print(aln_flag)
    print(alpha_flag)
    print(digit_flag)
    print(lower_flag)
    print(upper_flag)        
