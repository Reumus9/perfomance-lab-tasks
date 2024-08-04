import json

def recursive_search_id(dictionary, id, value):
    if "id" in dictionary:
        if dictionary["id"] == id:
            dictionary["value"] = value
            return dictionary
            
    for val in dictionary:
        if isinstance(dictionary[val], list):
            dictionary[val]=recursive_search_id(val, id, value)
    
    return dictionary


def create_report(test_path = input("введите путь к файлу с данными теста:"),
                  values_path = input("введите путь к файлу с данными значений:"),
                  report_path = input("введите путь для сохранения отчета:")):
    
    with open(test_path, "r") as test, open(values_path, "r") as values, open(report_path, "w") as report:
        test_data = json.load(test)
        values_data = json.load(values)
        report_data = None
        for key in values_data["values"]:
            for val in test_data["tests"]:
                report_data =recursive_search_id(test_data,key["id"], key["value"])

        json.dump(report_data, report, indent=4)
        
create_report()
            
# пока не работает        
        
        

