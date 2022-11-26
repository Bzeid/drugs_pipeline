import json

def load(graph_liaison, output_file_name):
    '''load tranform result (final graph liaison) to json file'''
    json_str = json.dumps(graph_liaison, indent=4)
    with open(output_file_name, "w") as outfile:
        outfile.write(json_str)
    
