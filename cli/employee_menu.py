from classes.employee import E1
from utils.input_helper import safe_int


def menu_employee():
    while True :
        print("\t1. View Profile ")
        print("\t2. View My Tasks ")
        print("\t3. Search Task")
        print("\t4. View Task Details")
        print("\t5. Update Task Status ")
        print("\t6. Logout ")

        employee_choice = safe_int("Enter your choice : ")
        
        
        if employee_choice == 1 :
            print("View  My Profile : ")
            emp_id = safe_int("Enter Your Employee ID : ")
            E1.view_profile(emp_id)
            
            

        elif  employee_choice == 2 :
            print("View My Task : ")
            emp_id = safe_int("Enter Your Employee ID : ")
            E1.my_task(emp_id)
            
            


        elif employee_choice == 3 :
           print("Search Task : ")
           task_id = safe_int("Enter the ID of the task : ")
           E1.search_task(task_id)


        elif employee_choice == 4 :
            print("View Task Details") 
            task_id = safe_int("Enter the Task ID for Details : ")
            E1.task_details(task_id)



        elif employee_choice == 5 :
            print("Update Task Status : ")
            task_id = safe_int("Enter the Task ID for changing Status : ")
            emp_id = safe_int("Enter Your Employee ID : ")
            E1.change_status(task_id,emp_id)

        elif employee_choice == 6 :
            print("\nThank You Employee \n") 

            break 
        else:
            print("\nEnter a valid Input Admin \n")