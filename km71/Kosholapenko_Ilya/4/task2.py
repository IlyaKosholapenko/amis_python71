print("Данная программа предназначена для вычисления значение функции  sign(x)\nв зависимости от значения x")#Выводим приветствие и предназначение программы
x = float(input("Введите значение х:"))#Команда для ввода переменной
if x > 0:#условие 1
    signx = 1#присваиваем соответственное значение переменной
elif x < 0:#условие 2
    signx = -1#присваиваем соответственное значение переменной
else:#условие 3
    signx = 0#присваиваем соответственное значение переменной
print("sign(x) = " + str(signx))#вывод результатa
print(input("Нажмите клавишу \"Enter\" для окончания работы программы"))#Команда для окончания программы
