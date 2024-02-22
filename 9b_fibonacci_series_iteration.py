# Create a program that prints numbers in Fibonacci series using iteration

def fibonacci_iterative(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def main():
    n = int(input("Enter the number of terms in the Fibonacci series: "))
    fib_series = fibonacci_iterative(n)
    print("Fibonacci series up to", n, "terms:", fib_series)

if __name__ == "__main__":
    main()
