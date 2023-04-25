import random

flashcards = {
   
}


print("Let's build some flashcards!")
# ask the user for terms and definitions in a loop, Loop starts here
stop1 = False
while stop1 == False:
    u_term = input("Enter a term: ")
    u_def = input("Enter a definition: ")
    # allow them to stop entering terms and definitions
    # store those in the dictionary like this flashcards[key]=value (flashcards[term]=def)
    flashcards[u_term] = u_def
    print('Flashcard saved!') #optional
    # loop (part 1) until the user quits, Loop ends here
    yes_no = input('Do you want to quit? y/n: ')
    if yes_no == 'y':
        stop1 = True

#part 2
print("It's time for a quiz! I'll show you a term and you think about the definition.")
stop2 = False
while stop2 == False: # randomly select a card (term)
    rand_term = random.choice( list( flashcards.keys() ) )
    # show the term (print)
    print("Here is the term: {}".format(rand_term) ) 
    # show "ready?" and then wait for the Enter key
    input("Ready? (Press enter when ready)" )
    # show the definition (print)
    print("Here is the definition: {}".format( flashcards[rand_term] ) )
    # put that in a loop until the user wants to quit
    yes_no = input('Do you want to quit? y/n: ')
    if yes_no == 'y':
        stop2 = True