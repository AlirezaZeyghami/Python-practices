my_text = input().strip()

sentences = my_text.split(".")

word_index = 1

keywords = []

for sentence in sentences:
    sentence = sentence.strip()

    if not sentence:
        continue

    words = sentence.split()

    for i, raw_word in enumerate(words):
        word = raw_word.strip(",.").strip()

        if word == "":
            word_index += 1
            continue

        if (i != 0) and word[0].isalpha() and word[0].isupper() and (not word.isdigit()):
            keywords.append((word, word_index))

        word_index += 1

if not keywords:
    print("None")
else:
    for word, index in keywords:
        print(f"{index}:{word}")
