import pandas as pd
from bs4 import BeautifulSoup
import re
import hazm
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import nazarkav as nk


train = None

def fetch_data():
    df = pd.DataFrame(data={'c1': [1111111, 2, 3], 'c2': [4, 5, 6]})
    df.to_csv('test.tsv', sep="\t", index=False)
    print(df)

def balance_data():
    cols = ['comment', 'c', 'rate', 'name', 'date']

    # Read the labeled data
    data = pd.read_csv('data/hotel-dataset.csv', names=cols)

    # Sampling
    pos_data = data[data['c'] == 'pos'].sample(n=2000)
    neg_data = data[data['c'] == 'neg'].sample(n=2000)

    # Concat
    hotel_polarity = pd.concat([pos_data, neg_data], ignore_index=True)

    # Save to file
    hotel_polarity[['comment', 'c']].to_csv('data/hotel-polarity.tsv', sep='\t', encoding='utf8', index=False)


def remove_tag():
    with open('data/hotel-dataset.csv', 'r', encoding='utf8') as f:
        hotel_data = f.read()

    with open('data/hotel-dataset.csv', 'w', encoding='utf8') as f:
        f.write(BeautifulSoup(hotel_data, "html.parser").get_text())

def remove_nonletter():
    with open('data/hotel-dataset.tsv', 'r', encoding='utf8') as f:
        hotel_data = f.read()

    with open('data/hotel-dataset.tsv', 'w', encoding='utf8') as f:
        # Remove non-letters and save it
        f.write(re.sub("[^a-zA-Z]", " ", hotel_data))

def bag_of_word():
    hotel_pol = pd.read_csv('data/hotel-polarity.tsv', sep='\t')
    tokenizer = hazm.WordTokenizer()

# def split():
#     #numy
#     train, test = train_test_split( data, train_size = 0.8, random_state = 44 )
#
#     # for panda use following code
#     all_i = np.arange( len( data ))
#     train_i, test_i = train_test_split( all_i, train_size = 0.8, random_state = 44 )
#     train = data.ix[train_i]
#     test = data.ix[test_i]
#
# def metric():
#     p = rf.predict_proba( test_x )
#     auc = AUC( test_y, p[:,1] )
#
# def theano:
#     #use in svd
def mytokenizer(record):
    print(record)
    return nk.Preprocessor().preprocess(record)

def preproc(l):
    print(l)
    return l

def bow():
    corpus = ['چشم‌انداز اتاق‌ها بسیار خوب بود',
              'کیفیت غذای رستوران جالب نبود',
              'اتاق‌ها بسیار خوب بودند']
    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # bag of words tool.
    vectorizer = CountVectorizer(
            tokenizer=nk.Preprocessor().tokenize,
            preprocessor=nk.Cleaner().clean)

    # fit_transform() does two functions: First, it fits the model
    # and learns the vocabulary; second, it transforms our training data
    # into feature vectors. The input to fit_transform should be a list of
    # strings.
    train_data_features = vectorizer.fit_transform(corpus)

    # Numpy arrays are easy to work with, so convert the result to an
    # array
    train_data_features = train_data_features.toarray()
    print(vectorizer.get_feature_names())



import sys
print(sys.version_info)

bow()