import json
from typing import List, Dict

PATH = "candidates.json"


def load_candidates_from_json(path = PATH) -> List[dict]:
    """
    Return list of all candidates from json file
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_candidate(candidate_id: int) -> Dict | None:
    """
    Search candidate by id
    Return candidate dict
    """
    for candidate in load_candidates_from_json():
        if candidate["id"] == candidate_id:
            return candidate
    return None


def get_candidates_by_name(candidate_name: str) -> List:
    """
    Search candidate by name
    Return list with candidates
    """
    candidates_by_name = []
    for candidate in load_candidates_from_json():
        if candidate["name"].lower().split()[0] == candidate_name.lower():
            candidates_by_name.append(candidate)
    return candidates_by_name


def get_candidate_by_skill(skill: str) -> List:
    """
       Search candidate by skill
       Return list with candidates
       """
    candidate_by_skill_list = []
    for candidate in load_candidates_from_json():
        if skill in candidate["skills"].lower().split(", "):
            candidate_by_skill_list.append(candidate)
    return candidate_by_skill_list


