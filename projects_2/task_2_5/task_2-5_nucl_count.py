dna = input('Введите воследовательность ДНК:').upper()
count_A = dna.count('A')
count_T = dna.count('T')
count_G = dna.count('G')
count_C = dna.count('C')
lenght = len(dna)

A_per = count_A / int(len(dna)) * 100
T_per = count_T / int(len(dna)) * 100
G_per = count_G / int(len(dna)) * 100
C_per = count_C / int(len(dna)) * 100


print('=== Анализ последовательности ДНК ===\n')
print(f'Последовательность в верхнем регистре: {dna}\n')
print('Подсчёт нуклеоидов:')
print(f'A:\t{count_A}\nT:\t{count_T}\nG:\t{count_G}\nC:\t{count_C}\n')
print('Процентное содержание каждого нуклеоида:')
print(f'A:\t{A_per:.2f}%\nT:\t{T_per:.2f}%\nG:\t{G_per:.2f}%\nC:\t{C_per:.2f}%\n')
print (f'Общая длинна: {lenght} нуклеоидов')