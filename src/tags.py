import requests
import json
import pandas as pd

from collections import Counter

#avoid the docker setting up by doing so
#json_data ={'query': '"How can I generate conditional distributions of data by taking slices of scatterplots?"', 'prediction': {'topIntent': 'plot', 'intents': {'plot': {'score': 0.9788371}}, 'entities': {'data': [{}], 'plots': [{'plot type': [{'scatterplot': ['scatterplots'], '$instance': {'scatterplot': [{'type': 'scatterplot', 'text': 'scatterplots', 'startIndex': 74, 'length': 12, 'score': 0.9501133, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], '$instance': {'plot type': [{'type': 'plot type', 'text': 'scatterplots', 'startIndex': 74, 'length': 12, 'score': 0.9486826, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], 'action': [{'make': ['generate'], '$instance': {'make': [{'type': 'make', 'text': 'generate', 'startIndex': 11, 'length': 8, 'score': 0.9749215, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}], '$instance': {'data': [{'type': 'data', 'text': 'data', 'startIndex': 49, 'length': 4, 'score': 0.9762081, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'plots': [{'type': 'plots', 'text': 'scatterplots', 'startIndex': 74, 'length': 12, 'score': 0.9448885, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}], 'action': [{'type': 'action', 'text': 'generate', 'startIndex': 11, 'length': 8, 'score': 0.974810064, 'modelTypeId': 1, 'modelType': 'Entity Extractor', 'recognitionSources': ['model']}]}}}} 

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

# We send the 5 questions that are alike from the tags
def match_tags(tag_list, db_tag):
    
    inbrefID = {}
    for tag in tag_list[:len(tag_list) - 1]:        
        matched = db_tag[db_tag["Tag"] == tag]["Id"].values
        matched_list = matched.tolist()
        histo = {k:matched_list.count(k) for k in set(matched_list)}

        inbrefID = dict(Counter(inbrefID) + Counter(histo))

    return inbrefID

def get_answers_alike(tag_list):
    
    # RIP RAM
    # Can and should be improved

    data_path = '../data/'

    try :
        pd_tags = pd.read_csv(data_path + 'Tags.csv')
        pd_answ = pd.read_csv(data_path + 'Answers.csv')
        pd_qst = pd.read_csv(data_path + 'Questions.csv')
    
    except OSError:
        print("Could not open Tags.csv, Questions.csv or Answers.csv check if thoses files are in the good directory.")
        return
    
    # Make an dictionary compiling all the ids in the db of Tags that matches thoses computed with LUIS
    matched_ids = match_tags(tag_list,pd_tags)
    
    # We sort from the most to the least relevant id and keep the top five
    sorted_matched_ids = sorted(matched_ids, key=matched_ids.get, reverse=True)[:5]
    
    # Array for the best answer we want to return to the user
    matched_answ = []
    matched_qst = []
    
    # Loop over our best matchs
    for ids in sorted_matched_ids:
        # Get the answers that correspond to the id of the matched question
        answer = pd_answ[pd_answ["ParentId"] == ids]
        
        # Sort them based on their score and keep the first one
        answer = answer.sort_values(by=["Score"]).head(1)
        
        answer_body = answer["Body"].values
        if len(answer_body) != 0:
            matched_answ.append(answer_body[0])

        # Get the question title that correspond to the id of the matched question
        question_title = pd_qst[pd_qst["Id"] == ids]["Title"].values
        
        if len(question_title) != 0:
            matched_qst.append(question_title[0])
        
    return matched_answ, matched_qst   
