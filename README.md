# Italian-Vocabulary-Recommender

### This system recommends new Italian vocabulary tailored to a language learner’s target CEFR (Common European Framework of Reference for Languages) level and known vocabulary. It uses rule-based filtering combined with semantic similarity and a machine learning model to rank how “ready” the learner is to learn each word.

## Project Components

### Italian Vocabulary Recommender
Italian_Vocabulary_Recommender.ipynb

### Data Extraction
it_m3.xls
italian_freq.txt (frequency list)
Data Extraction.ipynb

### Input Collection and Vocabulary Dataset
known_words.json
italian_cefr_vocab_with_freq_pos.csv

### FastText word embeddings for semantic similarity
cc.it.300.vec https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.it.300.vec.gz
filter_fasttext_to_vocab.py
cc.it.filtered.vec

### Feedback Loop
learnability_log.json

### Logistic Regression (Readiness Scoring)
train_word_readiness_model.ipynb






