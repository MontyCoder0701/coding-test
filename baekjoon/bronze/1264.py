vowel = ["a", "e", "i", "o", "u"]

while True:
    count = 0
    sentence = input()

    if sentence == "#":
        break

    for letter in sentence:
        if letter.lower() in vowel:
            count += 1
    print(count)
