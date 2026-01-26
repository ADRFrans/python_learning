import math
import os
import random
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utilities.llm_tools import (
    load_text,
    build_vocab,
    encode,
    decode,
    sample_next,
)

text = load_text("../../data/phase_2_data/corpus.txt")
chars, stoi, itos = build_vocab(text)
encoded = encode(text, stoi)

vocab_size = len(chars)

random.seed(0)
weights = []
for _ in range(vocab_size):
    row = []
    for _ in range(vocab_size):
        row.append((random.random() - 0.5) * 0.01)
    weights.append(row)


def softmax(logits):
    max_logit = max(logits)
    exp_vals = [math.exp(x - max_logit) for x in logits]
    total = sum(exp_vals)
    return [v / total for v in exp_vals]


learning_rate = 0.5
steps = 2000

for step in range(steps):
    i = random.randint(0, len(encoded) - 2)
    current_id = encoded[i]
    target_id = encoded[i + 1]

    logits = weights[current_id]
    probs = softmax(logits)

    epsilon = 1e-12
    loss = -math.log(probs[target_id] + epsilon)

    gradients = probs[:]
    gradients[target_id] -= 1.0

    for j in range(vocab_size):
        weights[current_id][j] -= learning_rate * gradients[j]

    if (step + 1) % 400 == 0:
        print(f"step {step + 1}, loss {loss:.4f}")


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
