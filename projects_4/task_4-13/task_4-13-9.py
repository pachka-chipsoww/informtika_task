n = int(input("Введите количество элементов массива: "))
A = []
print("Введите элементы массива: ")
for i in range(n):
    A.append(int(input()))
i = 0
sum = 0
while i < n:
    if i % 2 != 0:
        sum = sum + A[i]
    i = i + 1
print("Сумма  всех элементов в произвольно заданном массиве с нечетными индексами,: ", sum)