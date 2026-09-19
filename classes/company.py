# This is the main Parent class 
import json 


class Company:

    emp_list = []    
    task_list = []

    # Load employee data
    def load_emp(self):
        with open("data/employee.json", "r") as file:
            Company.emp_list = json.load(file)

    # Save employee data
    def save_emp(self):
        with open("data/employee.json", "w") as file:
            json.dump(Company.emp_list, file, indent=4)

    # Load task data
    def load_task(self):
        with open("data/tasks.json", "r") as file:
            Company.task_list = json.load(file)

    # Save task data
    def save_task(self):
        with open("data/tasks.json", "w") as file:
            json.dump(Company.task_list, file, indent=4)



C1= Company()
C1.load_emp()
C1.save_emp()
C1.load_task()
C1.save_task()
