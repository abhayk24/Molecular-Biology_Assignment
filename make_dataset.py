"""
make_dataset.py  -  creates promoter_dataset.csv

Label 1 (promoter): -35 box (TTGACA) + spacer of 16-18 bases + -10 box (TATAAT).
Label 0 (non-promoter) has THREE kinds, so the task is not trivial:
    50%  purely random DNA
    25%  decoy: only ONE box present (either -35 or -10)
    25%  decoy: BOTH boxes present but with WRONG spacing (4-10 or 26-35 bases)
Each motif base is mutated with probability 10% (biological noise).
A model that only counts motifs (k-mers) cannot separate decoys from real
promoters - it must also learn the SPACING. This is why a CNN is useful.
"""
import random, csv
random.seed(42)
BASES = "ACGT"
L = 100
N_PER_CLASS = 4000
MUT = 0.10

def rnd(n): return "".join(random.choice(BASES) for _ in range(n))

def mutate(m, rate=MUT):
    return "".join(random.choice([b for b in BASES if b != c]) if random.random() < rate else c for c in m)

def embed(core):
    left = random.randint(3, L - len(core) - 3)
    return rnd(left) + core + rnd(L - len(core) - left)

def promoter():
    return embed(mutate("TTGACA") + rnd(random.randint(16, 18)) + mutate("TATAAT"))

def decoy_single():
    box = mutate(random.choice(["TTGACA", "TATAAT"]))
    return embed(box)

def decoy_spacing():
    gap = random.choice(list(range(4, 11)) + list(range(26, 36)))
    return embed(mutate("TTGACA") + rnd(gap) + mutate("TATAAT"))

rows = []
for _ in range(N_PER_CLASS):
    rows.append((promoter(), 1))
    r = random.random()
    if r < 0.5:    rows.append((rnd(L), 0))
    elif r < 0.75: rows.append((decoy_single(), 0))
    else:          rows.append((decoy_spacing(), 0))
random.shuffle(rows)

with open("promoter_dataset.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["sequence", "label"]); w.writerows(rows)
print("Saved promoter_dataset.csv :", len(rows), "sequences")
