task_list=[]
first_task = input('Enter the first task: ')
task_list.append(first_task)
print('Here is the list so far:\n\t{}'.format(task_list))

stop = False
while stop == False:
    print('Here are the options:\n1) Add a new task\n2) Remove a task\n3) Print the list')
    option = input('Select an option: ')

    if(option) == '1':
        new_task = input('Enter the task: ')
        task_list.append(new_task)
    elif (option) == '2':
        old_task = input('Type the task to be removed: ')
        task_list.remove(old_task)
    elif (option) == '3':
        print('Here is the list so far:\n\t{}'.format(task_list))
    else: 
        print('Invalid option. Please try again.')
    yes_no = input('Do you want to quit? y/n: ')
    if yes_no == 'y':
        stop = True
