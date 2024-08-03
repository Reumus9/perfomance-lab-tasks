massive = int(input("введите длину массива:")) 
# длина кругового массива
interval = int(input("введите интервал обхода:"))
# интервал обхода

path = []
# переменная хранения пути

massive_value = 1


while True:
    for cout in range(interval):   
        if cout == 0:
            path.append(massive_value)
        else:
            massive_value += 1
        if massive_value > massive:
            massive_value = 1
            
    if massive_value == 1:
        break

print(f"полученный путь:{"".join(map(str, path))}")
