task_list = []
task_status = []


def menu_display():
    print("\nHello! Welcome to the To-Do List App!")


def add_task():
    print("\nYou have chosen to add a task.")
    while True:
            task_added = input("Please enter the task you would like to add. ").strip()
            if len(task_added) > 100:
                print("That is too many characters! Please enter a shorter task. ")

            elif task_added:
                break
            else:
                print("Please enter a non-empty task.")

    if "Default" in task_list:
        task_list.remove("Default")
        task_status.remove(task_status[0])
    task_list.append(task_added)
    task_status.append('Incomplete')
    print('Added task "',task_added, '", marked "Incomplete".')

def del_task():
    print("\nYou have chosen to delete a task.")
    print("Tasks present in list:")
    for task, status in zip(task_list, task_status):    #w3Schools Zip(), used to display the lists in format
        print(task_list.index(task)+1, '.','"',task,'"', 'marked:', '"',status,'"')

    while True:
        try:
            while True:
                task_del = int(input("Please enter the number of the task you would like to delete. "))
                if task_del:
                    break
                else:
                    "Please enter a valid number."
            del_index = task_del - 1
            removed_task = task_list.pop(del_index)
            removed_status = task_status.pop(del_index)
            print('Removed task "', removed_task, '".')
            break

        except ValueError:
            print("Please enter a valid number. ")
        except OverflowError:
            print("That number is too large! Please enter a valid number. ")
        else:
            pass
            
            
    if "Default" in task_list:
        task_list.remove("Default")
        task_status.remove(task_status[0])


def view_tasks():
    print("\nYou have chosen to view your tasks. Here are your tasks:")

    for task, status in zip(task_list, task_status):    #w3Schools Zip(), used to display the lists in format
        print('"',task,'"', 'marked:', '"',status,'"')

def mark_complete():
    print("\nYou have chosen to mark a task as complete.")
    print("Tasks present in list:")
    for task, status in zip(task_list, task_status):    #w3Schools Zip(), used to display the lists in format
        print(task_list.index(task)+1, '.','"',task,'"', 'marked:', '"',status,'"')

    while True:
        try:
            while True:
                task_com = int(input("Please enter the number of the task you would like to mark as complete. "))
                if task_com:
                    break
                else:
                    "Please enter a valid number."
            com_index = task_com - 1
            compd_status = task_status.pop(com_index)
            task_status.insert(com_index, "Completed")
            print('Task "', com_index, '"marked as Completed.')
            break

        except ValueError:
            print("Please enter a valid number. ")
        except OverflowError:
            print("That number is too large! Please enter a valid number. ")
        else:
            pass

menu_display()
while True:
    try:
        print("\nMenu:\n 1. Add a Task\n 2. View Tasks\n 3. Mark a Task as Complete\n 4. Delete a Task\n 5. Quit")
        choice = int(input("\nWhat would you like to do? Please enter the number of your choice. "))
    except ValueError:
        print("Please enter a valid number. ")
    else:
        if choice == 1:
            if len(task_list) < 9223372036854775:        #How would someone get this close to overflow? With a lot of dedication, I guess.
                add_task()
            else:
                print("Somehow, there are too many items in the list.")
        if choice == 2:
            if len(task_list) > 0:
                view_tasks()
            else:
                print("There are no tasks in the list.")
        if choice == 3:
            if len(task_list) > 0:
                mark_complete()
            else:
                print("There are no tasks in the list to mark as complete.")
        if choice == 4:
            if len(task_list) > 1:
                del_task()
            else:
                print("There's only one task left! You can't have an empty list.")
        if choice == 5:
            break

print("Exiting. Thank you for using the To-Do List App!\n ")