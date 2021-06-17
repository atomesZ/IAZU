import requests
import json

from tags import *


def get_top5(query):

    APP_ID="481300a9-e5c5-49ac-a6ea-20f1c037393d"
    APP_VERSION="merge_trial"

    API_ENDPOINT = f"http://localhost:5000/luis/prediction/v3.0/apps/{APP_ID}/versions/{APP_VERSION}/predict?verbose=true&query=\"{query}\""

    # sending get request and saving response as response object
    r = requests.get(url = API_ENDPOINT)

    # extracting response text 
    json_data = json.loads(r.text)


    tag_list, tag_value = get_tags(json_data)

    return get_answers_alike(tag_list)
