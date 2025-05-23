def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
result = generate_fibonacci(num_terms)
print("Fibonacci Sequence:", result)
