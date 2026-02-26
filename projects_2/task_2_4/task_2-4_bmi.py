weight = float(input("Введите массу (кг): "))
height = float(input("Введите ваш рост (см): "))
height = height / 100
bmi = weight / (height ** 2)

print("\n--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height} м")
print(f"Вес:\t{weight} кг")
print(f"Индекс массы тела:\t{bmi:.2f}")