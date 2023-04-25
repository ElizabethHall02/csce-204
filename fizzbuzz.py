count = 1

while count <= 100: 
    #check if divisible by 3
    #check if divisible by 5
    #check if divisible by 3 and 5
    #otherwise, print count
    
    if count % 3 == 0 and count % 5 == 0:
        print('FIZZBUZZ')
    elif count % 5 == 0:
        print('BUZZ')
    elif count % 3 == 0:
        print('FIZZ')
    else:
        print(count)
    count = count + 1
