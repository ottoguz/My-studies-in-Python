#TYPE A SENTENCE AND I WILL SHOE YOU THE LAST OCCURRENCE OF THE LETTER 'A'

sentence = str(input('Type a sentence:')).upper().strip()
print('Number of occurrences of the letter "a": {}' .format(sentence.count('A')))
print('The first occurrence was in the position: {}' .format(sentence.find('A') + 1))
print('The last occurrence was in the position:  {}' .format(sentence.rfind('A') + 1))



