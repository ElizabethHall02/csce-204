tasks = [ ]

while True:

    todos = input("Do you wany to (V)iew, (A)dd, (R)emove, or (Q)uit: ").lower().strip()

    if tasks:
          print("Yay! You have nothing todo!")
    elif todos == "q":
            break
    elif todos == "v":
        for task in tasks:
            print(f" -{task}")
    elif todos == "a":
        task = input("Enter todo name: ").lower().strip()
        tasks.append(task)
    elif todos == "r":
        task = input("Enter task: ").lower().strip()
        tasks.remove(task)
    else:
        print(f"Sorry {task} isn't in your list")


    

print("goodbye")
