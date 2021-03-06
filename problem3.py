def factors(n):
    factor = 2
    while factor ** 2 <= n:
        while n % factor == 0:
            n = n // factor
            yield factor
        factor += (2 if factor != 2 else 1)
    if n != 1:
        yield n


def f(n):
    return max(factors(n))


if __name__ == "__main__":
    print f(3)
