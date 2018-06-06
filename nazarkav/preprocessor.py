import os
from bs4 import BeautifulSoup
import hazm
import re
import nazarkav as nk

data_path = os.path.join(nk.__path__[0], 'data')


def get_stopwords():
    stopwords = []
    with open(os.path.join(data_path, 'FarsiStopWords.txt'), 'r') as file:
        for line in file:
            stopwords.append(line.replace('\ufeff', '').replace('\n', ''))
    return stopwords


class Preprocessor():
    def __init__(self,
                 stem=True):
        self._stem = self.stem if stem else lambda x: x
        self.regex = re.compile('[0-9۰-۹()-/"\':,;\^*\.!?،؟]')

    def remove_tag(self, input):
        return BeautifulSoup(input, "html.parser").get_text()

    def remove_nonletter(self, input):
        return self.regex.sub(' ', input)

    def correct_spelling(self, input):
        return input

    def normalize(self, input):
        return hazm.Normalizer().normalize(input)

    def clean(self, record):
        return self.remove_tag(
            self.remove_nonletter(
                self.correct_spelling(
                    self.normalize(record))))

    def clean_all(self, dataset):
        output = []
        for record in dataset:
            clean_record = self.remove_tag(
                self.remove_nonletter(
                    self.correct_spelling(
                        self.normalize(record))))
            output.append(clean_record)
        return output

    def stem(self, word):
        return hazm.Stemmer().stem(word)

    def stem_tokenize(self, record):
        """Tokenize persian words and then stem each of them and return a list of words

        Parameters
        ----------
        record : str
            a document

        Returns
        -------
        output : list of string
            List of word
        """
        output = []
        for w in hazm.WordTokenizer().tokenize(record):
            output.append(self._stem(w))
        return output

    def tokenize(self, record):
        return hazm.WordTokenizer().tokenize(record)
