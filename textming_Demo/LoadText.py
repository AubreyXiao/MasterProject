from os import listdir
import string
from collections import Counter
from nltk.corpus import stopwords


#read the file and return the text
def load_doc(filename):
    #open and only for read
    file = open(filename,'r')
    text = file.read()
    file.close()
    return text


#clean each document (remove punctuation, stopwords)
def clean_doc(doc):
    tokens = doc.split()
    #replace all "," with string.punctuation
    table = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(table) for w in tokens]
    #remove those are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]
    #filter out stop words
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]
    #filter out short words
    tokens = [word for word in tokens if len(word)>1]

    return tokens

def add_doc_to_vocab(filename,vocab):
    #load the doc
    doc = load_doc(filename)
    #clean the doc
    tokens = clean_doc(doc)
    #update the vocab
    vocab.update(tokens)

#save the tokens to a file
def save_list(tokens, filename):
    data = '\n'.join(tokens)
    file = open(filename,'w')
    file.write(data)
    file.close()

#take directory and read each text
def process_docs(directory,vocab):
    lines = list()
    for filename in listdir(directory):

        if not filename.endswith(".txt"):
           continue
        path = directory + '/'+ filename
        line = add_doc_lines(path,vocab)
        lines.append(line)
    return lines

#clean and transfer a file to a string and append it to a list( positive ane negative)
def add_doc_lines(filename, vocab):
    doc = load_doc(filename)
    tokens = clean_doc(doc)
    new_tokens = [w for w in tokens if w in vocab]

    return ' '.join(new_tokens)


# load the vocab

vocab_filename = "/Users/xiaoyiwen/MasterDemo/vocab.txt"
vocab = load_doc(vocab_filename)
vocab = vocab.split()
vocab = set(vocab)

negative_lines = process_docs("/Users/xiaoyiwen/Desktop/review_polarity/txt_sentoken/neg",vocab)
positive_lines = process_docs("/Users/xiaoyiwen/Desktop/review_polarity/txt_sentoken/pos",vocab)


save_list(negative_lines,'negative_reviews.txt')
save_list(positive_lines,'positive_reviews.txt')





#######test document

#define a vocab
#vocab = Counter()
#build up the vocab
#process_docs("/Users/xiaoyiwen/Desktop/review_polarity/txt_sentoken/neg",vocab)
#process_docs("/Users/xiaoyiwen/Desktop/review_polarity/txt_sentoken/pos",vocab)

#print(len(vocab))
#print(vocab.most_common(50))

#shrink the vocab >=5
#min_occurance = 5
#tokens = [k for k,c in vocab.items() if c>=min_occurance]
#print(len(tokens))
#
#save to a vocab file
#save_list(tokens,'vocab.txt')


