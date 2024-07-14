#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
    tasks = []

    while True:
        print("\n ****** TO-DO LIST ******")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Mark Tasks")
        print("4. Delete Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            n_tasks = int(input("How many tasks do you want to add? "))
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            if not tasks:
                print("No tasks to show.")
            else:
                for i, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{i + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the number of the task to be marked as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            task_index = int(input("Enter the number of the task to be deleted: ")) - 1
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                print("Task deleted!")
            else:
                print("Invalid task number.")
       
        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



# In[ ]:




