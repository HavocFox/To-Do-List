# -----------------------------------------------------------------------------------
# VARIABLES
# -----------------------------------------------------------------------------------

task_list = []
task_status = []

# -----------------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------------

def welc_display(): #Displays welcome message
    print("\nHello! Welcome to the To-Do List App!")


def add_task():        # Add a task
    print("\nYou have chosen to add a task.")
    while True:
            task_added = input("Please enter the task you would like to add. ").strip() # Remove unnecessay whitespace.
            if len(task_added) > 250:                                                   # Preventing awful formatting with long task names.
                print("That is too many characters! Please enter a shorter task. ")

            elif task_added:                                                            # Add the task if it isn't comprised only of whitespace.
                break
            else:
                print("Please enter a non-empty task.")

    task_list.append(task_added)                                                        # Add the task to the task list
    task_status.append('Incomplete')                                                    # Add the task's status to the status list
    print('Added task "',task_added, '", marked "Incomplete".')                         # Print task and completion status

def del_task():        # Delete a task
    print("\nYou have chosen to delete a task.")
    print("Tasks present in list:")
    for task, status in zip(task_list, task_status):                                            # w3Schools Zip(), used to display the lists in format
        print(task_list.index(task)+1, '.','"',task,'"', 'marked:', '"',status,'"')             # Print task and completion status

    while True:
        try:
            while True:
                task_del = int(input("Please enter the number of the task you would like to delete. "))
                if task_del <= len(task_list):                                                  # Prevent access of indexes outside the list size
                    break
                else:
                    print("That number isn't in the list.")
            del_index = task_del - 1                                                            # Separate value to hold real index (in Zero Base form)
            removed_task = task_list.pop(del_index)                                             # Remove task at true index
            removed_status = task_status.pop(del_index)                                         # Remove completion status at same index as removed task
            print('Removed task "', removed_task, '".')                                         # Print what task was removed
            break

        except ValueError:                                                    # Exception if incorrect value or string is entered
            print("Please enter a valid number. ")
        except OverflowError:                                                 # Exception if too high of a value is entered
            print("That number is too large! Please enter a valid number. ")
        else:
            pass

def view_tasks():      # View tasks
    print("\nYou have chosen to view your tasks. Here are your tasks:")

    for task, status in zip(task_list, task_status):                                                # w3Schools Zip(), used to display the lists in format
        print('"',task,'"', 'marked:', '"',status,'"')                                              # Print all tasks and completion status

def mark_complete():
    print("\nYou have chosen to mark a task as complete.")
    print("Tasks present in list:")
    for task, status in zip(task_list, task_status):                                                # w3Schools Zip(), used to display the lists in format
        print(task_list.index(task)+1, '.','"',task,'"', 'marked:', '"',status,'"')

    while True:
        try:
            while True:
                task_com = int(input("Please enter the number of the task you would like to mark as complete. "))
                if task_com:                                                                        #Continue if it isn't comprised only of whitespace.
                    if task_com <= len(task_list):                                                  # Prevent access of indexes outside the list size
                        break
                    else:
                        print("That number isn't in the list.")
                else:
                    "Please enter a valid number."
            com_index = task_com - 1                                                            # Separate value to hold real index (in Zero Base form)
            compd_status = task_status.pop(com_index)                                           # Remove task completion status at true index in status list
            task_status.insert(com_index, "Complete")                                           # Insert "Complete back at that same index"
            print('Task "', com_index+1, '" marked as Completed.')                              # Print what task was completed
            break

        except ValueError:                                                    # Exception if incorrect value or string is entered
            print("Please enter a valid number. ")
        except OverflowError:                                                 # Exception if too high of a value is entered
            print("That number is too large! Please enter a valid number. ")
        else:
            pass


# -----------------------------------------------------------------------------------
# MAIN CODE
# -----------------------------------------------------------------------------------

welc_display()      #Display the welcome message.

while True:
    try:
        print("\nMenu:\n 1. Add a Task\n 2. View Tasks\n 3. Mark a Task as Complete\n 4. Delete a Task\n 5. Quit")
        choice = int(input("\nWhat would you like to do? Please enter the number of your choice. "))                # Prompt for user input (a choice from the list).

    except ValueError:                                                                                              # Handle incorrect input, prompt for correct input
        print("Please enter a valid number. ")
    else:
        if choice == 1:
            if len(task_list) < 9223372036854775:                                                                   # How would someone get this close to overflow? With a lot of dedication, I guess.
                add_task()
            else:
                print("Somehow, there are too many items in the list.")
        if choice == 2:
            if len(task_list) > 0:                                                                                  # Don't let user view an empty list
                view_tasks()
            else:
                print("There are no tasks in the list.")
        if choice == 3:
            if len(task_list) > 0:                                                                                  # Don't let user mark a task completed an empty list
                mark_complete()
            else:
                print("There are no tasks in the list to mark as complete.")
        if choice == 4:
            if len(task_list) > 0:                                                                                  # Don't let user delete from an empty list
                del_task()
            else:
                print("You can't delete tasks from an empty list.")
        if choice == 5:                                                                                             # Quit application
            break

print("Exiting. Thank you for using the To-Do List App!\n ")                                                        # Exit app