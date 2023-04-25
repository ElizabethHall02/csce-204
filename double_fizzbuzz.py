# while loop version
#count = 1
#while count <= 100:
 #   if count % 3 == 0 and count % 5 == 0:
  #      print('FIZZBUZZ')
  #  elif count % 5 == 0:
   #     print('BUZZ')
   # elif count % 3 == 0:
   #     print('FIZZ')
   # else:
    #    print(count)
   # count = count + 1

#print('end while loop')

# for loop version
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FIZZBUZZ')
    elif num % 5 == 0:
        print('BUZZ')
    elif num % 3 == 0:
        print('FIZZ')
    else:
        print(num)

    