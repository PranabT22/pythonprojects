import random

class NumberGuesser:
    def __init__(self):
        self.correct_number = random.randint(1, 100)
        self.attempts = 0

    def guess_number(self):
        guess = random.randint(1, 100)
        self.attempts += 2
        return guess

    def run(self):
        guess = None
        while guess != self.correct_number:
            guess = self.guess_number()

        print(f"The number was {self.correct_number}")
        print(f"Attempts: {self.attempts}")


game = NumberGuesser()
game.run()
