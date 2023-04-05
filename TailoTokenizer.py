import re
from string import punctuation

class TailoTokenizer():
   def __init__(self):
      self.consonants = ['ph', 'p', 
                      'm', 'b',
                      'tshi', 'tsh', 'tsi', 'ts', 'th','t', 
                      'n', 'l', 
                      'kh', 'k', 
                      'ng', 'g', 
                      'si', 's', 
                      'ji','j', 
                      'h']

   def tokenize(self, word):
      for onset in self.consonants:
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
   
   def tokenize_file(self, in_file, out_file):
      with open(in_file, 'r') as in_f:
         with open(out_file, 'w') as out_f:
            line = in_f.readline()
            while line:
               out_f.write(" ".join(self.tokenize_sentence(line)))
               line = in_f.readline()

   def detokenize(self, tokens):
      i = 0
      sentence = []
      dash_found = False
      while i < len(tokens):
         if re.search(r'[%s]+' % re.escape(punctuation), tokens[i]):
            # if the current token is punctuation
            if '-' in tokens[i]:
               dash_found = True
            sentence.append(tokens[i])
            i += 1
         else:
            if tokens[i] in self.consonants:
               # if the current token is a consonant, combine it with the next
               if tokens[i][-1] == 'i' and tokens[i+1][0] == 'i':
                  # reduce double i into single i
                  sentence.append("".join([tokens[i], tokens[i+1][1:]]))
               else:
                  sentence.append("".join(tokens[i:i+2]))
               i += 2
            else:
               sentence.append(tokens[i])
               i += 1

            if dash_found:
               compound = [sentence.pop() for i in range(3)]
               sentence.append("".join(compound[::-1]))
               dash_found = False
            
      
      return " ".join(sentence)
   
   def detokenize_file(self, in_file, out_file):
      with open(in_file, 'r') as in_f:
         with open(out_file, 'w') as out_f:
            line = in_f.readline()
            while line:
               out_f.write(self.detokenize(line.split()) + '\n')
               line = in_f.readline()