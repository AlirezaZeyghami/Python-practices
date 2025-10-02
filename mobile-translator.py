existing_words_number = int(input())

my_translation = {}
for _ in range(existing_words_number):
    main, english, french, german = input().split()
    my_translation[main] = main
    my_translation[english] = main
    my_translation[french] = main
    my_translation[german] = main

sentence = input().split()

final_translation = []

for word in sentence:
    if word in my_translation:
        final_translation.append(my_translation[word])
    else:
        final_translation.append(word)

print(" ".join(final_translation))
