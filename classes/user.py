# This is the main Parent class 
import json 
from models.employee import  EmployeeRecord 
from models.task import Task

class Company:

    emp_list = []    
    task_list = []

    # Load employee data
    def load_emp(self):
        with open("data/employee.json", "r") as file:
            raw_data = json.load(file)
            Company.emp_list = [EmployeeRecord(*item) for item in raw_data]


    # Save employee data
    def save_emp(self):
        with open("data/employee.json", "w") as file:
            raw_data = [
                [e.emp_id, e.name, e.email, e.mobile, e.department, e.role]
                for e in Company.emp_list
            ]
            json.dump(raw_data, file, indent=4)

    # Load task data
    def load_task(self):
        with open("data/tasks.json", "r") as file:
            #Company.task_list = json.load(file)
            raw_list = json.load(file)
            Company.task_list = [Task.from_dict(d) for d in raw_list]
            
    # Save task data
    def save_task(self):
        with open("data/tasks.json", "w") as file:
            #json.dump(Company.task_list, file, indent=4)
            json.dump([t.to_dict() for t in Company.task_list], file , indent=4)

