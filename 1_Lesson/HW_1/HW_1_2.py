    #  Task2. Напишите программу для проверки ложности утверждения
    #  (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.
    # (W and Z) or not Y or ((not X) == (not W))
    #     1      2  3     4   5     6  7 

print('w z y x')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not (w and z or not y or x == w):
                    print(w, z, y, x)