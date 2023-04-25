import random

lowers = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
uppers = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
nums = ['0', '1', '2','3','4','5','6','7','8','9'] 
specials = ['*', '&', '%','^','&','!','@','#','$'] 
all_chars = lowers + uppers + nums + specials

stop1 = False
while stop1 == False:
    length = int(input("How many characters?: "))
    password = ''
     
    rand_char = random.choice(all_chars)  
    password += (rand_char)
    password = ''.join(random.choices(all_chars, k=length))
    print (password) 
            
                
    yes_no = input("Do you want to print another password? y/n ")
    if yes_no == 'n':
         stop1 = True
         print("Have a nice day!")
                


        
             


        