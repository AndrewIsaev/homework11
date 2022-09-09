import json




def load_candidates_from_json(path:str):
    """
    Return list of all candidates from json file
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id:int):
    for candidate in load_candidates_from_json("candidates.json"):
        if candidate["id"] == candidate_id:
            return candidate
        return "Нет такого кандидата"


