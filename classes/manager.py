class Manager:
    task_dict = { }

    def create_task(self):
        self.task_no = int(input("Enter the Task No :"))
        self.task_details = input("Enter the Task Deatils  : ")
        Manager.task_dict[self.task_no] = self.task_details
        print("Task Created Sucessfully ")

    def all_task(self):
        for task in Manager.task_dict.items():
            print(task)



# Main Code 
M1 = Manager()

def menu_manager():
    while True:
        print("""
                1. Create Task
                2. Assign Task
                3. View All Tasks
                4. View Task Status
                5. Logout""")

        man_choice = int(input("Enter the Choice : "))

        if man_choice == 1 :
            print("Creating a Task  : ")
            M1.create_task()

        elif man_choice == 2 :
            print("Assisgning a Task to  ")

        elif man_choice == 3 :
            print("Listing all Task  : ")
            M1.all_task()

        elif man_choice == 4 :
            print("View Task status : ")
        elif man_choice == 5 :
            print("Thank You Manager ")
            break
        else:
            print("Enter a valid Input Manager ")

