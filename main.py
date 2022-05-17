import itertools
import string
import time


def guess_common_words(word):
    with open('words.text', 'r') as words:
        data = words.read().splitlines()
    # print(data)

    for i, match in enumerate(data):
        if match == word:
            return f'The word is: {match} (Attempt #{i})'

    return 0


# Goes through every combination of chars
def brute_force(word, min_length=4, max_length=10, includes_digits=False, includes_symbols=False):
    # Modify this for total symbols
    chars = string.ascii_lowercase

    if includes_digits:
        chars += string.digits

    if includes_symbols:
        chars += string.punctuation

    attempts = 0
    for word_length in range(min_length, max_length):

        for guess in itertools.product(chars, repeat=word_length):
            attempts += 1
            guess = ''.join(guess)

            if guess == word:
                na_attempts = '{:,}'.format(attempts, )
                return f'"{word}" was found in {na_attempts} guesses.'
            # print(guess, attempts)


# Find the word
search_term = input("Which word? >> ").lower()

# Get the current timestamp
start_time = time.time()

common_search = guess_common_words(search_term)
print("Searching...")

if common_search != 0:
    print(common_search)
else:
    request = brute_force(search_term, min_length=3, max_length=10)
    print(request)

# Print the time it took
print(round(time.time() - start_time, 2), 's')
