import re
from string import punctuation

class TailoTokenizer():
   def __init__(self):
      self.initial = ['ph', 'p', 
                      'm', 'b',
                      'tshi', 'tsh', 'tsi', 'ts', 'th','t', 
                      'n', 'l', 
                      'kh', 'k', 
                      'ng', 'g', 
                      'si', 's', 
                      'ji','j', 
                      'h']

   def tokenize(self, word):
      for onset in self.initial:
         if word.lower().find(onset) == 0:
            if onset[-1] == 'i':
               return [word[:len(onset)], word[len(onset) - 1:]]
            else:
               return [word[:len(onset)], word[len(onset):]]
      return [word]
   
   def tokenize_sentence(self, sent):
      tokens = []
      for word in re.split(r' |([%s]+)' % re.escape(punctuation), sent):
         if word is not None:
            if re.search(r'[%s]+' % re.escape(punctuation), word):
               # if any combination of punctuation
               tokens.append(word)
            else:
               # if a tai-lo romanization
               tokens.extend(self.tokenize(word))
      return tokens
   
   def tokenize_file(self, input_f, output_f):
      with open(input_f, 'r') as in_f:
         with open(output_f, 'w') as out_f:
            line = in_f.readline()
            while line:
               out_f.write(" ".join(self.tokenize_sentence(line)))
               line = in_f.readline()
