import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

def col_dup_remover1(data: pd.DataFrame) -> pd.DataFrame:
    data.drop_duplicates(subset=['Количество комнат',
                                 'Адрес',
                                 'Площадь, м2',
                                 'Дом'], 
                         inplace=True)
    return data

def col_dup_remover2(data: pd.DataFrame) -> pd.DataFrame:
    data.drop_duplicates(subset=['Комнат',
                                 'Адрес',
                                 'Площадь',
                                 'Этаж',
                                 'Этажность_дома'], 
                         inplace=True)
    return data