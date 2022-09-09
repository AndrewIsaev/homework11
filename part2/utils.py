import json




def load_candidates_from_json(path:str):
    """
    Return list of all candidates from json file
    """

    with open(path, encoding="utf-8") as file:
        return json.load(file)


