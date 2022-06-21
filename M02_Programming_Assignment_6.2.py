# 6.2 Guessing a number
# While loop to compare two values and give response

x = True
guess_me = 7
number = 1

#while guess_me != number
while x is True:

    if number < guess_me:
        print('too low')
        break

    elif number > guess_me:
        print('oops (too high)')
        break

    elif number == guess_me:
        print('found it!')
        break

    else:
        print('something went wrong here')
        break