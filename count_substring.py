def count_substring(string, sub_string):
    
    str_len = len(string)
    sub_len = len(sub_string)
    counter = 0
    
    for i in range(0, str_len):
        if(string[i:sub_len + i] == sub_string ):
            counter = counter + 1
    

    return counter
