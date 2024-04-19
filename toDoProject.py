task_list = ['Default']
task_status = ['Incomplete']


def menu_display():
    print("Hello! Welcome to the To-Do List App!")
    print("Menu:\n 1. Add a Task\n 2. View Tasks\n 3. Mark a Task as Complete\n 4. Delete a Task\n 5. Quit")

def add_task():
    print("You have chosen to add a task.")
    task_added = input("Please enter the task you would like to add. ")
    task_list.append(task_added)
    task_status.append('Incomplete')
    print('Added task "',task_added, '", marked "Incomplete".')

menu_display()
while True:
    try:
        choice = int(input("What would you like to do? Please enter the number of your choice. "))
    except ValueError:
        print("Please enter a valid number. ")
    else:
        if choice == 1:
            add_task()
        if choice == 5:
            break

print("Exiting. Thank you for using the To-Do List App! ")