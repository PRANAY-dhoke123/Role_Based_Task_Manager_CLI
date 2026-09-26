from utils.input_helper import safe_int
from classes.user import Company

class Employee(Company):    
    

    def view_profile(self,emp_id):
        found  = False 
        for E in Company.emp_list :
            if E.emp_id == emp_id :                   
                print("\n===== Employee Profile =====")
                print(f"Employee ID     : {E.emp_id}")
                print(f"Employee Name   : {E.name}")
                print(f"Employee Email  : {E.email}")
                print(f"Mobile No       : {E.mobile}")
                print(f"Department      : {E.department}")
                print(f"Role            : {E.role}")
                print("============================")
                found = True
                break
        if found == False:
            print(" Please enter a Valid Employee ID : ")

    def my_task(self,emp_id ):
        found = False
        for E in Company.task_list:
            if E.assign_to == emp_id:
                found = True
                print("\n===== Your Tasks =====")
                for key, value in E.to_dict().items():
                    print(f"{key}: {value}")
                print("============================")

        if found == False :
            print("NO Task Assigned")

    def search_task(self,task_id,emp_id):
        found = False 
        for E in Company.task_list:
            if E.task_id == task_id  and E.assign_to == emp_id :
                print("\n===== Your Tasks =====")
                for key, value in E.to_dict().items():
                    print(f"{key}: {value}")
                print("============================")
                found = True
                break
        if found == False :
            print("No tasks ")

    def task_details(self,task_id,emp_id):
        
        found = False 
        for E in Company.task_list:
            if E.task_id == task_id  and E.assign_to == emp_id:
                print("\n===== Your Tasks  Descriptions =====")
                print(f"Task ID           : {E.task_id}")
                print(f"Task Title        : {E.title}")
                print(f"Task Description  : {E.description}") 
                found = True 
                print("============================")
                break
        if found == False:
            print("No tasks")



    def change_status(self,task_id,emp_id):
        
        found = False
        for E in Company.task_list:
            if E.task_id == task_id and E.assign_to == emp_id :
                print("\n1. Pending")
                print("2. In Progress")
                print("3. Completed")

                choice_status = safe_int("Enter your choice of status  :  ")
                status_map = {   1: "Pending", 2: "In Progress", 3: "Completed"  }

                if choice_status not in status_map:
                    print("Invalid status.")
                    return
                
                E.update_status(status_map[choice_status])
                self.save_task()
                print(f"######## Sucessfully Change Status of {task_id} ##########")                
                found = True
                break
        if found == False :
            print("Not changed Status : ")