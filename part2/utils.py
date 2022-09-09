import json
from typing import List, Dict

PATH = "candidates.json"
def load_candidates_from_json(path: str) -> List[dict]:
    """
    Return list of all candidates from json file
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id: int) -> Dict|str:
    for candidate in load_candidates_from_json(PATH):
        if candidate["id"] == candidate_id:
            return candidate



def get_candidates_by_name(candidate_name: str) -> List|str:
    candidates_by_name = []
    for candidate in load_candidates_from_json(PATH):
        if candidate["name"].lower().split()[0] == candidate_name.lower():
            candidates_by_name.append(candidate)
            return candidates_by_name




def get_candidate_by_skill(skill: str) -> List:
    candidate_by_skill_list = []
    for candidate in load_candidates_from_json(PATH):
        if skill in candidate["skills"].lower().split(", "):
            candidate_by_skill_list.append(candidate)
    return candidate_by_skill_list


def formatted_output(candidates_list: list) -> str:
    res = ""
    for candidate in candidates_list:
        res += "<h1>" + candidate["name"] + "<br>"
        res += candidate["position"] + "<br>"
        res += candidate["skills"] + "<br><br>"
    return res

