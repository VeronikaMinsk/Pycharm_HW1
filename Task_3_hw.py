a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Треугольник существует и является равносторонним.")
    elif a == b or a == c or b == c:
        print("Треугольник существует и является равнобедренным.")
    else:
        print("Треугольник существует и является разносторонним.")
else:
    print("Треугольник с такими сторонами не существует.")


