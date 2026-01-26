with open("data/phase_2_data/corpus.txt", "r") as f:
    text = f.read()

chars = sorted(list(set(text)))

vocab_size = len(chars)

stoi = {}
index = 0
for ch in chars:
    stoi[ch] = index
    index += 1

stoi = {ch: i for i, ch in enumerate(chars)}

itos = {}
index = 0
for ch in chars:
    itos[index] = ch
    index += 1

itos = {i: ch for i, ch in enumerate(chars)}

encoded = []
for ch in text:
    encoded.append(stoi[ch])

decoded_chars = []
for num in encoded:
    decoded_chars.append(itos[num])

decoded_text = "".join(decoded_chars)

print(encoded)

print(decoded_text)

