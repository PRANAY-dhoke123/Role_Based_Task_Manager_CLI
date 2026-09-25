from cli import admin_menu , employee_menu , manager_menu
from utils.input_helper import safe_int

class Application:

    def start(self):

        while True :
            print("\n######## ROLE BASED TASK MANAGEMENT ######### \n")
            print("Login As : ")
            print("\t1. Admin ")
            print("\t2. Manager ")
            print("\t3. Employee ")
            print("\t4. Exit ")

            user_choice = safe_int("Enter your choice ")

            if user_choice == 1:
                print("\nWelcome Admin")
                admin_menu.menu_admin()
                
            elif user_choice == 2:
                print("Welcome Manager")
                manager_menu.menu_manager()
            elif user_choice == 3:
                print("Welcome Employee")
                employee_menu.menu_employee()

            elif user_choice == 4 :
                print("Thank You")
                break
            else:
                print("Please Enter a Valid Input")



                
