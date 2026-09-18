import json 

class Admin:    

    emp_list = []
    # Load employee data when program starts
    def load_emp(self):

        with open("data/employee.json", "r") as file:
            Admin.emp_list = json.load(file)

    # For adding the employee data in the list and the save to file
    def add_employee_details(self):
        self.emp_id = int(input("Enter the Employee ID: "))
        self.emp_name = input("Enter the Employee Name : ")
        self.emp_email = input("Enter the Email ID of Employee : ")
        self.emp_mo_no = int(input("Enter Employee Mobile Number : "))
        self.emp_depart = input("Enter the Department of Employee: ")
        self.emp_role = input("Enter the role of Employee: ")

        E = [self.emp_id , self.emp_name ,self.emp_email , self.emp_mo_no , self.emp_depart , self.emp_role]
        Admin.emp_list.append(E)
        

    def save_emp(self):
        with open ("data/employee.json", "w") as file:  
            json.dump(Admin.emp_list, file,indent = 4)

    #For the Loading all  employee data 
    def load_all_emp(self):
        for E in Admin.emp_list:
            print(E)


    #For deleting the data from the list 
    def delete_employee_details(self,del_emp_id):
        self.del_emp_id  = del_emp_id  

        found = False
        for E in Admin.emp_list:
            if E[0] == self.del_emp_id:
                Admin.emp_list.remove(E)
                self.save_emp()               
                found = True
                print(f"\n###### Sucessfully Deleted Employee {E[0]} details  ########## \n")
 
                break
        if found == False:
            print("Not a Valid Emoloyee ID")


    # For finding the details of the employee
    def find_emp(self, emp_id):
        self.emp_id = emp_id   
                
        found = False
        for E in Admin.emp_list:
            if self.emp_id == E[0] :
                print("\nEmployee Details:")
                print(f"Employee ID        : {E[0]}")
                print(f"Employee Name      : {E[1]}")
                print(f"Employee Email     : {E[2]}")
                print(f"Employee Mobile No : {E[3]}")
                print(f"Department         : {E[4]}")
                print(f"Role               : {E[5]}")
                found = True
                print(f"\n###### Sucessfully Dsiplay Details of Employee By ID : {self.emp_id} ##########\n ")
                break

        if found == False : 
            print("Please enter a Valid Employee ID : ")
            
        


# Main Admin Code 
A1 = Admin()
A1.load_emp()

def menu_admin():
    while True :
        print("\t1. Add Employee ")
        print("\t2. Delete Employee ")
        print("\t3. View Employee Details")
        print("\t4. View All Employee")
        print("\t5. Exit ")

        admin_choice = int(input("Enter your choice : "))
        if admin_choice == 1 :
            print("Enter the Details of Employee ")
            A1.add_employee_details()
            A1.save_emp()
            print("\n####  Sucessfully Added Employee  ########### \n")


        elif admin_choice == 2 :
            print("Deleting the Details of Employee ")
            del_emp_id  = int(input("Enter the Employee ID for Delete : "))
            A1.delete_employee_details(del_emp_id)


        elif admin_choice == 3 :
            print("View Employee Details  ")
            emp_id = int(input("Enter the ID of the Employee For Details : "))
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