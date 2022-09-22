#! /bin/python3

# creator : Dumisani Mbonani (eagle)

from random import choice as gen
from random import randint as randnum


counter = 0
wins = 0

cmd = ''

# replace the randomly selected position with under score _ then  return it
def change_word_func(word, get_index):

    guess_letter = ''
    new_word = ''

    for index in range(len(word)):

        if index == get_index:
            new_word = new_word + '_'
            guess_letter = word[index]
        else:
            new_word = new_word + word[index]


    # print(guess_letter, new_word)

    return [guess_letter, new_word]


# get randonm word with with the correct letter
def words():

    name = './text/names.txt'

    with open(name,'r') as fp:

        words = fp.read()

    words = words.split('\n')
    words = tuple(words)

    # Algo for randomly selecting a hidden letter

    word_get = gen(words)
    get_index = randnum(0,len(word_get) - 1)
    guess_letter = ''
    new_word = ''

    req_change = change_word_func(word_get, get_index)

    for i in range(len(word_get)):

        if i == get_index:

            guess_letter = req_change[0]

            new_word = req_change[1]

    return {'answer': guess_letter, 'correct_word': word_get, 'guess': new_word}

# Run game
while True:

    play = words()

    print(f"guess the missing letter: {play['guess']}")

    cmd = input('> ')

    if cmd == play['answer']:

        wins = wins + 1

        if not wins == 5:

           print(f"correct the missing letter was -> {play['answer']} : {play['correct_word']}")
        else:

            print("You win the game good for you")

            break

    else:

        if counter == 5:

            print('You lose')

            break

        print(f'Wrong try another one: {counter+1}')
        counter = counter + 1


