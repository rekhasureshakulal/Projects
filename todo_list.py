def main():
    tasks = []

    def add_task():
        try:
            task = input("Enter task description: ")
            tasks.append({"task": task, "completed": False})
            print("Task added successfully.") 
            print("\n *******************************************") 
        except Exception as e:
            print("Error is : ",e)      
    

    def view_tasks():
        try:

            if len(tasks) == 0:
                print("No tasks to display.")
            else:   
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    status = "Completed" if task["completed"] else "Inprogress"
                    print(f"{i}. [{status}] {task['task']}")
        except Exception as e:
            print("Error is : ",e)
    def mark_complete():
        while True:
            view_tasks()      
            index = int(input("Enter the number of the task you want to complete: ")) - 1    

            if index < 0 or index >= len(tasks):
                print("Invalid task number.")
            elif tasks[index]["completed"]:
                print("This task is already completed.")
            else:            
                tasks[index]["completed"] = True
                print("Task marked as completed.")
                break

    def remove_task():
        try:
            while True:
                view_tasks()            
                index = int(input("Enter the task number that you want to remove: ")) - 1
                
                if index < 0 or index >= len(tasks):
                    print("Invalid task number.")
                else:
                    del tasks[index]
                    print("Task removed.")
                    break    
        except Exception as e:
            print("Error is : ",e)        

    while True:
        try:
            print("\n") 
            print("\n *******************************************")   
            print("\nMenu:")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Mark a task as completed")
            print("4. Remove a task")
            print("5. Quit")
            print("\n *******************************************") 
        
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                add_task()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                mark_complete()
            elif choice == '4':
                remove_task()
            elif choice == '5':
                print("Exiting... THANK YOU FOR USING IT")
                break
            else:
                print("Invalid choice.") 
        except Exception as e:
            print("Error is : ",e)  
print("\n *******************************************")  
print("Welcome to the To-Do List Application!")
print("This simple program allows you to manage your tasks.")
print("You can add new tasks, view existing tasks, mark tasks as completed, remove tasks, and quit the application.")
print("Let's get started!")
print("\nWhen picking a task, please enter the corresponding number from the menu.")
print("For example, if you want to add a new task, enter '1'.")
print("If you want to mark a task as completed, enter '3' and follow the prompts.")
print("Enjoy organizing your tasks!")
print("\n *******************************************")   


if __name__ == "__main__":
    main()

