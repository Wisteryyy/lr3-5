import math
x=float(input("Введите значение x"))
y=float(input("Введите значение y"))
R=float(input("Введите радиус круга"))
formylarastoyania=math.sqrt(x**2+y**2)
if formylarastoyania <= R:
 print("Точка попадает в круг")
else:
 print("Точка не попадает в круг")