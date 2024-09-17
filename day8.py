def reverse(str):
    words = str.split()
    words.reverse()
    reversed_sentence = ' '.join(words)
    return reversed_sentence

str = "the sky is blue"
print(reverse(str))