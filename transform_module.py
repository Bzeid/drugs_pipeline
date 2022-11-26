import re
import pandas as pd
import logging

# config loggings
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')

def get_rows_containing_drug(drug_name, df, column_name):
    '''filter the dataframe following the given drug'''
    df[drug_name] = df[column_name].str.lower().map(lambda x: bool(re.search( drug_name.lower() , x)))
    df_rows_containing_drug  =   df[df[drug_name]== True]
    return df_rows_containing_drug

def get_column_value(dataframe, column_name):
    '''return pubmed tile, clinical trials scientific_title or journals 
       from dataframe with the associated date'''
    dataframe_filtred = dataframe[[column_name, 'date']].copy()
    # formatting date
    dataframe_filtred['date'] = pd.to_datetime(dataframe_filtred['date']).dt.strftime('%d/%m/%Y')
    column_value_with_date =  list(set(dataframe_filtred.itertuples(index=False, name=None)))
    return column_value_with_date 

def transform(drugs, clinicaltrials, pubmed):
    '''Transform extracted files to create drugs graphs liaisons'''
    '''input: dataframes containing drugs, clinicaltrials and pubmed'''
    '''output: json file containing the graph liaison for drugs'''
    graph_liaison = []
    drugs = drugs['drug']
    for drug in drugs:
        logging.info(f'creating graph liaison for {drug} ...')
        logging.info(f'extracting clinical trials scientific_title containing {drug}')
        clinicaltrials_including_drug = get_rows_containing_drug(drug, clinicaltrials, 'scientific_title')
        logging.info(f'extracting pubmed title containing {drug}')
        pubmed_including_drug = get_rows_containing_drug(drug, pubmed, 'title')
        clinicaltrials_scientific_title = get_column_value(clinicaltrials_including_drug, 'scientific_title')
        pubmed_title = get_column_value(pubmed_including_drug, 'title')
        clinicaltrials_journals = get_column_value(clinicaltrials_including_drug, 'journal')
        pubmed_journals = get_column_value(pubmed_including_drug, 'journal')
        drug_journals = list(set(pubmed_journals + clinicaltrials_journals))
        drug_dict = {"pubmed":pubmed_title, "clinical_trials":clinicaltrials_scientific_title, "journals": drug_journals }  
        graph_liaison.append(drug_dict)
    graph_liaison = dict(zip(drugs,graph_liaison))
    return graph_liaison
        