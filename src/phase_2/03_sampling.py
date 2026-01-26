
import os
import random

import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utilities.llm_tools import (
    load_text,
    build_vocab,
    encode,
    build_counts,
    counts_to_probs,
    generate_text,
)

text = load_text("../../data/phase_2_data/corpus.txt")

chars, stoi, itos = build_vocab(text)

encoded = encode(text, stoi)

vocab_size = len(chars)

counts = build_counts(encoded, vocab_size)

probs = counts_to_probs(counts)

random.seed(0)

start_id = encoded[0]

output = generate_text(probs, itos, start_id, length=200)

print(output)

