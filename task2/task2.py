import argparse

def import_datat2(path1, path2 ):
    # функция для импорта данных из файлов
    with open(path1,"r") as f1, open(path2,"r") as f2:
        fr1 = f1.read()
        circle_value = tuple(map(float,(fr1.split())))
        # кортеж содержит данные x, y, r окружности
        points_coordinat = []
        # лист для хранения данных x,y координат точек
        for line in f2:
            pair = tuple(map(float, line.split()))
            points_coordinat.append(pair)
        return (circle_value, points_coordinat)
    
    

        
def points_in_out_circle(circle_value, points_coordinat):
    # функция для определения вхождения точек в окружность
    # circle_value: кортеж содержит данные x, y, r окружности
    # points_coordinat: лист для хранения данных x,y координат точек
    x, y, r = circle_value
    cout = 0
    for point in points_coordinat:
        if ((point[0] - x)**2 + (point[1] - y)**2)**0.5 < r:
            print(cout, "точка внутри", sep="-", end="\n")
        elif ((point[0] - x)**2 + (point[1] - y)**2)**0.5 == r:
            print(cout, "точка лежит на окружности", sep="-",end="\n")
        else:
            print(cout, "точка снаружи", sep="-", end="\n")
        cout += 1
            


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path1", type=str)
    parser.add_argument("path2", type=str)
    args = parser.parse_args()
    
    points_in_out_circle(*import_datat2(args.path1, args.path2))
    
    
if __name__ == "__main__":
    main()