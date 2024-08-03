import statistics as st

def read_array_from_file(file_path):
    # функция импортирует элементы из файла в лист
    massive = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                massive.append(int(line))
    return massive

def delta(massive, mean):
   # отклонение от среднего значения
   # mean: среднее значение массива
    list_d = [abs(number-mean) for number in massive]
    return sum(list_d)/len(list_d)



def filtr_deviation(massive, x_mean, delta):
    # функция выборки значений массива находящиеся в диапазоне отклонения
    filtr_list =[]
    for number in massive:
        if abs(number-x_mean) <= delta:
            filtr_list.append(number)
    return filtr_list
 


def counting_move(massive, number):
    # счетчик количества перемещений
    count = 0
    for digital in massive:
        count+=abs(digital-number)
    return count

def gradient_descent(massive, filtr_mean):
    # filtr_mean: среднее значение после фильтрации массива с помощью функции filtr_deviation
    # реализована проверка ближайших значений к filtr_mean на минимальное количество ходов
    min_move = counting_move(massive, filtr_mean)
    
    while True:
        number =filtr_mean+1
        if counting_move(massive, number) < min_move:
            min_move = counting_move(massive, number)
        else:
            break
        
    while True:
        number =filtr_mean-1
        if counting_move(massive, number) < min_move:
            min_move = counting_move(massive, number)
        else:
            break
    return min_move
        
    
def minimal_move(path = input("введите путь к файлу:")):
    massive = read_array_from_file(path)
    mean = round(st.mean(massive))
    delta_x = delta(massive, mean)
    filtr_mean = round(st.mean(filtr_deviation(massive, mean, delta_x)))
    print(gradient_descent(massive, filtr_mean))

    
minimal_move()    
    
    
    
    
    