import numpy as np

roots = int(input("Введите количество неизветных: "))
constraint = int(input("Введите количество ограничений: "))

coefficients = [[0] * roots for i in range(constraint)]
sign = [0 for i in range(constraint)]
right = [0 for i in range(constraint)]
functionCoefficients = [0 for i in range(roots)]

for i in range(constraint):
    for j in range(roots):
        coefficients[i][j] = float(input("Введите значение" + str(j + 1)
                                         + " коэффициента " + str(i + 1) + " ограничения: "))

for i in range(constraint):
    sign[i] = input("Введите знак равенства / неравенства ограничений: ")

for i in range(constraint):
    right[i] = float(input("Ввведите правую часть ограничений: "))

for i in range(roots):
    functionCoefficients[i] = float(input("Введите " + str(i + 1) + " коэффициент функций: "))

constraintInequality = [0 for i in range(0)]
constraintEquality = [0 for i in range(0)]
for i in range(constraint):
    if sign[i] != "==":
        constraintInequality.append(i)
    else:
        constraintEquality.append(i)

n = 0
for i in range(len(constraintInequality)):
    for j in range(len(constraintInequality)):
        n = 1
        if n == j:
            if sign[constraintInequality[i]] == "<=":
                coefficients[constraintInequality[i]].insert(roots + j, float(1))
                n -= 1
            else:
                coefficients[constraintInequality[i]].insert(roots + j, float(-1))
                n -= 1
        else:
            coefficients[constraintInequality[i]].insert(roots + j, float(0))

for i in range(len(constraintEquality)):
    for j in range(len(constraintInequality)):
        coefficients[constraintEquality[i]].insert(roots + j, float(0))

for i in range(roots):
    functionCoefficients[i] *= -1

for i in range(len(constraintInequality) + 1):
    functionCoefficients.append(float(0))

print(np.row_stack([np.column_stack([coefficients, right]), functionCoefficients]))