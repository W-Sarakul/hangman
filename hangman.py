# Write your code here
import random
word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(word_list)
print('H A N G M A N')
print()

choice = input('Type "play" to play the game, "exit" to quit:')

if choice == 'play':

    tries = 8
    ans = list('-' * len(chosen_word))
    guess_set = set()
    while tries > 0:
        if ''.join(ans) == chosen_word:
            break
        print()
        print(''.join(ans))
        #print('Input a letter:')
        print('Input a letter:', end="")
        
        guess = input()
        while len(guess) != 1 or guess.isupper() or not guess.isalpha():
            if len(guess) != 1:
                print('You should input a single letter')
                print()
                print(''.join(ans))
                #print('Input a letter:')
                print('Input a letter:', end="")
                guess = input()
                
            elif guess.isupper() or not guess.isalpha():
                print('Please enter a lowercase English letter')
                print()
                print(''.join(ans))
                #print('Input a letter:')
                print('Input a letter:', end="")
                guess = input()
                
        if guess in chosen_word and guess not in ans:
            for i in range(len(chosen_word)):
                if guess == chosen_word[i]:
                    ans[i] = chosen_word[i]
        elif guess in guess_set:
            print('You\'ve already guessed this letter')
            
        else:
            tries -= 1
            print('That letter doesn\'t appear in the word')
        guess_set.add(guess)

            
    if ''.join(ans) == chosen_word:
        print(''.join(ans))
        print('You guessed the word! {}'.format(chosen_word))
        print('You survived!')
    else:
        print('You lost!')
elif choice == 'exit':
    pass
