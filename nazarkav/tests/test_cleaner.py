import pandas as pd
import os.path as op
import numpy.testing as npt
import nazarkav as nk

data_path = op.join(nk.__path__[0], 'data')


def test_Cleaner():
    # hotel_pol = pd.read_csv(op.join(data_path, 'hotel-polarity.tsv'), sep='\t').head()
    # sample = hotel_pol['comment'].tolist()
    sample = ['این هتل خیلی خوبی می باشد؟',
              'این متن حاوی تگ <br> می باشد']
    output = ['این هتل خیلی خوبی می‌باشد ',
              'این متن حاوی تگ  می‌باشد']
    cleaner = nk.Cleaner()
    print(cleaner.clean('? .سیسی ۱ ۲0 3یبیب '))


    npt.assert_equal(cleaner.clean_all(sample),output)


test_Cleaner()

def test():
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfVectorizer
    import pandas as pd
    import numpy as np
    import hazm
    import os
    import nazarkav as nk
    data_path = '/home/amir/Dropbox/ProgrammingProjects/Python/nazarkav/nazarkav/data'
    hotel_pol = pd.read_csv(os.path.join(data_path, 'hotel-polarity.tsv'), sep='\t')
    hotel_comment = hotel_pol['comment'].tolist()
    vectorizer = CountVectorizer(
    tokenizer=nk.Preprocessor(stem=False).tokenize,
    preprocessor=nk.Cleaner().clean,
    max_features=20)
    train_data_features = vectorizer.fit_transform(hotel_comment)
    nk.dataframe2png(pd.DataFrame(train_data_features.toarray(),columns=vectorizer.get_feature_names
                ()).head(10))
    nk.dataframe2png(pd.DataFrame(train_data_features.toarray(),columns=vectorizer.get_feature_names
            ()).head(10))
test()