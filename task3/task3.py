import json

def create_report(test_path = input("введите путь к файлу с данными теста:"),
                  values_path = input("введите путь к файлу с данными значений:"),
                  report_path = input("введите путь для сохранения отчета:")):
    
    with open(test_path, "r") as test, open(values_path, "r") as values, open(report_path, "w") as report:
        test_data = json.load(test)
        values_data = json.load(values)
        
        

