import requests
import json

from tags import *


def get_json_from_query(query):
    APP_ID="481300a9-e5c5-49ac-a6ea-20f1c037393d"
    APP_VERSION="merge_trial"

    API_ENDPOINT = f"http://luis:5000/luis/prediction/v3.0/apps/{APP_ID}/versions/{APP_VERSION}/predict?verbose=true&query=\"{query}\""

    # sending get request and saving response as response object
    r = requests.get(url = API_ENDPOINT)

    # extracting response text 
    json_data = json.loads(r.text)

    return json_data



def get_top5(query, pd_tags, pd_answ, pd_qst):

    json_data = get_json_from_query(query)

    tag_list, tag_value = get_tags(json_data)

    print("\n\n#################\n\n")
    print("tag list:", tag_list)
    print("\n\n#################\n\n")

    return get_answers_alike(tag_list, pd_tags, pd_answ, pd_qst)
