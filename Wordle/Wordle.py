import random

class Wordle_Round:
    def __init__(self):
        self.guesses = []
        self.answer = self.rand_word()

    def __repr__(self):
        return str(self.guesses[-1] == self.answer)

    def wordle(self, guess, answer):
        guess = guess.lower()
        answer = answer.lower()
        result = ['w'] * 5

        answer_letters = list(answer)

        # handle greens
        for i in range(5):
            if guess[i] == answer[i]:
                result[i] = 'g'
                answer_letters[i] = None  # remove matched letter

        # handle yellows
        for i in range(5):
            if result[i] == 'w' and guess[i] in answer_letters:
                result[i] = 'y'
                answer_letters[answer_letters.index(guess[i])] = None  # mark that letter as used

        return ''.join(result)

    def rand_word(self):
        word_bank = ['horse', 'words']
        rand_word = random.choice(word_bank)
        return rand_word

    def is_end_round(self, guess):
        guess = guess.lower()
        self.guesses.append(guess)

        guessed_correctly = guess == self.answer
        too_many_guesses = len(self.guesses) >= 2
        return too_many_guesses or guessed_correctly

class Wordle:
    def __init__(self):
        self.guss_num = 0
        self.game_history = [] # array of wins and losses
        self.round = Wordle_Round()

    def new_guess(self, guess):
        self.round.guess_word(guess)
        return guess

def main():
    wordle = Wordle_Round()

    print('start round')
    while True:
        guess = input()
        if wordle.is_end_round(guess):
            print('round finished')
            break

if __name__ == '__main__':
    main()