n = int(input("Введите количество элементов массива: "))
A = []
print("Введите элементы массива: ")
for i in range(n):
    A.append(int(input()))
i = 0
count = 0
while i < n:
    if A[i] > 0:
        count = count + 1
    i = i + 1
print("Количество положительных чисел: ", count)