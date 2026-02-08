''' Let's understand the concept of dynamic programming through fibonacci series.
Dynamic programming is typically a way to make the algorithm more efficient by storing the
intermediate results, specially in the case of repetitive computations. 
If we want to solve a problem using dynamic programming we can do it in three different ways
1. Recursion
2. Memoization
3. Bottom up '''
#recursion
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        result = fib(n-1) + fib(n-2)
    return result
#Memoization
def fibbo(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n ==2:
        return 1
    else:
        result_1 = fibbo(n-1, memo) + fibbo(n-2, memo)
    memo[n] = result_1
    return result_1
def fib_memo(n):
    memo = [None] * (n+1)
    return fibbo(n, memo)
#Bottom up
def fibbonacci(n):
    if n==1 or n==2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]