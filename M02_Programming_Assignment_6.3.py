# 6.3 Using For Loops
# A for loop to iterate until a number is found

guess_me = 5

for number in range(10):

    if number < guess_me:
        print('too low!')

    elif number == guess_me:
        print('found it!')
        break

    elif number > guess_me:
        print('oops')
        break

    else:
        print('something seems fishy here...')