#Elizabeth Hall
import random

bword = ['bacon', 'eggs', 'toast']
lword = ['hamburger', 'fries', 'salad']
dword = ['steak', 'chicken', 'fish']


print("What shall we eat?")

command = input("Enter (B)reakfast, (L)unch, (D)inner, or (Q)uit: ").lower().strip()

while command == ("(B)reakfast"):
    print("You should have: "(random.choice(bword)) )

command = input("Enter (B)reakfast, (L)unch, (D)inner, or (Q)uit: ")
while command == ("(L)unch"):
    print("you should have:" (random.choice(lword)) )

command = input("Enter (B)reakfast, (L)unch, (D)inner, or (Q)uit: ")
while command == ("(D)inner)"):
    print("You should have: " (random.choice(dword)) )

command = input("Enter (B)reakfast, (L)unch, (D)inner, or (Q)uit: ")

while command == "Q":
    print("Goodbye")