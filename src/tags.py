import requests
import json
import pandas as pd

from collections import Counter


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

def get_answers_alike(tag_list, pd_tags, pd_answ, pd_qst):
 
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
