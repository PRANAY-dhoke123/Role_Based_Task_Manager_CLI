import json 
from classes.company import Company

class Manager(Company):
    


    #Creating a Task and saving in dict and then in list 
    def create_task(self):        
        self.task_id = int(input("Enter the Task ID : "))
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
        for E in Company.task_list:
            for key, value in E.items():
                print(f"\t{key}: {value}")
            print("-"*80)
                
    # getting data of employee for assiginig the task 
    def get_emp_data(self):
        with open("data/employee.json" , "r")  as file:
            emp_data = json.load(file)
            print("List of Employee : ")
            for E in emp_data :
                print(f" {E[0]} : {E[1]} : {E[4]} : {E[5]} ")

    # For assisining the task 
    def assigning_task(self,assign,task_id):
        found = False
        for E in Company.task_list:
            if E["Task ID"] == task_id:
                E["Task Assigning To"] = assign
                self.save_task()
                found = True
                break 
        if found == False:
            print("Not a Valid Task ID : ")            

    # for checking the Assigned Task 
    def assigned_task(self):
        for E in Company.task_list:
            if E['Task Assigning To'] is not None:
                print(f"{E['Task ID']} : {E['Task Title']}   :   {E['Task Description']} : {E['Task Assigning To']}")
        


    # for updating the task details :
    def update_task(self,update_id):
        found = False
        changed = False
        for E in Company.task_list:
            if update_id == E['Task ID']:
                found = True
                change = input("Enter What to change : ")
                if change in  E and change != "Task ID":
                    data = input("Enter the Value of update ")
                    E[change] = data
                    self.save_task()
                    changed = True 
                    break
        
        if found == False:
            print("Invalid Task ID : ")
        if changed == False:
            print("Not Updated ")





    # Search for the task by id

    #status
    def task_status(self):
        for E in Company.task_list:
            print(f"{E['Task ID']}  :  {E['Task Title']}   : {E['Task Status']}")


    
    #change status of Task
    def change_status(self,task_id):
        
        found = False
        for E in Company.task_list:
            if E['Task ID'] == task_id :
                data_status = input("What is new status  :  ")
                E['Task Status'] = data_status
                self.save_task()
                found = True
                print(f"######## Sucessfully Change Status of {task_id}##########")
                break
        if found == False :
            print("Not changed Status : ")

    # deleting the Task
    def delete_task(self,del_id):
        found = False 
        for E in Company.task_list:
            if E['Task ID'] == del_id :
                Company.task_list.remove(E)
                self.save_task()
                found = True
                break
        if found == False:
            print("Delete Doesn't occur : ")

    def search_task(self,search_id):
        found = False
        for E in Company.task_list:
            if search_id == E['Task ID']:
                for key, value in E.items():
                    print(f"\t{key}: {value}")
                found = True
                break
        
        if found == False:
            print("Invalid Task ID : ")


# Main Code 
M1 = Manager()


def menu_manager():
    while True:
        print("""
                1. Create Task
                2. View All Tasks
                3. Assign Task
                4. View Assigned Tasks
                5. Update Task
                6. Change Status
                7. Reassign Task
                8. Delete Task
                9. Search Task
                10. Logout """)

        man_choice = int(input("Enter the Choice : "))

        if man_choice == 1 :
            print("Creating a Task  : ")
            M1.create_task()
            M1.save_task()
            print("\n#### Sucessfully  Created a Task #########\n")

        elif man_choice == 2 :
            print("View All Task ")
            M1.view_all_task()

        elif man_choice == 3 :
            print("Assign Task : ")
            M1.get_emp_data()
            M1.view_all_task()
            task_id = int(input("Enter the Task ID for assigning : "))
            assign = int(input("Enter the ID of employee for Assigning Task : "))
            M1.assigning_task(assign,task_id)            

        elif man_choice == 4 :
            print("View Assigned Tasks : ")
            M1.assigned_task()

        elif man_choice == 5 :
            print("Update Task : ")
            update_id = int(input("Enter the Task ID to Update : "))
            M1.update_task(update_id)
            

        elif man_choice == 6 :
            print("Change Status : ")
            M1.task_status()
            task_id = int(input("Enter the Task id for change status  :  "))
            M1.change_status(task_id)

        elif man_choice == 7 :
            print("Reassign Task : ")            
            M1.get_emp_data()
            M1.view_all_task()
            task_id = int(input("Enter the Task ID for reassigning : "))
            assign = int(input("Enter the ID of employee for reassigning Task : "))
            M1.assigning_task(assign,task_id) 




        elif man_choice == 8 :
            print("Delete Task : ")
            M1.status()
            del_id = int(input("Enter the Task id for delete : "))
            M1.delete_task(del_id)

        elif man_choice == 9 :
            print("Search Task : ")
            search_id = int(input("Enter the Task ID to Search : "))
            M1.search_task(search_id)




        elif man_choice == 10 :
            print("Thank You Manager ")
            break
        else:
            print("Enter a valid Input Manager ")

