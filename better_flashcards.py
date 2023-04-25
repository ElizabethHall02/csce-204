import random

def build_deck():
    flashcards = {}
    print("Let's build some flashcards!")
    subject = input('What is the name of the subject? ')
    stop1 = False
    while stop1 == False:
        u_term = input("Enter a term: ")
        u_def = input("Enter the definition")
        flashcards[u_term] = u_def
        print("Flashcard saved!")
        yes_no = input('Do you want to quit? y/n: ')
        if yes_no == 'y':
            stop1 = True
            # file_name = [subject].txt
            file_name = '{}.txt'.format(subject)
            # write the dictionary to a file (save the deck)
            with open( file_name, 'w' ) as test_file:
                test_file.write( str( flashcards ) )

def quiz_time():
    subject = input('What is the name of the subject? ')
    file_name = '{}.txt'.format(subject)
    with open( file_name, 'r' ) as test_file:
        quiz_dict = eval( test_file.read() )
    print("Now it's time for a quiz! I will display the term, you quote the definition")
    stop2 = False
    while stop2 == False:
        rand_terms = random.choice( list( quiz_dict.keys() ) )
        print("Here is the term: {}".format(rand_term) )
        input("Ready? (Press enter when you are ready) ")
        print("Here is the definition: {}".format( quiz_dict[rand_term] ) )
        yes_no = input('Do you want to quit? y/n: ')
        if yes_no == 'y':
            stop2 = True

print('Welcome to the flashcards app!')
# TODO: begin the loop
stop3 = False
while stop3 == False:
    print('Here are your options:')
    print('\t1) Build a new deck of flashcards\n\t2) Quiz from a saved deck\n\t3) Quit')
    choice = input('Enter your choice: ')
    if choice == '1':
        build_deck()
    elif choice == '2':
        quiz_time()
    elif choice == '3':
        print('Have a nice day!')
        stop3 = True

