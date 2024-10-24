def main():
    tasks = []
    
    while True :
        print("===== to-do List =====")
        print("1. add task")
        print("2. show task")
        print("3. mark task as done")
        print("4. exit")
    
        choice = input("enter your choice:")
    
        if choice == '1':
            print()
            n_tasks = int(input("How any task you want to add:"))
       
            for i in range(n_tasks):
               task = input("enter the tasks :") 
               tasks.append({"task": task, "done": False})
               print("task added!")
           
          
        elif choice == '2':
             print("\ntasks:")
             for index, task in enumerate(tasks):
                 status = "done" if task["done"]else "Not Done"
                 print(f"{index + 1}. {task['task']} - {status}")
            
        elif choice =='3':
             task_index = int(input("enter the task number of mark as done:")) - 1 
             if 0 <= task_index < len(tasks):
                 tasks[task_index]["done"] = True
                 print("task marked as done!")
             else:
                 print("invaid task number.")     
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
main()