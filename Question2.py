def number(n):
    if n == 1:
        return 8
    else:
        return number(n - 1) + 7

print("number(1) =", number(1))   
print("number(5) =", number(5))  
print("number10) =", number(10)) 

# The function is recursive because it calls itself within the function by decreasing the value of n until n becomes 1.