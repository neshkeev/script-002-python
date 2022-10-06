def fibo(n):
    if n <= 2:
        return 1
    return fibo(n - 2) + fibo(n - 1)
