"""
Word Occurrences
Estimate: 30 minutes
Actual:   11 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
word_to_count = dict(sorted(word_to_count.items()))
max_word_length = max(len(key) for key in word_to_count)
for key in word_to_count:
    print(f"{key:{max_word_length}} : {word_to_count[key]}")
