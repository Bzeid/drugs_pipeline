from extract_module import *
from transform_module import *
from load_module import *
from adhoc_processing import *

def main():

    drugs = extract_csv("drugs.csv")
    clinical_trials = extract_csv("clinical_trials.csv")
    # extract pubmed from both csv and json files
    pubmed = pd.concat([extract_csv("pubmed.csv"), extract_json("pubmed.json")], ignore_index=True)
    
    graph_liaison = transform(drugs, clinical_trials, pubmed)
    load(graph_liaison, "drugs_graph_liaison.json")
    
    # Getting the result of the adhoc processing (journals with most drugs)
    get_journals_with_most_drugs("drugs_graph_liaison.json")

if __name__== "__main__":
    main()