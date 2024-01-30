"""Write a program that computes the list of the first 100 Fibonacci numbers.
The first two Fibonacci numbers are 1 and 1.
The n+1 Fibonacci number is computed by adding the n-th and the n-1-th Fibonacci number.
The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8. Print out the results"""

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    fib_sequence = [1, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence


first_100_number = fibonacci_sequence(100)
print(first_100_number)