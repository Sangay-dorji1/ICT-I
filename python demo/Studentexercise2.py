def pattern(n):
    # Base case
    if n == 1:
        print("*")
        return
    
    # Recursive call
    pattern(n - 1)
    
    # Print after returning (increasing order)
    print("* " * n)
    
n = int(input(" enter a number: "))
print(pattern(n))