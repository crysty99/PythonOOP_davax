def pow_op(base: int, exp: int) -> int:
    return base ** exp


def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError('Negative values not allowed')
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
