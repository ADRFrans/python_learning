# Used to build safe file paths.
import os
import random
# Used to modify the system path to include the repo root.
import sys

# Add the repo root to sys.path so utilities can be imported
# regardless of where you run the script from.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Import reusable helpers that handle vocab, encoding, and sampling.
from utilities.llm_tools import (
    load_text,
    build_vocab,
    encode,
    build_counts,
    counts_to_probs,
    generate_text,
)

# 1) Load the text corpus.
text = load_text("../../data/phase_2_data/corpus.txt")

# 2) Build vocabulary mappings.
chars, stoi, itos = build_vocab(text)

# 3) Encode the text into integer identifiers (ids)
encoded = encode(text, stoi)

# How many unique characters exist in the corpus (vocabulary size).
vocab_size = len(chars)

# 4) Create the bigram count matrix: counts of (current char -> next char).
counts = build_counts(encoded, vocab_size)

# 5) Convert counts to probabilities so each row sums to ~1.0.
probs = counts_to_probs(counts)

# Fix the random seed so you get the same output while learning. 
random.seed(0)

# Use the first character from the corpus as the starting point.
start_id = encoded[0]

# 6) Generate text by repeatedly sampling the next character.
output = generate_text(probs, itos, start_id, length=200)

# Show the sampled output.
print(output)
