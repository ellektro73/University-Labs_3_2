n = "258762"

sum_digits = 0

if len(n) == 6 and n.isdigit():
    for char in n:
        sum_digits += int(char)

    print(f"Число: {n}")
    print(f"Сума цифр: {sum_digits}")
else:
    print("Помилка: введіть коректне шестизначне число.")