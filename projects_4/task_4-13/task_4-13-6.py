n = int(input("Введите количество чисел: "))
i = 0
sum = 0
while i < n:
    A = float(input("Введиче число: "))
    sum = sum + A
    i = i + 1
mean = sum / n
print(f"Среднее арифметическое {n} чисел: {mean}")