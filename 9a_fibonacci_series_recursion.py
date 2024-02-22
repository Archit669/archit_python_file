# Create a program that prints numbers in Fibonacci series using recursion.

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci_recursive(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

def main():
    n = int(input("Enter the number of terms in the Fibonacci series: "))
    fib_series = fibonacci_recursive(n)
    print("Fibonacci series up to", n, "terms:", fib_series)

if __name__ == "__main__":
    main()
