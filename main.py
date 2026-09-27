from algorithms import count_vowels, gcd_euclidean, sum_odd_numbers


def main() -> None:
    print("=== Лабораторная работа № 2. Вариант 2 ===")

    n = 10
    odd_sum = sum_odd_numbers(n)
    print(f"\n1. Сумма нечётных чисел до {n}: {odd_sum}")

    num1, num2 = 48, 18
    nod = gcd_euclidean(num1, num2)
    print(f"2. НОД({num1}, {num2}) по алгоритму Евклида: {nod}")

    test_string = "Программирование на Python"
    vowel_count = count_vowels(test_string)
    print(f"3. Количество гласных в строке '{test_string}': {vowel_count}")


if __name__ == "__main__":
    main()