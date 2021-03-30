# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and
# settings.
import random
from subroutines.sports import sports


class WordProcessor:
    def __init__(self, word="home", max_tries=5):
        self.actual_word = word.lower()
        self.guessed_word = "_" * len(word)
        self.max_tries = max_tries
        self.tries_counter = 0
        self.can_proceed = True
        print(
            f"The word you are guessing has {len(self.actual_word)} letters. Good luck"
            f"\nYour guessed word:   {self.guessed_word}"
        )

    def find_positions(self, character):
        return [i for i, c in enumerate(self.actual_word) if c == character]

    def register_guess(self, character):
        response = 0
        if character not in self.actual_word:
            self.tries_counter += 1
            print(
                "Sorry, the word does not contain this letter. You have "
                f"only {self.max_tries - self.tries_counter} remaining attempts.\n"
                f"Your guessed word:   {self.guessed_word}"
            )
        elif character in self.guessed_word:
            self.tries_counter += 1
            print(
                "Sorry, you already have guessed this letter. You have "
                f"only {self.max_tries - self.tries_counter} remaining attempts.\n"
                f"Your guessed word:   {self.guessed_word}"
            )
        else:
            char_positions = self.find_positions(character=character)
            guessed_list = list(self.guessed_word)
            for pos in char_positions:
                guessed_list[pos] = list(self.actual_word)[pos]
            self.guessed_word = "".join(guessed_list)
            self.tries_counter += 1
            if self.guessed_word == self.actual_word:
                self.can_proceed = False
                response = 1
                print(
                    "Amazing work! You have correctly guessed the word: "
                    f"{self.actual_word}"
                )
            else:
                print(
                    "Good, you have guessed this letter correctly. You have "
                    f"{self.max_tries - self.tries_counter} remaining attempts.\n"
                    f"Your guessed word:   {self.guessed_word}"
                )
        if self.tries_counter >= self.max_tries:
            self.can_proceed = False
            print(
                "Sorry you have exhausted all your attempts\n"
                f"The word you were given is {self.actual_word}"
            )
        return response

    @staticmethod
    def sanity_check(character):
        if len(character) == 1 and character.isalpha():
            return True

    def attempt_guess(self, character):
        character = character.lower()
        sanity = self.sanity_check(character)
        if sanity:
            score = self.register_guess(character)
        else:
            print(
                "You are only allowed to choose one of the english alphabets. You have "
                f"{self.max_tries - self.tries_counter} remaining attempts.\n"
                f"Your guessed word:   {self.guessed_word}"
            )
            score = 0
        return score

    def iterate(self):
        attempt_scores = []
        while self.can_proceed:
            character = input("Enter your guess letter:  ")
            attempt_scores.append(self.attempt_guess(character=character))
        return attempt_scores


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r_words = random.sample(population=sports, k=5)
    print("You have chosen the sports category")
    for r_word in r_words:
        word_processor = WordProcessor(word=r_word, max_tries=7)
        scores = word_processor.iterate()
        print(scores)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
