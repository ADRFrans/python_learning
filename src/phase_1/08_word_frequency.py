from src.phase_1.utils import read_from_file

# use the read_from_file function to read the contents of 'data/text.txt'
# then create a variable file to hold the contents
file = read_from_file('data/text.txt')

# empty list to hold words from file
str_list = []

# if statment to make strings lowercase and replace punctuation with spaces
if file is not None:
    file = file.lower() \
        .replace('.', ' ') \
        .replace(',', ' ') \
        .replace('?', ' ') \
        .replace('!', ' ') \
        .replace('-', ' ') \

    #split the files at the spaces and add them to the list.
    for word in file.split():
        str_list.append(word)

#take a list and each value in the list build a dictionary key value pair
def build_dictionary(list_of_words):
    #empty dictionary to hold words and their counts
    word_dict = {}
    #iterate through list of words
    for word in list_of_words:
        #if word is already a key, increment its value by 1 else add it as a new key with value of 1
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

print(build_dictionary(str_list))
