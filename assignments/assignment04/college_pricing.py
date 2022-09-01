# Author: Elizabeth Hall


textbook = 64.99 * .07
dorm_roomPerWeek = 184.99 
breakfast = 3.85
lunch = 8.95
dinner = 12.79
days = float(input("How many days are you budgeting for: "))
books = float(input("How many books do you need: "))
totalExpense = ((lunch + dinner + breakfast) * days + (textbook * books) + dorm_roomPerWeek/7 * days) 
totalExpense = round(totalExpense + totalExpense * .07)
print(f"""
Total Expenses: ${totalExpense}
""")