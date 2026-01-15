with open("data/phase_2_data/corpus.txt", "r") as f:
    text = f.read()

# set(text) gives unique characters
# list() turns the set into a list
# sorted() keeps the list in a stable order
chars = sorted(list(set(text)))

vocab_size = len(chars)

# If text contains letters, spaces, and punctuation, those are all part of the vocabulary.

# print(vocab_size, chars)

################    STOI    ####################
# Now we numberize the characters.
# We assign each character its position in the list.
# Example: chars = ['a'] -> enumerate(chars) gives (0, 'a').
# stoi means string to index (character -> number).

# Long form: character -> number
stoi = {}
index = 0 
for ch in chars: 
    stoi[ch] = index 
    index += 1

# Short form: character -> number (same result)
stoi = {ch: i for i, ch in enumerate(chars)}

#print(stoi)

#############   ITOS    ####################
# itos = index to string (number -> character).
# If stoi lets you go from 'a' -> 0, then itos lets you go from 0 -> 'a'.
# For each character in chars, store it at its number index.
# Example: itos[0] -> 'a', itos[1] -> 'b'.

# Long form: number -> character
itos = {}
index = 0
for ch in chars:
    itos[index] = ch
    index += 1

# Short form: number -> character (same result)
itos = {i: ch for i, ch in enumerate(chars)}

#print(itos)

######################      Encoded         ############
# Walk through each character in the full text.
# For each character, look up its number in stoi and store it in a list.

encoded = []
for ch in text:
    encoded.append(stoi[ch])

# print(encoded[:10]) # just showing the first 10 numbers

#################       DECODED     ################
# Convert the list of numbers back into characters using itos.
# Go through each number in encoded, look up the character in itos,
# and build a new string.

# long form 

decoded_chars = []
for num in encoded:
    decoded_chars.append(itos[num])

decoded_text = "".join(decoded_chars)

# Numbers representing the text
print(encoded)
# The decoded text
print(decoded_text)
