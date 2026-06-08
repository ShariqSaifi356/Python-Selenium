import json as j

with open("C:\\Users\\asus\\Desktop\\Selenium-Python\\Problems\\JSON\\employees.json", "r") as file:
    data = j.load(file)
    
    print(data["company"])
    print(data["location"])
    print(data["isHiring"])
    print(data["departments"][0]["name"])
    print(data["departments"][1]["manager"])
    print(len(data["departments"]))
    
    
    for i in range(len(data["departments"])):
        for employee in data["departments"][i]["employees"]:
            print(employee["name"])
            
    print("@@@@@@@@@@@@@@@@@@@@")
    
    for i in range(len(data["departments"])):
        for employee in data["departments"][i]["employees"]:
            print(f'''{employee["name"]} - {employee["salary"]}''')
            
        print("@@@@@@@@@@@@@@@@@@@@")
        
    maximum = 0
    employee_name = ""
        
    for i in range(len(data["departments"])):
        for employee in data["departments"][i]["employees"]:
            if maximum < employee["salary"]:
                maximum = employee["salary"]
                employee_name = employee["name"]

    print(f"{employee_name} - {maximum}")

    print("@@@@@@@@@@@@@@@@@@@@")          
        
        
    for i in range(len(data["departments"])):
        for employee in data["departments"][i]["employees"]:
            if "Python" in employee["skills"]:
                print(employee["name"])
                
    print("@@@@@@@@@@@@@@@@@@@@")
    
    total_salary = 0
    
    for i in range(len(data["departments"])):
        for employee in data["departments"][i]["employees"]:
            total_salary = total_salary + employee["salary"]
            
    print(total_salary)