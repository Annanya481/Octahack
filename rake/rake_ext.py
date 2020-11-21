from rake_nltk import Rake, Metric
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import os 

def get_best(text):
    text = str(text).lower()

    nltk_stop = stopwords.words('english')
    r = Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO,
        stopwords=nltk_stop,
        punctuations='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    ) 
    

    text = text
    r.extract_keywords_from_text(text)

   

    return r.get_ranked_phrases_with_scores() 

def final_out(text):
    extractions = get_best(text)
    return extractions[0][1], extractions[0][1]





    