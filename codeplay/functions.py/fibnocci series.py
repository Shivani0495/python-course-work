def fibonacci_series(n):
    fib = [0, 1]
    for i in range(2, n):
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)
    return fib[:n]

# Example usage
n = 10
print(f"Fibonacci series up to {n} terms:")
print(fibonacci_series(n))
