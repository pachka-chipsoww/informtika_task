N = int(input("Введите количество чисел: "))
i = 1
sum = 0
while i <= N:
    sum = sum + i**2
    i = i + 1
print(f"Сумма квадратов первых {N} чисел: {sum}")