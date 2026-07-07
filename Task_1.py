import math
numbers = int(input("Введите кол-во чисел: "))
ceil_or_floor = 0
for i in range(numbers):
    number = float(input("Введите число: "))
    if number >= 0:
        ceil_or_floor = math.ceil(number)
        number = math.log(math.ceil(number))
        print("x =", ceil_or_floor, "log(x) =", number)
    else:
        ceil_or_floor = math.floor(number)
        number = math.exp(math.floor(number))
        print("x =", ceil_or_floor, "exp(x) =", number)