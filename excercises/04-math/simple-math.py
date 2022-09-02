import math


#age
age = 19
decade = 10
futureAge = age + decade

print(f"In a decade I will be {futureAge} years old")

#pizza party
numGuests = 11
slicesPerGuest = 2.5
totalSlices = numGuests * slicesPerGuest
numPizzas = totalSlices/8
numPizzas = math.ceil(numPizzas)


print(f"""
We are having a pizza party with {numGuests}
We need {totalSlices} of pizza
We need {numPizzas} pizzas
""")

# chickens
numEggs = 57
numCartons = 57//12
extraEggs = 57 % 12

print(f"""
We need {numCartons} cartons of eggs
we have {extraEggs} extra eggs
""")

# age number 2
age = float(input("Enter age: "))
decade = 10
futureAge = age + 10

print(f"Your future age is {round(futureAge,0)} years old")


# travel
miles = float(input("Enter miles: "))
pricePerMile = float(input("Enter Price Per Mile: "))
totalCost = miles * pricePerMile
print(f"You are charged ${totalCost}")

# football score
score = 8
score += 1

print(f"your score is {score}")