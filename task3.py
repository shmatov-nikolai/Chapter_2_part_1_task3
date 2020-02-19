'''
"Аналог шифра цезаря ". Программа должна запрашивать элементы списка через
пробел. После чего пользователь должен ввести значение для сдвига элементов списка.
Значение может быть как положительным, так и отрицательным. Если значение
положительное, элементы списка должны сдвигаться вправо, если отрицательное -
влево. Результат необходимо вывести на экран:
Введенные данные: [5,7,9,10,2], 2
Результат: [9,10,2,5,7]
'''

def sdvig_list(some_list, step):
    if step > 0:
        for i in range(step):
            some_list.insert(0, some_list.pop())
    elif step < 0:
        for i in range(abs(step)):
            some_list.append(some_list.pop(0))


listok = input("введите последовательность чисел через пробел, для преобразования:").split()
sdvig_num = int(input("введите кол-во сдвигов в преобразовании:"))
print(listok)
if sdvig_num > 0:
    listok_sdvig = sdvig_list(listok, sdvig_num)
    print(f"{listok} сдвиг вправо")
elif sdvig_num < 0:
    listok_sdvig = sdvig_list(listok, sdvig_num)
    print(f"{listok} сдвиг влево")

