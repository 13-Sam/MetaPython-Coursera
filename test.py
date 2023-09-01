import json
from employee import details, employee_name, age, title



def create_dict(name, age, title):
    
    ### WRITE SOLUTION HERE
    employee_info = {
        'name' : str(employee_name),
        'age' : str(age),
        'title' : str(title)
    }
    return employee_info

print(create_dict(employee_name, age, title))