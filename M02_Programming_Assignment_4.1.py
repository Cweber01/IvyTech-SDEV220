# 4.1 Rudimentary Guessing Number
# Guessing a secret number between 1 and 10 and receiving feedback based on answer

secret = 7

#guess = 9
guess = 7
#guess = 2

if guess == secret:
    print('just right')
elif guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('What went wrong here??')