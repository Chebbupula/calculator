print("Введите первое число")
a = input()
print("Введите второе число")
b = input()
print("Какое действие?")
a = int(a)
b = int(b)
print("1. +")
print("2. -")
print("3. *")
print("4. /")
choice = input("Введите номер действия (1/2/3/4): ")
if choice == '1':
    plus = a + b
    print("Число " + str(plus))
elif choice == '2':
    minus = a - b
    print("Число" + str(minus))
elif choice == '3':
    multiply = a * b
    print("Число" + str(multiply))
elif choice == '4':
    divide = a / b
    print("Число" + str(divide))
else:
    print("ОШИБКА")