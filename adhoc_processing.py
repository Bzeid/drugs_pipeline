import json
from collections import Counter
import logging

def read_json(file_input):
    '''read json file'''
    f = open(file_input)
    graph_liaison = json.load(f)
    return graph_liaison


def get_journals_with_most_drugs(path_graph_liaison):
    '''get the journals with most drugs'''
    '''input: path of the json file containing final result of the pipeline (final graph liaison)'''
    '''output: json file with journals with most drugs'''

    logging.info(f'Gettintg journals with most drug')
    graph_liaison = read_json(path_graph_liaison)
    list_journals_in_graph=[]
    for drug in graph_liaison.keys():
       drug_journals = [sublist[0].replace('\\xc3\\x28', '') for sublist in graph_liaison[drug]['journals']]
       list_journals_in_graph = list_journals_in_graph + drug_journals
    journals = [k for k, v in Counter(list_journals_in_graph).items() if v == max(Counter(list_journals_in_graph).values())]
    data = {"journals_with_most_drugs":journals}
    with open('journals_with_most_drugs.json', 'w') as f:
        json.dump(data, f)