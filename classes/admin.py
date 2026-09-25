
from classes.user import Company
from utils.input_helper import safe_int


class Admin(Company):     
    

    # For adding the employee data in the list and the save to file
    def add_employee_details(self):
        self.emp_id = safe_int("Enter the Employee ID: ")

        for E in Company.emp_list:
            if E[0] == self.emp_id :
                print(f"{self.emp_id} This ID already available ")
                return 

        self.emp_name = input("Enter the Employee Name : ")
        self.emp_email = input("Enter the Email ID of Employee : ")
        self.emp_mo_no = safe_int("Enter Employee Mobile Number : ")
        self.emp_depart = input("Enter the Department of Employee: ")
        self.emp_role = input("Enter the role of Employee: ")

        E = [self.emp_id , self.emp_name ,self.emp_email , self.emp_mo_no , self.emp_depart , self.emp_role]
        Company.emp_list.append(E)
        

    

    #For the Loading all  employee data 
    def load_all_emp(self):
        for E in Company.emp_list:
            print(E)


    #For deleting the data from the list 
    def delete_employee_details(self,del_emp_id):
        self.del_emp_id  = del_emp_id  

        found = False
        for E in Company.emp_list:
            if E[0] == self.del_emp_id:
                Company.emp_list.remove(E)
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
        for E in Company.emp_list:
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

