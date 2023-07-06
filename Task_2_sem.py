number = int(input("Введите число от 1 до 999: "))

if 1 <= number <= 9:
    # Цифра
    square = number ** 2
    print("Введена цифра. Квадрат числа:", square)
elif 10 <= number <= 99:
    # Двузначное число
    digit_product = (number // 10) * (number % 10)
    print("Введено двузначное число. Произведение цифр:", digit_product)
elif 100 <= number <= 999:
    # Трехзначное число
    reverse_number = int(str(number)[::-1])
    print("Введено трехзначное число. Зеркальное отображение:", reverse_number)
else:
    print("Введено некорректное число. Пожалуйста, введите число от 1 до 999.")