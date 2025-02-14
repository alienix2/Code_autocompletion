from collections import Counter
from tqdm import tqdm

"""
NOTE: The basic script is way too slow to be used for large datasets and
therefore another library will be used (this should work for small datasets).
"""


def tokenize_file(file_path):
    with open(file_path, "r") as f:
        data = f.read()
    tokens = data.encode("utf-8")
    tokens = list(map(int, tokens))
    return tokens


def get_stats(ids):
    pairs = zip(ids, ids[1:])
    return Counter(pairs)


def merge(ids, pair, idx):
    new_ids = []
    skip = False
    for i, j in zip(ids, ids[1:] + [None]):
        if skip:
            skip = False
            continue
        if (i, j) == pair:
            new_ids.append(idx)
            skip = True
        else:
            new_ids.append(i)
    return new_ids


def get_merges(num_merges, tokens):
    ids = list(tokens)
    merges = {}
    for _ in tqdm(range(num_merges)):
        stats = get_stats(ids)
        best = max(stats, key=stats.get)
        idx = max(set(tokens) | {0}) + 1
        ids = merge(tokens, best, idx)
        merges[best] = idx
    return merges


def get_vocab(merges, max_token):
    vocab = {idx: bytes([idx]) for idx in range(max_token + 1)}
    for (i, j), idx in merges.items():
        vocab[idx] = vocab[i] + vocab[j]
    return vocab


def decode(ids, vocab):
    tokens = b"".join([vocab[i] for i in ids])
    text = tokens.decode("utf-8", errors="replace")
    return text


def encode(text, merges):
    tokens = list(text.encode("utf-8"))
    while len(tokens) >= 2:
        stats = get_stats(tokens)
        best = max(stats, key=stats.get)
        if best not in merges:
            break
        idx = merges[best]
        tokens = merge(tokens, best, idx)
    return tokens


tokens = tokenize_file("processed_datasets/formatted_python_data_be_file.txt")[:1000]
max_token = max(tokens)

merges = get_merges(
    5000,
    tokens,
)
print(decode(encode("hello world", merges), get_vocab(merges, max_token)))
