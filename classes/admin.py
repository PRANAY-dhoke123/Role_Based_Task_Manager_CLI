class Admin:    

    emp_list = []

    def add_employee_details(self):
        self.emp_id = int(input("Enter the Employee ID: "))
        self.emp_name = input("Enter the Employee Name : ")
        self.emp_email = input("Enter the Email ID of Employee : ")
        self.emp_mo_no = int(input("Enter Employee Mobile Number : "))
        self.emp_depart = input("Enter the Department of Employee: ")
        self.emp_role = input("Enter the role of Employee: ")

        E = [self.emp_id , self.emp_name ,self.emp_email , self.emp_mo_no , self.emp_depart , self.emp_role]
        Admin.emp_list.append(E)
        print("####  Sucessfully Added Employee  ########### \n")
        

    def delete_employee_details(self,del_emp):
        self.del_emp = del_emp

        for E in Admin.emp_list:
            if E[0] == self.del_emp:
                removed  = Admin.emp_list.remove(E)
                print(f"###### Sucessfully Deleted Employee {removed} details ")
            else:
                print("Enter a valid  Employee ID for deleting ")

    def all_emp():
        for emp in Admin.emp_list:
            print(emp)


    def find_emp(self, emp_id):
        self.emp_id = emp_id 

        for E in Admin.emp_list:
            if self.emp_id in E :
                print(E)
            else:
                print(f"{self.emp_id}Not in the List ")





# Main Admin Code 
A1 = Admin()

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

        elif admin_choice == 2 :
            print("Deleting the Details of Employee ")
            del_emp = int(input("Enter the Employee ID for Delete : "))
            A1.delete_employee_details(del_emp)


        elif admin_choice == 3 :
            print("View Employee Details  ")
            emp_id = int(input("Enter the ID of the Employee For Details : "))
            A1.find_emp(emp_id)

        elif admin_choice == 4 :
            print(" All Employee Details : ")
            A1.all_emp()

        elif admin_choice == 5 :
            print("Thank You Admin ") 

            break 
        else:
            print("Enter a valid Input Admin ")