# Compulsory Task 1

# Defines the function to print all the weekdays
def print_weekdays():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(days)

# This calls the function which then prints out the days
print_weekdays()

# This function will take in a string and break it up and return every second word as hello
def every_second_word(sentence, repeat_word):
    word_list = sentence.split()
    sentence_length = len(word_list)
    for i in range(0, sentence_length):
        if i % 2 != 0:
            word_list[i] = repeat_word
    build_sentence = ''
    for word in word_list:
        build_sentence = build_sentence + word + ' '
    print(build_sentence)

# The user can enter the string they would like to alter
sentence = input('Please enter a sentence you would like to change: ')

# The use can choose which word the would like to change every second word to be. The default word is hello.
while True:
    repeat_word = 'Hello'
    default = input(
        'Would you like to choose a word to change every second word to? (Yes or No -' +
        ' If you select no a default word will be used): ')
    default = default.lower()
    if default == 'yes':
        repeat_word = input('What would you like the word to be: ')
        break
    if default == 'no':
        print('A default word: ' + repeat_word + ' will be used.')
        break
    if default != 'yes' or default != 'no':
        print('You have not selected yes or no.')

# This calls the function and uses the inputs that the user has selected or entered above
every_second_word(sentence, repeat_word)







