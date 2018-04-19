#convert to lowercase
#Text has been split into one sentence per line.
#There is white space around punctuation like periods, commas, and brackets.

from os import listdir
import string
from collections import Counter
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.text import text_to_word_sequence
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
import nltk.tokenize.punkt
import re
import regex


#load the file and return the text
def load_file(filename):
    #open and only for read
    file = open(filename,'r')
    text = file.read()
    file.close()
    return text

#clean the doc
#remove: # tags, punctuations, not alphabate, stopwords, ,shortwords
#?? stemming words , mutil words.
def convert_text_to_tokens(text):
    #remove tags from the text
    print(text)
    text = re.sub("<.*?>", "\n", text)
    print("-2:remove the tags and split the sentences")
    print(text)
    tokens = text.split("\n")
    print("-1:split the sentences into a list")
    print(tokens)
    # #split the text into sentences
    # tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
    # tokens = tokenizer.tokenize(text)
    # print("0:split the text into sentences:")
    # print(tokens)
    #convert to lowercase
    tokens = [token.lower() for token in tokens]
    print("2:lowercase:")
    print(tokens)
    #filter the puntuactions
    #tokens = text_to_word_sequence(text, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\n', lower=True, split=' ')
    table = str.maketrans('','',string.punctuation)
    tokens = [w.translate(table) for w in tokens if w!='']
    print("3:remove punctuations")
    print(tokens)
    print("tokenization!!!!!!!!!!!!!!!!!!!")
    #remove those are not alphabate
    tokens1 = []
    for token in tokens:
        token2 = word_tokenize(token)
        tokens1 += token2
    print(tokens1)

    tokens2 = [word1 for word1 in tokens1 if word1.isalpha()]
    print("4:remove alphabate:")
    print(tokens2)
    #filter out the stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word1 for word1 in tokens1 if word1 not in stop_words]
    print("5:remove stopwors:")
    print(tokens)
    #filter out the short words
    tokens = [w for w in tokens if len(w)>1]
    print("6:remove shortwords:")
    print(tokens)
    #stemming words
    stemmer =SnowballStemmer('english')
    tokens = [stemmer.stem(t) for t in tokens]
    print("7:stemmed words:")
    print(tokens)
    return tokens

#stemming the words and return a list of stemmed-tokens
def do_stemming(tokens):
    stemmed = []
    for t in tokens:
        stemmed.append(SnowballStemmer('english').stem(t))
    return stemmed

#load all docs in a directory
def process_files(directory, is_trian):
    for filename in listdir(directory):
       if not filename.endswith(".txt"):
           continue
       if not is_trian:
           break
       path = directory + '/' + filename
       text = load_file(path)
       convert_text_to_tokens(text)

       #add_doc_to_vocab(path, vocab)

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

filename = "/Users/xiaoyiwen/Desktop/datasets/train/neg1/7_3.txt"
text = load_file(filename)
convert_text_to_tokens(text)













