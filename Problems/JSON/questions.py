'''
Count total departments.
Count total employees.
Find average salary.
Find youngest employee.
Find employees older than 25.
Print all unique skills.
Find department with highest total salary.
Convert all employee names to uppercase.
Add a new employee and save the JSON.
Sort employees by salary in descending order.
'''


import json as j

with open("C:\\Users\\asus\\Desktop\\Selenium-Python\\Problems\\JSON\\employees.json", "r") as file:
    data = j.load(file)
    
    # Count total departments.
    
    print(f"The total number of departments are: {len(data['departments'])}")
    print("****************************************************************")
    # Count total employees.
    count = 0
    for i in range(len(data["departments"])):
        for employee in data["departments"][i]["employees"]:
            count = count + 1
            
    print(count)
    