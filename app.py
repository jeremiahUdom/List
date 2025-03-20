from List import List

list_name = ''
action = input('Welcome to list. Do you want to create a new list or continue with an exiting one(Y/N): ')

if action.lower() == 'y':
    list_name = input('What would you like to name the list: ')
    open(f'{list_name}.txt', 'w')
elif action.lower() == 'n':
    list_name = input('What is the name of the list you want to continue with: ')
else:
    print('Invalid input')

list = List(list_name)
    
list_action = input("What would you like to do(add, remove, or load): ")

if list_action.lower() == "add":
    title = input("Enter title: ")
    list.add_list(title)
elif list_action.lower() == "remove":
    list_id = int(input("Enter the id of the list you want to remove: "))
    list.remove_list(list_id)
elif list_action.lower() == "load":
    lists = list.load_lists_from_file()
    print(lists)
else:
    print("Invalid action. Please try again")