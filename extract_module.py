import pandas as pd
import json
from jsoncomment import JsonComment

def extract_csv(csv_file):
    '''extract csv to pandas dataframe'''
    '''input: csv file'''
    '''output: pandas Data frame'''
    dataframe =  pd.read_csv(csv_file, sep=",", encoding = 'utf8')
    return dataframe

def extract_json(json_file):
    '''extract json to pandas dataframe'''
    '''input: json file'''
    '''output: pandas Data frame'''
    with open("pubmed.json") as data_file:
        # use JsonComment to deal with Trailing comma at the end of pubmed.json file.
        parser = JsonComment(json)
        data = parser.load(data_file)
    dataframe = pd.DataFrame.from_dict(data)
    return dataframe   
    