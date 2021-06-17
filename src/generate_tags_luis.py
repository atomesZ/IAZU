import pandas as pd
import numpy as np

from top5 import *
from tags import *

def get_query_tags_db(query, query_id, db_luis_tags):
    # Compute our tag list from the question title
    tag_list, tag_values = get_tags(get_json_from_query(query))

    for tag in tag_list[:len(tag_list) - 1]:
        db_luis_tags = pd.concat([db_luis_tags, pd.DataFrame({"Id":[query_id], "Tag":[tag]})])

    return db_luis_tags

def generate_luis_tags(db_questions):
    db_titles = db_questions[["Title","Id"]].values

    # Create a temporay dataframe to store all the tags and their query ID
    db_luis_tags = pd.DataFrame(columns=["Id", "Tag"])

    for title, id_ in db_titles:
        db_luis_tags = get_query_tags_db(title, id_, db_luis_tags)

    return db_luis_tags