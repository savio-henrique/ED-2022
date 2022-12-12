def fib(n,memo = {}):
    if n in memo:
        return memo[n]
    if n < 1:
        return 0
    elif n == 1:
        return 1
    memo[n] = fib(n - 1,memo) + fib(n - 2,memo)
    return memo[n]

n = int(input())
print(f"fibonacci({n}) = {fib(n)}.")