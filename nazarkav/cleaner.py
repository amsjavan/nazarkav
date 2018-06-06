import re
from bs4 import BeautifulSoup
import hazm
import pandas as pd
import nazarkav as nk
import os

data_path = os.path.join(nk.__path__[0], 'data')


def get_stopwords():
    stopwords = []
    with open(os.path.join(data_path, 'FarsiStopWords.txt'), 'r') as file:
        for line in file:
            stopwords.append(line.replace('\ufeff', '').replace('\n', ''))
    return stopwords


class Cleaner():
    def __init__(self,
                 tag=True,
                 nonletter=True,
                 spelling=True,
                 marker=True,
                 normalize=True):
        self.tag = self.remove_tag if tag else lambda x: x
        self.nonletter = self.remove_nonletter if nonletter else lambda x: x
        self.spelling = self.correct_spelling if spelling else lambda x: x
        self.normal = self.normalize if normalize else lambda x: x

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
        return self.tag(
                self.nonletter(
                        self.spelling(
							self.normal(record))))

    def clean_all(self, dataset):
        output = []
        for record in dataset:
            clean_record = self.tag(
                    self.nonletter(
                            self.spelling(
								self.normal(record))))
            output.append(clean_record)
        return output