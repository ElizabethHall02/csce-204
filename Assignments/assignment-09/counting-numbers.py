#Elizabeth Hall

print("Lets count!")
n = 0

start = int(input("Enter Starting Number: ").lower().strip())
x = int(start)

end = int(input("Enter Ending Number: ").lower().strip())
y= int(end)

for i in range(x,y):
    print(i+1, end=' ')

print(f"There are : {y - x} numbers")




