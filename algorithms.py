def sum_odd_numbers(n: int) -> int:
    if n < 1:
        return 0
    return sum(x for x in range(1, n + 1) if x % 2 != 0)


def gcd_euclidean(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def count_vowels(text: str) -> int:
    vowels = set("aeiouyаеёиоуыэюя")
    return sum(1 for char in text.lower() if char in vowels)