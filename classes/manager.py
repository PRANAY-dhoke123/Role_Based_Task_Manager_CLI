
from classes.user import Company
from utils.input_helper import safe_int

class Manager(Company):
    


    #Creating a Task and saving in dict and then in list 
    def create_task(self):        
        self.task_id = safe_int("Enter the Task ID : ")

        for T in Company.task_list:
            if T['Task ID'] == self.task_id:
                print(f"{self.task_id } - Task ID already Exits")
                return


        self.task_title = input("Enter the Task Title  : ")
        self.descp = input("Enter Description of Task : ")
        self.assign = None
        self.priority = input("Enter the Priority : ")
        self.deadline = input("Enter the Date of Deadline : ")
        self.status = input("Enter the status of Task : ")

        task_dict = {
                    "Task ID" : self.task_id ,
                    "Task Title" : self.task_title ,
                    "Task Description" : self.descp , 
                    "Task Assigning To" : self.assign ,
                    "Task Priority" : self.priority,
                    "Task Deadline" : self.deadline,
                    "Task Status" : self.status
                }
        Company.task_list.append(task_dict)

    
    
    
    #For View All Task 
    def view_all_task(self):
        print("List of Tasks ")
        print("\n===== ALL TASK LIST  =====")
        for E in Company.task_list:
            for key, value in E.items():
                print(f"\t{key}: {value}")
            print("============================")
                
    # getting data of employee for assiginig the task 
    def get_emp_data(self):
        print("\n===== EMPLOYEE LIST =====")
        for E in Company.emp_list:
            print(f"Employee ID: {E[0]}")
            print(f"Employee Name: {E[1]}")
            print(f"Employee Designation: {E[4]}")
            print(f"Employee Status: {E[5]}")
        print("============================")

    # For assisining the task 
    def assigning_task(self,assign,task_id):
        if not any(e[0] == assign for e in Company.emp_list):
            print("Employee does not exist")
            return
        found = False
        for E in Company.task_list:
            if E["Task ID"] == task_id:
                E["Task Assigning To"] = assign
                
                self.save_task()
                print("\n===== TASK ASSIGNED SUCCESSFULLY =====")       
                print(f"Task ID       : {E['Task ID']}")
                print(f"Task Title    : {E['Task Title']}")
                print(f"Assigned To   : {E['Task Assigning To']}")
                print("======================================")
                found = True
                break 
        if found == False:
            print("Not a Valid Task ID : ")            

    # for checking the Assigned Task 
    def assigned_task(self):
        print("\n===== ASSIGNED TASKS =====")
        found = False
        for E in Company.task_list:
            if E['Task Assigning To'] is not None:
                print(f"Task ID       : {E['Task ID']}")
                print(f"Task Title    : {E['Task Title']}")
                print(f"Description   : {E['Task Description']}")
                print(f"Assigned To   : {E['Task Assigning To']}")
                found = True
        if found == False:
            print("No Task Assigned")
        print("============================")


    # for updating the task details :
    def update_task(self,update_id):
        found = False
        changed = False
        for E in Company.task_list:
            if update_id == E['Task ID']:
                found = True
                change = input("Enter What to change : ")
                if change in  E and change != "Task ID":
                    data = safe_int("Enter the Value of update ")
                    E[change] = data
                    self.save_task()
                    print("\n===== UPDATE TASK =====")
                    print(f"Task Title       :{E['Task Title']}")
                    print(f"Task Description :{E['Task Description']}")
                    changed = True 
                    break
        
        if found == False:
            print("Invalid Task ID : ")
        if changed == False:
            print("Not Updated ")





    # Search for the task by id

    #status
    def task_status(self):
        print("\n===== TASK STATUS =====")
        for E in Company.task_list:
            print(f"Task ID     : {E['Task ID']}")
            print(f"Task Title  : {E['Task Title']}")
            print(f"Task Status : {E['Task Status']}")
        print("============================")

    
    #change status of Task
    def change_status(self,task_id):
        
        found = False
        for E in Company.task_list:
            if E['Task ID'] == task_id :
                data_status = input("What is new status  :  ")
                E['Task Status'] = data_status
                self.save_task()
                found = True
                print("\n===== STATUS CHANGED SUCCESSFULLY =====")
                print(f"Task ID     : {E['Task ID']}")
                print(f"Task Title  : {E['Task Title']}")
                print(f"New Status  : {E['Task Status']}")
                print("=======================================")
                break
        if found == False :
            print("Not changed Status : ")

    # deleting the Task
    def delete_task(self,del_id):
        found = False 
        for E in Company.task_list:
            if E['Task ID'] == del_id :
                print("\n===== TASK DELETED =====")
                print(f"Task ID    : {E['Task ID']}")
                print(f"Task Title : {E['Task Title']}")
                Company.task_list.remove(E)
                self.save_task()
                found = True
                print("Task Deleted Successfully")
                print("============================")
                break
        if found == False:
            print("\nDelete Doesn't Occur")
            print("Invalid Task ID")

    def search_task(self,search_id):
        found = False
        for E in Company.task_list:
            if search_id == E['Task ID']:
                print("\n===== TASK DETAILS =====")
                print(f"\tTask ID: {E['Task ID']}")
                print(f"\tTask Title: {E['Task Title']}")
                print(f"\tTask Description: {E['Task Description']}")
                print(f"\tTask Assigning To: {E['Task Assigning To']}")
                print(f"\tTask Priority: {E['Task Priority']}")
                print(f"\tTask Deadline: {E['Task Deadline']}")
                print(f"\tTask Status: {E['Task Status']}")
                print("============================")
                found = True
                break
        
        if found == False:
            print("Invalid Task ID : ")


# Main Code 
M1 = Manager()
