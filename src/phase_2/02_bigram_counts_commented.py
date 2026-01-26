# Bigram model: count next-character transitions and normalize to probabilities.

# Open the text file (read mode).
with open("data/phase_2_data/corpus.txt", "r") as f:
    text = f.read()

# Build the sorted list of unique characters.
chars = sorted(list(set(text)))

# Build the character -> number dictionary.
stoi = {}
index = 0
for ch in chars:
    stoi[ch] = index
    index += 1

# Build the number -> character dictionary.
itos = {}
index = 0
for ch in chars:
    itos[index] = ch
    index += 1

# Encode the full text into a list of numbers.
encoded = []
for ch in text:
    encoded.append(stoi[ch])

# Count how many unique characters we have.
vocab_size = len(chars)

# Create a 2D table (rows = current char, columns = next char).
# Each cell will store a count.
counts = []
for _ in range(vocab_size):
    row = [0] * vocab_size
    counts.append(row)

# Fill counts using the standard current -> next pattern.
for i in range(len(encoded) - 1):
    current_id = encoded[i]
    next_id = encoded[i + 1]
    counts[current_id][next_id] += 1

# Convert counts into probabilities (row by row).
probs = []
for row in counts:
    row_total = sum(row)
    if row_total == 0:
        probs.append(row)
    else:
        probs_row = []
        for c in row:
            probs_row.append(c / row_total)
        probs.append(probs_row)

#goal pick a next character based on the probabilit row.
#if the probilities for a row are: 
# [0.1, 0.7, 0.2]
#then index 1 should be picked most often 

import random

start_id = encoded[0]
generated_ids = [start_id]

for _ in range(100):
    current_id = generated_ids[-1]
    prob_row = probs[current_id]
    next_id = random.choices(
        population=list(range(vocab_size)),
        weights=prob_row,
        k=1
    )[0]
    generated_ids.append(next_id)

generated_text = ""
for idx in generated_ids:
    generated_text += itos[idx]

print(generated_text)
