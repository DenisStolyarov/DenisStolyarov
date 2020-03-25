#Guess the number.
import random
guessTaken = 0
print('What is your name?')
name = input()
number = random.randint(1,20)
print('OK,'+ name + '. I made a number from 1 to 20')
for guessTaken in range(6):
    
    print('Try to guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your nubmer is Little!')

    if guess > number:
        print('Your nubmer is Big!')

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken + 1)
    print('Exellent,' + name + '! You managed for ' + guessTaken + ' attempts.')
    
if guess != number:
    number = str(number)
    print('Sorry,' + name + '. But my number is ' + number)        
