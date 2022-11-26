## Project description

This project contain the different modules of the(ETL) pipeline required to build graph liaison for drugs.

### python Used Packages 

After installing python (https://www.python.org/),
you will have to insall prerequisites packages by running the following command in the terminal of your local machine: 
pip install -r requirements.txt 




#### 2 - Getting the project 

After having python and all prerequisites packages,
you can get the project from the remote git repo by running the following git command:

git clone https://github.com/Emirov/data_pipeline_wevops_test.git




## Run the pipeline


you run the project by running the following command in the terminal of your local machine:
python main.py

you will see the logs of the project in your terminal, you will also notice that a two new json files named drugs_graph_liaison.json and journals_with_most_drugs.json are created in the project directory. the drugs_graph_liaison.json  contain the final graph_liaison for each drug and the journals_with_most_drugs.json will contain the result of adhoc processing ( journals with most drug).
