# This file is for Menu Driven Program 
from classes import admin,employee,manager 


while True :
    print("\n######## ROLE BASED TASK MANAGEMENT ######### \n")
    print("Login As : ")
    print("\t1. Admin ")
    print("\t2. Manager ")
    print("\t3. Employee ")
    print("\t4. Exit ")

    user_choice = int(input("Enter your choice "))
    if user_choice == 1:
        print("\nWelcome Admin")
        admin.menu_admin()
        
    elif user_choice == 2:
        print("Welcome Manager")
        manager.menu_manager()
    elif user_choice == 3:
        print("Welcome Employee")
        


    elif user_choice == 4 :
        print("Thank You")
        break
    else:
        print("Please Enter a Valid Input")
