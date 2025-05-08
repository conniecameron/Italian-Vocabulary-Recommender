import pandas as pd

# Load your CEFR + frequency vocabulary list
vocab_df = pd.read_csv("/home/connie/Downloads/italian_cefr_vocab_with_freq.csv")
target_words = set(vocab_df["word"].str.lower())

# Filter the FastText .vec file
input_vec = "/home/connie/Downloads/cc.it.300.vec"
output_vec = "/home/connie/Downloads/cc.it.filtered.vec"

print("🔍 Filtering word vectors... This may take a few minutes.")

with open(input_vec, "r", encoding="utf-8") as fin, open(output_vec, "w", encoding="utf-8") as fout:
    header = fin.readline()
    fout.write(header)  # Keep original header

    kept = 0
    for line in fin:
        word = line.split(" ", 1)[0]
        if word.lower() in target_words:
            fout.write(line)
            kept += 1

print(f"✅ Done! Saved {kept} word vectors to {output_vec}")
