import math 

def add(first,second):
    return first + second
def subtract(first,second):
    return first - second  
def multiply(first,second):
     return first * second 
def divide(first,second):
     return first / second 
def modulus(first,second):
     if not isinstance(first, int):
        first = int(first)
        print("Converting first number to integer")
     if not isinstance(second, int):
        second = int(second)
        print("Converting second numnber to integer")
     return first % second 
def root(first,second):
     return second**(1/first)
def lcm(first,second): 
    if not isinstance(first,int):
        first = int(first)
        print("Converting first number to integer")
    if not isinstance(second,int):
        second = int(second)
        print("Converting second number to integer")
    gcd = math.gcd(first,second)
    lcm = abs(first*second) // gcd
    return lcm
def pythagorean(first,second):
    c = math.sqrt(first**2 + second**2)
    return c
     
stop1 = False  
while stop1 == False:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Select which operation you would like to perform: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Root")
    print("7. LCM")
    print("8. Pythagorean")
    
    choice = int(input("Enter choice: "))
    
           
    if choice == 1:
        print(add(num1,num2))
    elif choice == 2:
        print(subtract(num1,num2))
        print(subtract(num2,num1))
    elif choice == 3:
        print(multiply(num1,num2))
    elif choice == 4:
        print(divide(num1,num2))
        print(divide(num2,num1))
    elif choice == 5:
        print("{} % {} = {}".format(first, second, modulus(first,second)))
    elif choice == 6:
        print(root(num1,num2))
    elif choice == 7:
        print(lcm(num1,num2)) 
    elif choice == 8:
        print(pythagorean(num1,num2))
    yes_no = input('Do you want to quit? y/n: ')
    if yes_no == 'y':
        stop1 = True   
        print("Have a nice day!")
    
         