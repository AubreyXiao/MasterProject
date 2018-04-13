#convert to lowercase
#Text has been split into one sentence per line.
#There is white space around punctuation like periods, commas, and brackets.

from os import listdir
import string
from collections import Counter
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.text import text_to_word_sequence
import re


#load the file and clean them
#convert to lowercase
#Text has been split into one sentence per line.
#There is white space around punctuation like periods, commas, and brackets.


#load the file and return the text
def load_file(filename):
    #open and only for read
    file = open(filename,'r')
    text = file.read()
    file.close()
    return text

#clean the doc
def convert_text_to_tokens(text):
    #remove tags from the text
    text = re.sub("<.*?>", "", text)
    print(text)
    #filter the puntuactions
    tokens = text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\n', lower=True, split=' ')
    #remove those are not alphabate
    tokens = [word for word in tokens if word.isalpha()]
    #filter out the stopwords
    print(tokens)
    stop_words = set(stopwords.words('english'))
    tokens = [word1 for word1 in tokens if word1 not in stop_words]
    #filter out the short words
    tokens = [w for w in tokens if len(w)>1]
    return tokens



#load all docs in a directory
def process_files(directory, vocab, is_trian):
    for filename in listdir(directory):
       if not filename.endswith(".txt"):
           continue
       if not is_trian:
           break
       path = directory + '/' + filename
       add_doc_to_vocab(path, vocab)

#load doc and add to vocab
def add_doc_to_vocab(filename,vocab):
    text = load_file(filename)
    tokens = convert_text_to_tokens(text)
    vocab.update(tokens)


#save a list to a file
def save_to_file(token,filename):
    data = '/n'.join(token)
    file = open(filename,'w')
    file.write(data)
    file.close()

#should pass a vocab
def shrink_vocab(vocab, k):
    min_occurrence = k
    tokens = [ w for w, k in vocab.items() if k>=min_occurrence ]
    print(vocab.most_common(50))
    return tokens




#define a vocab
#vocab = Counter()

#define the dir needs to be processed
#neg_dir = "/Users/xiaoyiwen/Desktop/datasets/train/neg1"
#pos_dir = "/Users/xiaoyiwen/Desktop/datasets/train/pos1"

#update the vocab
#process_files(neg_dir,vocab,True)
#process_files(pos_dir,vocab,True)

#shrink_vocab(vocab,5)
#save_to_file(vocab,"vocab.txt")

neg_reviews = "/Users/xiaoyiwen/Desktop/datasets/train/neg1/3_4.txt"
text = load_file(neg_reviews)
print(text)


# tokens = convert_text_to_tokens(text)
# print(tokens)












