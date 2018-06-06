import pandas as pd
import os.path as op
import numpy.testing as npt
import nazarkav as nk

data_path = op.join(nk.__path__[0], 'data')


def test_Preprocessor():
    # hotel_pol = pd.read_csv(op.join(data_path, 'hotel-polarity.tsv'), sep='\t').head()
    # sample = hotel_pol['comment'].tolist()

    preprocessor = nk.Preprocessor()
    sample = 'قبلا این هتل اتاق‌های خوبی داشته است.'
    output = ['قبلا', 'این', 'هتل', 'اتاق', 'خوب', 'داشته_اس', '.']
    npt.assert_equal(preprocessor.stem_tokenize(sample), output)

    # hotel_pol = pd.read_csv(op.join(data_path, 'hotel-polarity.tsv'), sep='\t').head()
    # sample = hotel_pol['comment'].tolist()
    sample = ['این هتل خیلی خوبی می باشد؟',
              'این متن حاوی تگ <br> می باشد',
              'ین متن حاوی نشانگر های ! ? . می باشد']
    output = ['این هتل خیلی خوبی می‌باشد ',
              'این متن حاوی تگ  می‌باشد',
              'ین متن حاوی نشانگر‌های     می‌باشد']
    npt.assert_equal(preprocessor.clean_all(sample), output)


test_Preprocessor()