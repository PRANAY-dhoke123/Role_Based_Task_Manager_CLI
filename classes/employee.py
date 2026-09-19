import json 
from classes.company import Company

class Employee(Company):    
    

    def view_profile(self,emp_id):
        found  = False 
        for E in Company.emp_list :
            if E[0] == emp_id :                   
                print("\n===== Employee Profile =====")
                print(f"Employee ID     : {E[0]}")
                print(f"Employee Name   : {E[1]}")
                print(f"Employee Email  : {E[2]}")
                print(f"Mobile No       : {E[3]}")
                print(f"Department      : {E[4]}")
                print(f"Role            : {E[5]}")
                print("============================")
                found = True
                break
        if found == False:
            print(" Please enter a Valid Employee ID : ")

    def my_task(self,emp_id ):
        found = False
        for E in Company.task_list:
            if E['Task Assigning To'] == emp_id:
                found = True
                print("\n===== Your Tasks =====")
                for key, value in E.items():
                    print(f"{key}: {value}")
                print("============================")

        if found == False :
            print("NO Task Assigned")

    def search_task(self,task_id):
        found = False 
        for E in Company.task_list:
            if E['Task ID'] == task_id :
                print("\n===== Your Tasks =====")
                for key, value in E.items():
                    print(f"{key}: {value}")
                print("============================")
                found = True
                break
        if found == False :
            print("No tasks ")

    def task_details(self,task_id):
        
        found = False 
        for E in Company.task_list:
            if E['Task ID'] == task_id :
                print("\n===== Your Tasks  Descriptions =====")
                print(f"Task ID           : {E['Task ID']}")
                print(f"Task Title        : {E['Task Title']}")
                print(f"Task Description  : {E['Task Description']}") 
                found = True 
                print("============================")
                break
        if found == False:
            print("No tasks")



    def change_status(self,task_id,emp_id):
        
        found = False
        for E in Company.task_list:
            if E['Task ID'] == task_id and E["Task Assigning To"] == emp_id :
                data_status = input("What is new status  :  ")
                E['Task Status'] = data_status
                self.save_task()
                found = True
                print(f"######## Sucessfully Change Status of {task_id}##########")
                break
        if found == False :
            print("Not changed Status : ")


    
            


# Main Employee Code 
E1 = Employee()



def menu_employee():
    while True :
        print("\t1. View Profile ")
        print("\t2. View My Tasks ")
        print("\t3. Search Task")
        print("\t4. View Task Details")
        print("\t5. Update Task Status ")
        print("\t6. Logout ")

        employee_choice = int(input("Enter your choice : "))
        
        
        if employee_choice == 1 :
            print("View  My Profile : ")
            emp_id = int(input("Enter Your Employee ID : "))
            E1.view_profile(emp_id)
            
            

        elif  employee_choice == 2 :
            print("View My Task : ")
            emp_id = int(input("Enter Your Employee ID : "))
            E1.my_task(emp_id)
            
            


        elif employee_choice == 3 :
           print("Search Task : ")
           task_id = int(input("Enter the ID of the task : "))
           E1.search_task(task_id)


        elif employee_choice == 4 :
            print("View Task Details") 
            task_id = int(input("Enter the Task ID for Details : "))
            E1.task_details(task_id)



        elif employee_choice == 5 :
            print("Update Task Status : ")
            task_id = int(input ("Enter the Task ID for changing Status : "))
            emp_id = int(input("Enter Your Employee ID : "))
            E1.change_status(task_id,emp_id)

        elif employee_choice == 6 :
            print("\nThank You Employee \n") 

            break 
        else:
            print("\nEnter a valid Input Admin \n")