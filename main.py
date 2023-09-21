from publ import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

functionAims = int(input("Мы хотим найти минимум (1) или максимум (-1): "))

model = LpProblem(name="small-problem", sense=functionAims)

roots = int(input("Введите количество неизвестных: "))
constraint = int(input("Введите количество oграничений: "))

coefficients = [[0] * roots for i in range(constraint)]
sign = [0 for i in range(constraint)]
right = [0 for i in range(constraint)]
functionCoefficients = [0 for i in range(constraint)]

for i in range(constraint):
    for j in range(roots):
        coefficients[i][j] = int(input("Введите значение " + str(j + 1) + " коэффицента "
                                       + str(i + 1) + "ограничения: "))

for i in range(constraint):
    sign[i] = input("ведите знак равенства / неравенства ограничений: ")
for i in range(constraintn):
    right[i] = int(input("Введите правую часть ограничений: "))
for i in range(roots):
    functionCoefficients[i] = int(input("Введите " + str(i + 1) +" коэффицент функциии: "))

x1 = LpVariable(name="x1",lowBound=0)
x2 = LpVariable(name="x2",lowBound=0)
x3 = LpVariable(name="x3",lowBound=0)
x4 = LpVariable(name="x4",lowBound=0)
x5 = LpVariable(name="x5",lowBound=0)
for i in range(constraint):
    for j in range(roots):
        help += coefficients[i][j] * str(i + 1)
                # sign[i] + right[i], i + "con: ")
        #model += (coefficients[i][j] * str(i + 1) + coefficients[i][j] * str(i + 2) +
         #         coefficients[i][j] * str(i + 1) + coefficients[i][j] * str(i + 1) +
          #        coefficients[i][j] * str(i + 1) + sign[i] + right[i], i + "con: ")
#model += (7 * x1 + 0 * x2 + 16* x3 + 5 * x4  + 25 * x5 <= 600,"first_constraint")
#model += (8 * x1 + 1.7 * x2 - 0.5 * x3 + 4.7 * x4 == 890,"second_constraint")
#model += (4 * x1 - 1.5 * x2 + 10.4  * x3 + 13 * x4 == 756,"third_constraint")
#model += (4 * x1 - 1.5 * x2 + 10.4  * x3 + 13 * x4 == 756,"fourth_constraint")

for i in range(roots):
    models += functionCoefficients[i] * str(i + 1)

#obj_func =  10 * x1 - 0 * x2 + 40  * x3 + 13 * x4 + 56 * x5
#model += obj_func

status = model.solve()

print(f"status: {model.status},{LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}:{var.value()}")

