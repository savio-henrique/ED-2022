def fib(n,dic):
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
    if n < 1:
        return 0
    elif n == 1:
        if n-1 not in dic:
            dic[n-1] = 0
        return 1
    else:
        return fib(n - 1,dic) + fib(n - 2,dic)

chamados={}
num = int(input())
print(f"fibonacci({num}) = {fib(num,chamados)}.")
for i in sorted(chamados):
    print(f"{chamados[i]} chamada(s) a fibonacci({i}).")