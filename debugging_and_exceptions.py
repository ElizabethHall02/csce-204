# Use what you have learned from the lecture on 11 Apr
# to handle exceptions or sanitize inputs
loop = 'y'
while loop == 'y':
    try:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
        print('The quotient is: {}'.format(num1/num2))
    except ValueError:
        print('That is not a valid number')
    except ZeroDivisionError:
        print('Second number cannot be zero')
    loop = input('Would you like to calculate another? (y/n) ')

# ### INPUTS ###
# Format: first, second
# 0, 4
# 4, 0 (this will cause an exception)
# -1, 4 (negative input is valid)
# 4, -1
# -2, -8 (valid)
# -8, -2
# 0.5, 4.2 (this will cause an exception)
# 4.2, 0.5
# 0.0, 4.0
# 4.0, 0.0 (exception, likely already handled)
# -1.0, 4.0 (valid)
# 4.0, -1.0
# 1.0, G (letters are not valid inputs)
# G, 1.0