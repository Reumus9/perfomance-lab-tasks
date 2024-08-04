import json

def recursive_search_id(dictionary, id, value):
    if isinstance(dictionary, list):
        for item in dictionary:
            recursive_search_id(item, id, value)
    elif isinstance(dictionary, dict):
        if "id" in dictionary and dictionary["id"] == id:
            dictionary["value"] = value
        else:
            for key in dictionary:
                recursive_search_id(dictionary[key], id, value)

def create_report(test_path = input("введите путь к файлу с данными теста:"),
                  values_path = input("введите путь к файлу с данными значений:"),
                  report_path = input("введите путь для сохранения отчета:")):
    
    with open(test_path, "r") as test, open(values_path, "r") as values, open(report_path, "w") as report:
        test_data = json.load(test)
        values_data = json.load(values)
        for key in values_data["values"]:
            recursive_search_id(test_data["tests"], key["id"], key["value"])

        json.dump(test_data, report, indent=4)
        
create_report()
            
    
        
        

