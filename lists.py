if __name__ == '__main__':
    
    N = int(input())
    new_list = []
    
    for i in range(0, N):
        cmd = input()
        
        if cmd.split()[0] == 'insert':
            cmd_arr = cmd.split()
            new_list.insert(int(cmd.split()[1]), int(cmd.split()[2]))
            
        elif cmd.split()[0] == 'print':
            print(new_list)
        
        elif cmd.split()[0] == 'remove':
            new_list.remove(int(cmd.split()[1]))
        
        elif cmd.split()[0] == 'append':
            new_list.append(int(cmd.split()[1]))
        
        elif cmd.split()[0] == 'sort':
            new_list.sort()
        
        elif cmd.split()[0] == 'pop':
            new_list.pop()
        
        elif cmd.split()[0] == 'reverse':
            new_list.reverse()
        else:
            print("This is all the list operations ")
