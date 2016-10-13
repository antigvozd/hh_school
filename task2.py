def search_index(num):
    minim = 0
    index = 0
    for i in range(1, len(num)+1):                  # прорабатываем все возможные распределения по разрядам
        if i == len(num):                           # если длина разряда равна длине подпоследовательности
            num1 = [int(x) for x in num]
            arr = [x for x in range(len(num1))]
            if len(num) > 1 and num == '9'*len(num):    # если подпослед. вида 999
                minim = int('8' + '9'*(len(num) - 1))
                index = 1
                break
            elif num == '9':                            # если подпослед. = 9
                minim = 9
                index = 0
                break
            for s in range(len(num)):                   # в цикле избавляемся от неподходящих значений
                m = 9
                if s == 0:
                    for l in range(len(arr)):
                        m = num1[l] if num1[l] > 0 and num1[l] < m else m
                else:
                    for l in range(len(arr)):
                        if arr[l] + s >= len(num1):
                            index = len(num1) - arr[l] - s
                        else:
                            index = arr[l] + s
                        m = num1[index] if num1[index] < m else m
                l = 0
                while l < len(arr):

                    if arr[l] + s >= len(num1):
                        index = arr[l] + s - len(num1)
                    else:
                        index = arr[l] + s
                    if num1[index] != m:
                        arr.remove(arr[l])
                    else:
                        l += 1
                if s == len(num) - 1 and len(arr) > 1:
                    if num[:arr[0]] == '9'*len(num[:arr[0]]) and int(num[arr[0]:]) < int('9'*len(num[arr[0]:])):
                        minim = int(str(int(num[arr[0]:]) - 1) + num[:arr[0]])
                        index = len(num) - arr[0]
                    else:
                        minim = int(str(int(num[arr[0]:])) + num[:arr[0]])
                        index = 0
                    break
                if len(arr) == 1:
                    if num[:arr[0]] == '9'*len(num[:arr[0]]) and int(num[arr[0]:]) < int('9'*len(num[arr[0]:])):
                        minim = int(str(int(num[arr[0]:]) - 1) + num[:arr[0]])
                    else:
                        minim = int(num[arr[0]:] + num[:arr[0]])
                    index = len(num) - arr[0]
                    break
        else:                           # если длина разряда не равна длине подпоследовательности
            for j in range(i):                         # и по смещениям
                length = i
                razr = '_' * j                          # заполняем смещение разряда символом _
                list = []
                s = 0
                while s < len(num):
                    if razr == "" and num[s] == "0":                    # если первая цифра разряда 0, завершаем цикл
                        break
                        #pass
                    razr += num[s]
                    if s == len(num) - 1:                               # заполняем пустые разряды символом _
                        razr += '_' * (length - len(razr))
                    if len(razr) == length:
                        list.append(razr)
                        if s < len(num) - 1:
                            if razr == '9' * i and num[s + 1] == '1':   # проверяем случай 9|1
                                length += 1
                        razr = ""
                        if len(list) == 1 and s == len(num) - 1:
                            if minim == 0:
                                minim = int(list[0])

                            else:
                                minim = int(list[0]) if int(list[0]) < minim and int(list[0]) > 0 else minim

                        if len(list) == 2:
                            index = 0
                            k = 0
                            l = 0
                            while list[l][k] == "_":
                                index += 1
                                k += 1
                            if list[l][index:] == '9' * len(list[l][index:]) and index > 0:  # проверка 9|1
                                if list[l + 1][:index] == '1':
                                    list[l] = list[l][index:]
                                else:
                                    list[l] = str(int(list[l + 1][:index]) - 1) + list[l][index:]
                            elif index > 0:
                                list[l] = list[l + 1][:index] + list[l][index:]
                            else:
                                list[l] = list[l][index:]
                        if len(list) > 1:
                            l = len(list) - 1
                            while l < len(list):  #  пройдемся по каждому элементу списка разрядов
                                index = 0
                                k = 0
                                if l == len(list) - 1:
                                    while list[l][len(list[l]) - 1 - k] == "_":
                                        index += 1
                                        k += 1
                                    st = list[l][0:len(list[l]) - index] + (list[l - 1][len(list[l]) - index:])

                                    if list[l - 1][-index:] == '9' * len(list[l - 1][-index:]) and index > 0:
                                        list[l] = list[l][0:-index] + '0' * index

                                    elif index > 0:
                                        list[l] = str(int(st) + 1)

                                    else:
                                        list[l] = st

                                if l > 0:
                                    if int(list[l]) - int(list[l - 1]) != 1:
                                        j += 1
                                        l = len(list) - 1
                                        s = len(num)
                                    elif l == len(list) - 1:
                                        if s == len(num) - 1:
                                            if minim == 0:
                                                minim = int(list[0])
                                                index = j
                                            elif int(list[l - 1]) < minim and int(list[l - 1]) > 0:
                                                minim = int(list[0])
                                                index = j
                                l += 1
                    s += 1
            if minim > 0:
                break
    print(get_index(minim, index))


def get_index(minim, index):
    i = 1
    answer = 0
    while i < len(str(minim)) + 1:
        if len(str(minim)) == 1:
            answer = minim
        else:
            if i == 1:
                answer += 9
            elif i < len(str(minim)) and i > 1:
                answer += int('8' + '9'*(i - 1))
            elif i == len(str(minim)):
                answer += (minim - (int('9'*(i-1)) + 1)) * i + 1
        i += 1
    answer += index
    return answer

while True:
    x = input("Введите подпоследовательность: ")
    if len(x) <= 50:
        search_index(x)
    else:
        print("Количество символов должно быть меньше 50!")
