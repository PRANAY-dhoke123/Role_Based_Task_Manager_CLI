from models.task import Task
from classes.user import Company
from utils.input_helper import safe_int
 

class Manager(Company):
    


    #Creating a Task and saving in dict and then in list 
    def create_task(self):        
        self.task_id = safe_int("Enter the Task ID : ")

        for T in Company.task_list:
            if T.task_id == self.task_id:
                print(f"{self.task_id } - Task ID already Exits")
                return


        self.task_title = input("Enter the Task Title  : ")
        self.descp = input("Enter Description of Task : ")
        self.assign = None
        self.priority = input("Enter the Priority : ")
        self.deadline = input("Enter the Date of Deadline : ")
        self.status = input("Enter the status of Task : ")

        new_task = Task(self.task_id, self.task_title, self.descp, self.priority, self.deadline, status=self.status)
        Company.task_list.append(new_task)
        self.save_task()
        

    
    
    
    #For View All Task 
    def view_all_task(self):
        print("List of Tasks ")
        print("\n===== ALL TASK LIST  =====")
        for E in Company.task_list:
            for key, value in E.to_dict().items():
                print(f"\t{key}: {value}")
            print("============================")
                
    # getting data of employee for assiginig the task 
    def get_emp_data(self):
        print("\n===== EMPLOYEE LIST =====")
        for E in Company.emp_list:
            print(f"Employee ID: {E.emp_id}")
            print(f"Employee Name: {E.name}")
            print(f"Employee Designation: {E.department}")
            print(f"Employee Role: {E.role}")
        print("============================")

    # For assisining the task 
    def assigning_task(self,assign,task_id):
        if not any(E.emp_id == assign for E in Company.emp_list):
            print("Employee does not exist")
            return
        found = False
        for E in Company.task_list:
            if E.task_id == task_id:
                E.assign_to_employee(assign)
                
                self.save_task()
                print("\n===== TASK ASSIGNED SUCCESSFULLY =====")       
                print(f"Task ID       : {E.task_id}")
                print(f"Task Title    : {E.title}")
                print(f"Assigned To   : {E.assign_to}")
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
                print(f"Task ID       : {E.task_id}")
                print(f"Task Title    : {E.title}")
                print(f"Description   : {E.description}")
                print(f"Assigned To   : {E.assign_to}")
                found = True
        if found == False:
            print("No Task Assigned")
        print("============================")


    # for updating the task details :
    def update_task(self,update_id):
        field_map = {
            "Task Title": "title",
            "Task Description": "description",
            "Task Priority": "priority",
            "Task Deadline": "deadline",
        }

        found = False
        changed = False
        for E in Company.task_list:
            if update_id == E.task_id:
                found = True
                change = input("Enter What to change (Task Title / Task Description / Task Priority / Task Deadline): ")
                if change in field_map:
                    data = input("Enter the Value of update ")
                    setattr(E, field_map[change], data)
                    self.save_task()
                    print("\n===== UPDATE TASK =====")
                    print(f"Task Title       :{E.title}")
                    print(f"Task Description :{E.description}")
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
            print(f"Task ID     : {E.task_id}")
            print(f"Task Title  : {E.title}")
            print(f"Task Status : {E.status}")
        print("============================")

    
    #change status of Task
    def change_status(self,task_id):
        
        found = False
        for E in Company.task_list:
            if  E.task_id == task_id :
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
                print("\n===== STATUS CHANGED SUCCESSFULLY =====")
                print(f"Task ID     : {E.task_id}")
                print(f"Task Title  : {E.title}")
                print(f"New Status  : {E.status}")
                print("=======================================")  
                found = True
                break
                
        if found == False :
            print("Not changed Status : ")

    # deleting the Task
    def delete_task(self,del_id):
        found = False 
        for E in Company.task_list:
            if  E.task_id == del_id :
                print("\n===== TASK DELETED =====")
                print(f"Task ID    : {E.task_id}")
                print(f"Task Title : {E.title}")
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
                print(f"\tTask ID: {E.task_id}")
                print(f"\tTask Title: {E.title}")
                print(f"\tTask Description: {E.description}")
                print(f"\tTask Assigning To: {E.assign_to}")
                print(f"\tTask Priority: {E.priority}")
                print(f"\tTask Deadline: {E.deadline}")
                print(f"\tTask Status: {E.status}")
                print("============================")
                found = True
                break
        
        if found == False:
            print("Invalid Task ID : ")


