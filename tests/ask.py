import requests
import json


APP_ID="481300a9-e5c5-49ac-a6ea-20f1c037393d"
APP_VERSION="merge_trial"

AZURE_REGION="westeurope"

# TODO pre-taitement chopper la query sous forme de string

query = "How can I generate conditional distributions of data by taking slices of scatterplots?"

API_ENDPOINT = f"http://localhost:5000/luis/prediction/v3.0/apps/{APP_ID}/versions/{APP_VERSION}/predict?verbose=true&query=\"{query}\""

# sending get request and saving response as response object
r = requests.get(url = API_ENDPOINT)

# extracting response text 
json_data = json.loads(r.text)

print(json_data)

# TODO post traitement




# We send a list of tags

def get_tags(json_data):
    """
    Return list of tags
    """
    
    list_of_tags = []

    return list_of_tags



# We send the 5 questions that are alike from the tags
def get_5_questions_alike(list_of_tags):
    """
    Return: List of strings
    """
    questions_alike = []

    return questions_alike



def print_web(questions_alike):
    pass
