import requests
import json

#avoid the docker setting up by doing so
json_data ={'query': '"How can I generate conditional distributions of data by taking slices of scatterplots?"', 'prediction': {'topIntent': 'plot', 'intents': {'plot': {'score': 0.9788371}}, 'entities': {'data': [{}], 'plots': [{'plot type': [{'scatterplot': ['scatterplots'], '$instance': {'scatterplot': [{'type': 'scatterplot', 'text': 'scatterplots', 'startIndex': 74, 'length': 12, 'score': 0.9501133, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], '$instance': {'plot type': [{'type': 'plot type', 'text': 'scatterplots', 'startIndex': 74, 'length': 12, 'score': 0.9486826, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], 'action': [{'make': ['generate'], '$instance': {'make': [{'type': 'make', 'text': 'generate', 'startIndex': 11, 'length': 8, 'score': 0.9749215, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], '$instance': {'data': [{'type': 'data', 'text': 'data', 'startIndex': 49, 'length': 4, 'score': 0.9762081, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'plots': [{'type': 'plots', 'text': 'scatterplots', 'startIndex': 74, 'length': 12, 'score': 0.9448885, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'action': [{'type': 'action', 'text': 'generate', 'startIndex': 11, 'length': 8, 'score': 0.974810064, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}}} 

def get_tags(json_data):
    """
    Returns tag_list, the list of tags and tag value, the list of tags with associated keys
    """
    entities = json_data['prediction']['entities']
    
    tag_list = []
    tag_value = []
   
    for tag in entities:
        
        tag_list.append(tag)
        tag_value.append(entities[tag])

    return tag_list, tag_value