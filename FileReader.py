import math
import re

lista = [1, 2, 3, 2, 1, 9, 109]
listb = []

while lista > [0]:
    return_value = lista.pop()
    listb.append(return_value)

print(listb)

stringa = "abcba" [::-1]
print(stringa)


f=open("MathQuestions.txt","r")
line1 = f.readlines()[0]
f.close()

lista = []
for i in line1:
    lista.append(i)

int1 = int(lista[0])
operator = lista[2]
int2 = int(lista[4])

if operator == "+":
    result = int1 + int2
    print(int1, operator,  int2, "=", result)

x = 0

for i in line1:
    print(i)
    if i != ' ' and i != '\n' and i != '+':

        x += int(i)


print(x)


