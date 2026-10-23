def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        result = ""

        for letter in secret_word:
                if letter in guesses:
                    result += letter
                else:
                    result += "_"
        print(result)

        if "_" in result:
             return False
        else:
             return True

    return hangman_closure

secret_word = input("Please enter the secret word")
ready_set_play = make_hangman(secret_word)

while not ready_set_play(input("guess a letter: ")):
     pass

print("Yes, you guessed it!!")