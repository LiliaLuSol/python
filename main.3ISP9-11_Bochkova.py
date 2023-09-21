#Лаб 1. Бочкова Мария 3ИСП9-11
#10.

#class
# from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
#
# model = LpProblem(name="small-problem", sense=LpMaximize)
#
# x1 = LpVariable(name="x1",lowBound=0)
# x2 = LpVariable(name="x2",lowBound=0)
# x3 = LpVariable(name="x3",lowBound=0)
# x4 = LpVariable(name="x4",lowBound=0)
#
# model += (-1.8 * x1 + 2 * x2 + x3 - 4 * x4 == 756, "first_constraint")
# model += (-6 * x1 + 2 * x2 + 4 * x3 - x4 >= 450, "second constraint")
# model += (4 * x1 - 1.5 * x2 + 10.4 * x3 + 13 * x4 <= 89, "third_constraint")
#
# obj_func = 130.5 * x1 + 20 * x2 + 56 * x3 + 87.8 * x4
# model += obj_func
#
# print(model)
#
# status = model.solve()
# print(f"status: {model.status},{LpStatus[model.status]}")
# print(f"objective: {model.objective.value()}")
#
# for var in model.variables():
#     print(f"{var.name}:{var.value()}")


#Самостоятельная. 10
from pulp import *
import operator

functionAims = int(input("Мы хотим найти минимум (1) или максимум (-1): "))
if functionAims == 1:
    sense = LpMinimize
elif functionAims == -1:
    sense = LpMaximize
else:
    print("Ошибка: введите 1 или -1")

model = LpProblem(name="small-problem", sense=sense)

roots = int(input("Введите количество неизвестных: "))
constraint = int(input("Введите количество oграничений: "))

coefficients = [[0] * roots for i in range(constraint)]
sign = [0 for i in range(constraint)]
right = [0 for i in range(constraint)]
functionCoefficients = [0 for i in range(roots)]

for i in range(constraint):
    for j in range(roots):
        coefficients[i][j] = float(input(f"Введите значение {j+1}-го коэффициента {i+1}-го ограничения: "))

for i in range(constraint):
    sign[i] = input(f"Введите знак равенства / неравенства {i+1}-го ограничения: ")
for i in range(constraint):
    right[i] = float(input(f"Введите правую часть {i+1}-го ограничения: "))
for i in range(roots):
    functionCoefficients[i] = float(input(f"Введите {i+1}-й коэффициент целевой функции: "))

# x1 = LpVariable(name="x1",lowBound=0)
# x2 = LpVariable(name="x2",lowBound=0)
# x3 = LpVariable(name="x3",lowBound=0)
# x4 = LpVariable(name="x4",lowBound=0)
# x5 = LpVariable(name="x5",lowBound=0)
variables = [LpVariable(name=f"x{i}", lowBound=0) for i in range(1, roots+1)]

for i in range(constraint):
    helpy = lpSum(coeff * var for coeff, var in zip(coefficients[i], variables))
    if sign[i] == "<=":
        model += helpy <= right[i]
    elif sign[i] == "==":
        model += helpy == right[i]
    elif sign[i] == ">=":
        model += helpy >= right[i]
    elif sign[i] == "!=":
        model += helpy != right[i]

# for i in range(constraint):
#     #for j in range(roots):
#     helpy += LpAffineExpression([(str(j + 1),int(coefficients[i][j])) for j in range(roots)])
#     if ((sign[i]) == "<="):
#         model += (operator.le(helpy,right[i]),str(i) + " con")
#     elif ((sign[i]) == "=="):
#         model += (operator.eq(helpy,right[i]),str(i) + " con")
#     elif ((sign[i]) == ">="):
#         model += (operator.ge(helpy,right[i]),str(i) + " con")
#     elif ((sign[i]) == "!="):
#         model += (operator.ne(helpy,right[i]),str(i) + " con")

    #model += LpProblem(sign[i]) + LpProblem(int(right[i]))
#        helpy += LpConstraint(int(coefficients[i][j]) * str(i + 1))
#    model += (LpProblem(helpy) + LpProblem(sign[i]) + LpProblem(right[i]), str(i) + " constraint")

# for i in range(len(functionCoefficients)):
#     model += lpSum([functionCoefficients[i] * variables[i + 1] for i in range(roots)])

model += lpSum([functionCoefficients[i] * variables[i] for i in range(roots)])

print(model)
status = model.solve()

print(f"status: {model.status},{LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}:{var.value()}")


#проверка

# from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
#
# functionAims = int(input("Мы хотим найти минимум (1) или максимум (-1): "))
#
# model = LpProblem(name="small-problem", sense=functionAims)
#
# x1 = LpVariable(name="x1",lowBound=0)
# x2 = LpVariable(name="x2",lowBound=0)
# x3 = LpVariable(name="x3",lowBound=0)
# x4 = LpVariable(name="x4",lowBound=0)
# x5 = LpVariable(name="x5",lowBound=0)
#
# model += (7 * x1 + 0 * x2 + 16 * x3 + 5 * x4 + 25 * x5 <= 600,"first_constraint")
# model += (8 * x1 + 1.7 * x2 + 0 * x3 - 0.5 * x4 + 4.7 * x5 == 890,"second_constraint")
# model += (6 * x1 + 0 * x2 + 4 * x3 - 7 * x4 + 6.3 * x5 <= 270,"third_constraint")
# model += (84 * x1 + 62 * x2 + 80 * x3 + 0 * x4 + 14 * x5 >= 2300,"fourth_constraint")
#
# model += 10 * x1 + 0 * x2 + 40 * x3 + 13 * x4 + 56 * x5
#
# print(model)
#
# status = model.solve()
#
# print(f"status: {model.status},{LpStatus[model.status]}")
# print(f"objective: {model.objective.value()}")
#
# for var in model.variables():
#     print(f"{var.name}:{var.value()}")
