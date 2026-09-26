
from classes.user import Company
from utils.input_helper import safe_int
from models.employee import EmployeeRecord


class Admin(Company):     
    

    # For adding the employee data in the list and the save to file
    def add_employee_details(self):
        emp_id = safe_int("Enter the Employee ID: ")

        for E in Company.emp_list:
            if E.emp_id  == emp_id :
                print(f"{emp_id} This ID already available ")
                return 

        emp_name = input("Enter the Employee Name : ")
        emp_email = input("Enter the Email ID of Employee : ")
        emp_mo_no = safe_int("Enter Employee Mobile Number : ")
        emp_depart = input("Enter the Department of Employee: ")
        emp_role = input("Enter the role of Employee: ")

        E = EmployeeRecord(emp_id,emp_name,emp_email,emp_mo_no,emp_depart,emp_role)
        Company.emp_list.append(E)
        

    

    #For the Loading all  employee data 
    def load_all_emp(self):
        for E in Company.emp_list:
             print(f"ID: {E.emp_id} | Name: {E.name} | Email: {E.email} | "
                  f"Mobile: {E.mobile} | Dept: {E.department} | Role: {E.role}")


    #For deleting the data from the list 
    def delete_employee_details(self,del_emp_id):
        self.del_emp_id  = del_emp_id  
        
        for E in Company.emp_list:
            if E.emp_id == self.del_emp_id:
                Company.emp_list.remove(E)
                self.save_emp()                
                print(f"\n###### Sucessfully Deleted Employee {E.emp_id} details  ########## \n")
                return 
                
        print("Not a Valid Emoloyee ID")


    # For finding the details of the employee
    def find_emp(self, emp_id):
        self.emp_id = emp_id   
                
        found = False
        for E in Company.emp_list:
            if self.emp_id == E.emp_id :
                print("\nEmployee Details:")
                print(f"Employee ID        : {E.emp_id}")
                print(f"Employee Name      : {E.name}")
                print(f"Employee Email     : {E.email}")
                print(f"Employee Mobile No : {E.mobile}")
                print(f"Department         : {E.department}")
                print(f"Role               : {E.role}")
                found = True
                print(f"\n###### Sucessfully Dsiplay Details of Employee By ID : {self.emp_id} ##########\n ")
                break

        if found == False : 
            print("Please enter a Valid Employee ID : ")
            
        

