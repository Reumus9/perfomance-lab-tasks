import argparse

def circle_path(massive, interval):
    # massive: длина кругового массива
    # interval:интервал обхода
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
    path = "".join(map(str, path))
    print(f"полученный путь:{path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("massive_length", type=int)
    parser.add_argument("interval", type=int)
    args = parser.parse_args()
    
    circle_path(args.massive_length, args.interval)
    
if __name__ == "__main__":
    main()
    