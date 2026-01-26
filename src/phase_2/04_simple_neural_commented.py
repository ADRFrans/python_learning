import math
import os
import random
import sys

# Add the repo root to sys.path so utilities can be imported from any run location.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Import reusable helpers for loading text, vocab, encoding, and sampling.
from utilities.llm_tools import (
    load_text,
    build_vocab,
    encode,
    decode,
    sample_next,
)

# Lesson 4: Simple neural bigram model (pure Python).
# We learn a weight row for each current character to predict the next character.

# 1) Load text and build vocabulary.
text = load_text("../../data/phase_2_data/corpus.txt")
chars, stoi, itos = build_vocab(text)
encoded = encode(text, stoi)

# How many unique characters exist in the corpus.
vocab_size = len(chars)

# 2) Initialize trainable weights with small random values.
# weights[current_id][next_id] is the logit score for predicting next_id.
random.seed(0)
weights = []
for _ in range(vocab_size):
    row = []
    for _ in range(vocab_size):
        row.append((random.random() - 0.5) * 0.01)
    weights.append(row)

# 3) Softmax converts a row of logits into probabilities that sum to 1.
def softmax(logits):
    max_logit = max(logits)
    exp_vals = [math.exp(x - max_logit) for x in logits]
    total = sum(exp_vals)
    return [v / total for v in exp_vals]

# 4) Train the model with a simple gradient update.
learning_rate = 0.5
steps = 2000

for step in range(steps):
    # Pick a random adjacent pair (current -> next) from the text.
    i = random.randint(0, len(encoded) - 2)
    current_id = encoded[i]
    target_id = encoded[i + 1]

    # Forward pass: convert logits to probabilities for this current_id.
    logits = weights[current_id]
    probs = softmax(logits)

    # Loss: negative log likelihood of the correct next character.
    epsilon = 1e-12
    loss = -math.log(probs[target_id] + epsilon)

    # Gradient for softmax + cross-entropy: probs minus 1 at the target.
    gradients = probs[:]
    gradients[target_id] -= 1.0

    # Update only the row for current_id (one-hot input assumption).
    for j in range(vocab_size):
        weights[current_id][j] -= learning_rate * gradients[j]

    if (step + 1) % 400 == 0:
        print(f"step {step + 1}, loss {loss:.4f}")

# 5) Generate text from the trained weights.
random.seed(1)
start_id = encoded[0]
ids = [start_id]

for _ in range(200):
    current_id = ids[-1]
    probs = softmax(weights[current_id])
    next_id = sample_next(probs, rng=random)
    ids.append(next_id)

print("\nGenerated text:\n")
print(decode(ids, itos))
