# Question 1.A
from collections import deque


def process_queue(input_file):
    queue = deque()
    with open(input_file, 'r') as file:
        for line in file:
            action, name = line.strip().split()
            if action == 'JUMP':
                queue.appendleft(name)
            else:
                if action == 'JOIN':
                 queue.append(name)
    return list(queue)


print(process_queue('input_file.txt'))

# Question 1.B

# Time Complexity:
# In terms of time complexity, the majority of the program takes a constant time (O(1)) because appending to a deque or list takes constant time.  

# The opening of the file line ‘with open(input_file, 'r') as file’ takes O(n) time where n is the number of lines in the input_file.txt file. The same goes for the return list(queue)line because it is returning n (the number of strings in the file). 

# So the time complexity here will be O(n) + O(n)  = O(n) or O(25) + O (25) = O(50).

# Space complexity:
# The number of bytes a string takes up is equal to the number of characters in the string plus 1 (the terminator), times the number of bytes per character. The number of bytes per character can vary. It is 1 byte for a regular char type. (taken from stack overflow, for own reference).

# Integer takes 4 bytes of storage in memory (int - 4B)
# There is usually a trade off between optimal memory used and runtime performance.
# The more time efficiency you have, the less space efficiency you have and vice versa. For example, merge sort is very fast but requires a lot of space. (for own reference).

# The space usage in this program is directly aligned to the number of names stored in the queue. 

# This program has no integers. The number of strings is in the ‘input_file.txt’ file. 
# The number of strings in this file is 52, including all the ‘jump’ and ‘join’ strings and name strings. 

# So, 52 x 1 = 52 bytes for the strings. 

# However, in this program we only store the names. There are 25 name strings in total so:

# 25 x 1 = 25 bytes for the strings, stored by the list(deque) function. 

# The space complexity of the program is O(n) where n is the number of names stored in the input_file.txt file. 
