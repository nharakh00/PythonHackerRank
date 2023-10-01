def print_formatted(number):
    
    width = len(str(bin(n)[2:]))
 
    for i in range(1, number + 1):
        
        print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), 
        bin(i)[2:].rjust(width))
        
        
     




if __name__ == '__main__':