raw = open("Beyond_Good_and_Evil.txt", "r").read().lower().strip().split()

def freq(word):
   list_single_word = filter(lambda x: x == word, raw)
  
   return len(list_single_word)

def freq_words(words):
   list_words = filter(lambda x: x in words, raw)
   return len(list_words)


def max_freq():
   word = reduce( lambda x, y: x if freq(x) >= freq(y) else y, raw )
   return word

print freq("Good")
print freq("Evil")
print freq_words(["What","is"])

print max_freq()
