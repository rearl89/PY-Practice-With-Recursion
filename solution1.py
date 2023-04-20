# Write code for algorithm 1 below
def recur1(n):
    if n == 0:
        return 0
    else:
        print(n)
        recur1(n - 1)
    
recur1(10)