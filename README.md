# Tai-Lo-Tokenizer
A basic tokenizer for tâi-lô (Taiwanese Hokkien romanization)

## To use
```python
from TailoTokenizer import TailoTokenizer

tokenizer = TailoTokenizer()

# To tokenize from an input file
tokenizer.tokenize_file(input_file, output_file)

# To tokenize a single sentence
tokens = tokenizer.tokenize_sentence(sent)

# To tokenize a single syllable/word
tokens = tokenizer.tokenize(word)

# To detokenize from an input file of tokenized strings
tokenizer.detokenize_file(input_file, output_file)

# To detokenize from a single list of tokens
sentence = tokenizer.detokenize(tokens)
```
