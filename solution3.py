# Write code for algorithm 3 below
def fibby_seq(n):
    if n <= 1:
        return n
    elif n == 2:
        return 1
    else:
        return fibby_seq(n-1) + fibby_seq(n-2)
print(fibby_seq(2))
print(fibby_seq(3))
print(fibby_seq(5))
print(fibby_seq(8))

