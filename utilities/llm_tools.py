import random

# Utility helpers for a char-level bigram model.
# These functions split the workflow into small steps: read text, map characters to
# integer identifiers (ids), build a bigram table, normalize into probabilities,
# then sample new text.

def load_text(path):
    # Read the entire file as a single string so each character is kept in order.
    # This is important because bigrams are based on adjacent character pairs.
    with open(path, 'r') as f:
        return f.read()

def build_vocab(text):
    # Sorted unique characters define the vocabulary (the model's "alphabet").
    # Sorting makes the mapping deterministic so integer identifiers (ids) are stable.
    chars = sorted(list(set(text)))
    stoi = {}
    itos = {}
    for i, ch in enumerate(chars):
        # stoi means "string to index" (character -> id).
        # itos means "index to string" (id -> character).
        # Using both directions lets us convert back and forth easily.
        stoi[ch] = i
        itos[i] = ch
    return chars, stoi, itos

def encode(text, stoi):
    # Convert each character to its integer identifier (id).
    # The output keeps the same length and order as the original text.
    return [stoi[ch] for ch in text]

def decode(ids, itos):
    # Convert a list of integer identifiers (ids) back into a string.
    # This reverses encode() so you can inspect generated output.
    return ''.join(itos[i] for i in ids)

def build_counts(encoded, vocab_size):
    # 2D matrix where counts[i][j] = how often id i is followed by id j.
    # Each row i represents the "current character"; each column j is the next one.
    counts = [[0] * vocab_size for _ in range(vocab_size)]
    for cur_id, next_id in zip(encoded, encoded[1:]):
        # Walk adjacent pairs (current, next) and increment that bigram count.
        counts[cur_id][next_id] += 1
    return counts

def counts_to_probs(counts):
    # Normalize each row to turn counts into probabilities.
    # Each row then sums to 1.0 (unless the row has no counts at all).
    probs = []
    for row in counts:
        row_total = sum(row)
        if row_total == 0:
            # Keep all zeros if a character never appears as a current char.
            # This avoids division by zero and preserves row length.
            probs.append(row)
            continue
        # Divide each count by the row total to get a probability.
        probs.append([c / row_total for c in row])
    return probs

def sample_next(prob_row, rng=None):
    # Manual weighted sampling using cumulative probability.
    # We draw a random number in [0, 1), then find where it falls in the CDF.
    if rng is None:
        rng = random
    r = rng.random()
    cumulative = 0.0
    for i, p in enumerate(prob_row):
        # Grow the cumulative sum; the first index that passes r is selected.
        cumulative += p
        if r <= cumulative:
            return i
    # Fallback for tiny floating-point gaps (e.g., sum slightly under 1.0).
    return len(prob_row) - 1

def generate_text(probs, itos, start_id, length, rng=None):
    # Repeatedly sample next characters to build a sequence.
    # This is the "inference loop" for a bigram model.
    if rng is None:
        rng = random
    ids = [start_id]
    for _ in range(length):
        # Look up the probability row for the current id, then sample a next id.
        current_id = ids[-1]
        next_id = sample_next(probs[current_id], rng=rng)
        ids.append(next_id)
    # Convert ids back into characters for readability.
    return decode(ids, itos)
