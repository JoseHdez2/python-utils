import english_words as EW
import nltk
import random
  
def random_words(n):
  return random.sample(EW.english_words_lower_set, 3)
  
def random_word():
  return random_words(1)[0]
  
#def adjective_noun():
  
#  while 