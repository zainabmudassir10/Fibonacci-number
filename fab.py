def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
n = int(input("Enter the number of Fibonacci numbers you want: "))
fib_numbers = fibonacci(n)
print("Fibonacci sequence:")
print(fib_numbers)
