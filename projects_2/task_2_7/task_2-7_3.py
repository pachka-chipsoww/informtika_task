seq = [ "ATATACGCGTA", "CTTCGGNGGA" ]
for i in seq:
    print(f"Последовательность целиком: {i}")
    print("Построчно:")
    for nucleotide in i:
        print(nucleotide)
print('Цикл выполнен')