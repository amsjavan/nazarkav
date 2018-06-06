from bs4 import BeautifulSoup
import hazm
import pandas as pd


class Cleaning():
    def __init__(self,
                 dataset_path=None,
                 tag=False,
                 spelling=False,
                 marker=False,
                 normalize=False):
        self.dataset_path = dataset_path
        self.dataset = None
        if dataset_path:
            with open(dataset_path, 'r') as file:
                self.dataset = file.readlines()
        self.tag = self.remove_tag if tag else lambda x: x
        self.spelling = self.correct_spelling if spelling else lambda x: x
        self.marker = self.remove_marker if marker else lambda x: x
        self.normal = self.normalize if normalize else lambda x: x

    def remove_tag(self, input):
        return BeautifulSoup(input, "html.parser").get_text()

    def correct_spelling(self, input):
        return input

    def remove_marker(self, input):
        return input

    def normalize(self, input):
        return hazm.Normalizer().normalize(input)

    def clean(self, input=None, overwrite=False):
        clean_data = self.tag(
                self.spelling(
                        self.marker(
                                self.normal(self.dataset if self.dataset else input))))
        if overwrite and self.dataset_path:
            with open(self.dataset_path, 'w') as file:
                file.write(clean_data)


def get_stopwords(self):
    stopwords = []
    with open('data/FarsiStopWords.txt', 'r') as file:
        for line in file:
            stopwords.append(line.replace('\ufeff', '').replace('\n', ''))
    return stopwords


def test():
    c = Cleaning('data/hotel-polarity.tsv', normalize=True)
    c.clean(overwrite=True)


test()
