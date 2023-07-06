number = int(input("Введите число: "))

if number <= 0 or number > 100000:
    print("Число должно быть положительным и не превышать 100000.")
else:
    is_prime = True

    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        print("Число", number, "является простым.")
    else:
        print("Число", number, "является составным.")
