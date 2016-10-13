def main():
    while True:
        map = []
        x = int(input("Количество островов: "))
        for i in range(x):
            map.append(input_isl())
        for i in map:
            island(i)

def input_isl():
    x = input("Размер острова: ")
    a = []
    b = x.split()
    for i in range(int(b[0])):
        a.append(list(map(int, input("Размер: ").split())))
    # print(a)
    return a

def island(mas):
    #mas = [[5, 3, 4, 5], [6, 2, 1, 4], [3, 1, 1, 4], [8, 5, 4, 3]]
    #mas = [[2, 2, 2], [2, 1, 2], [2, 1, 2], [2, 1, 2]]
    square = []                                                             # клетки острова
    arr = {}                                                                # массив распределенных по высоте клеток

    for i in range(len(mas)):  # заполняем объекты
        square.append([])
        for j in range(len(mas[i])):
            near = []                                                       # клетки, граничащие с данной
            if i == 0 or j == 0 or i == len(mas)-1 or j == len(mas[i])-1:
                status = 1
            else:
                status = 0
                near.append([mas[i-1][j], i-1, j])
                near.append([mas[i][j+1], i, j+1])
                near.append([mas[i+1][j], i+1, j])
                near.append([mas[i][j-1], i, j-1])
            if mas[i][j] not in arr:
                arr.setdefault(mas[i][j], [[i, j]])
            else:
                arr[mas[i][j]].append([i, j])

            square[i].append({'height': mas[i][j], 'old_height': mas[i][j], 'status': status, 'near': near})

    local = []
    j = 0
    buffer = []
    for i in arr.keys():
        buffer.append(i)
    for m in buffer:                        # пройдемся по имеющимся высотам клеток
        #print("water level: %d" %m)
        curr = arr[m]                               # клетки текущего уровня воды
        l=0
        while len(curr) > 0:                        # распределим квадраты одинаковой высоты по секторам
            local.append([curr.pop()])
            while j < len(local[l]):
                for i in curr:
                    for k in square[local[l][0][0]][local[l][0][1]]['near']:
                        if i == [k[1], k[2]]:
                            local[l].append(curr.pop())
                j += 1
            j = 0
            l += 1
        #print(local)
        for i in local:                             # пройдемся по секторам
            search_min(i, square, m)                # определим низшую граничную точку и поднимем воду на ее уровень
            for k in i:
                # print(k)
                if square[k[0]][k[1]]['status'] == 0:
                    arr[buffer[buffer.index(m)+1]].append(k)
                    #square[k[0]][k[1]]['height'] = next[0] if next[0] > m else square[k[0]][k[1]]['height']
                    # print(square[k[0]][k[1]].height)
        local = []
    #print(square)
    vol = volume(square)
    print(vol)

def search_min(list, square, level):
    mins = []
    next = []
    for i in list:
        if square[i[0]][i[1]]['status'] != 1:
            for j in square[i[0]][i[1]]['near']:
                next.append(j)
                mins.append(j[0] if j[0] > level else level)

    for i in next:
        a = min(mins)
        if square[i[1]][i[2]]['height'] <= a and square[i[1]][i[2]]['status'] != 0:
            for j in range(len(list)):
                square[list[0][0]][list[0][1]]['status'] = 2
                square[list[0][0]][list[0][1]]['height'] = a
                list.pop(0)
            break
        elif square[i[1]][i[2]]['height'] <= a:
            square[list[0][0]][list[0][1]]['height'] = a

def volume(square):
    volume = 0
    for i in square:
        for j in i:
            volume += j['height'] - j['old_height']
    return volume


main()

