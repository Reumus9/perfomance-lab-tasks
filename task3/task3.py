import json
import argparse

def recursive_search_id(dictionary, id, value):
    # реализация рекурсивного поиска id
    if isinstance(dictionary, list):
        for item in dictionary:
            recursive_search_id(item, id, value)
    elif isinstance(dictionary, dict):
        if "id" in dictionary and dictionary["id"] == id:
            dictionary["value"] = value
        else:
            for key in dictionary:
                recursive_search_id(dictionary[key], id, value)

def create_report(test_path, values_path, report_path):
    
    with open(test_path, "r") as test, open(values_path, "r") as values, open(report_path, "w") as report:
        test_data = json.load(test)
        values_data = json.load(values)
        for key in values_data["values"]:
            recursive_search_id(test_data["tests"], key["id"], key["value"])

        json.dump(test_data, report, indent=4)
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("test_path", type=str)
    parser.add_argument("values_path", type=str)
    parser.add_argument("report_path", type=str)
    args = parser.parse_args()
    
    create_report(args.test_path, args.values_path, args.report_path)  
    
    
if __name__ == "__main__":
    main()          
    
        
        

