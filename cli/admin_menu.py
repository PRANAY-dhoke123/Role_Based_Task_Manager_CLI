
from utils.input_helper import safe_int


def menu_admin(A1):
    while True :
        print("\t1. Add Employee ")
        print("\t2. Delete Employee ")
        print("\t3. View Employee Details")
        print("\t4. View All Employee")
        print("\t5. Exit ")

        admin_choice =  safe_int("Enter your choice : ")

        if admin_choice == 1 :
            print("Enter the Details of Employee ")
            A1.add_employee_details()
            A1.save_emp()
            print("\n####  Sucessfully Added Employee  ########### \n")


        elif admin_choice == 2 :
            print("Deleting the Details of Employee ")
            del_emp_id  = safe_int("Enter the Employee ID for Delete : ")
            A1.delete_employee_details(del_emp_id)


        elif admin_choice == 3 :
            print("View Employee Details  ")
            emp_id = safe_int("Enter the ID of the Employee For Details : ")
            A1.find_emp(emp_id)


        elif admin_choice == 4 :
            print(" All Employee Details : ")
            A1.load_all_emp()
            print("\n#######  Sucessfully Display All Employees Deatils  ###########\n")


        elif admin_choice == 5 :
            print("\nThank You Admin\n") 

            break 
        else:
            print("\nEnter a valid Input Admin \n")