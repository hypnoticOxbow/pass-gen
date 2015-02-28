import json
import random



def load_words():
    with open("./words_dictionary.json", "r") as english_dictionary:
        valid_words = json.load(english_dictionary)
        return valid_words

    return valid_words


transition = {
    "a": "@4",
    "b": "8",
    "o": "0",
    "e": "3",
    "u": "0",
    "l": "1",
    "i": "1",
    "t": "7"
}


def addRandomness(word):
    change_count = 3
    for i in range(len(word)):
        if ((word[i] in "aeioulbt") and random.choice((True, False, False))):
            word = word[:i] + random.choice(transition.get(
                word[i])) + word[(i + 1):]
            change_count += -1
            if change_count == 0:
                break
    return word


if __name__ == '__main__':
    english_words = load_words()
    base = ""
    for i in range(3):
        base += (random.choice(list(english_words.keys()))).capitalize()
    passwd = addRandomness(base)
    print(passwd)
