from classes.manager import M1
from utils.input_helper import safe_int


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

        man_choice = safe_int("Enter the Choice : ")

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
            task_id = safe_int("Enter the Task ID for assigning : ")
            assign = safe_int("Enter the ID of employee for Assigning Task : ")
            M1.assigning_task(assign,task_id)            

        elif man_choice == 4 :
            print("View Assigned Tasks : ")
            M1.assigned_task()

        elif man_choice == 5 :
            print("Update Task : ")
            update_id = safe_int("Enter the Task ID to Update : ")
            M1.update_task(update_id)
            

        elif man_choice == 6 :
            print("Change Status : ")
            M1.task_status()
            task_id = safe_int("Enter the Task id for change status  :  ")
            M1.change_status(task_id)

        elif man_choice == 7 :
            print("Reassign Task : ")            
            M1.get_emp_data()
            M1.view_all_task()
            task_id = safe_int("Enter the Task ID for reassigning : ")
            assign = safe_int("Enter the ID of employee for reassigning Task : ")
            M1.assigning_task(assign,task_id) 




        elif man_choice == 8 :
            print("Delete Task : ")
            
            del_id = safe_int("Enter the Task id for delete : ")
            M1.delete_task(del_id)

        elif man_choice == 9 :
            print("Search Task : ")
            search_id = safe_int("Enter the Task ID to Search : ")
            M1.search_task(search_id)




        elif man_choice == 10 :
            print("Thank You Manager ")
            break
        else:
            print("Enter a valid Input Manager ")

