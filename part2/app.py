from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route("/")
def all_candidates():
    candidates = utils.load_candidates_from_json()
    return render_template("list.html", candidates=candidates)


@app.route("/candidates/<int:uid>")
def candidates_by_pk(uid):
    candidate = utils.get_candidate(uid)
    if candidate == None:
        return render_template("404.html")
    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def search(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def search_by_skill(skill_name):
    candidates = utils.get_candidate_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates,
                           skill=skill_name, quantity=len(candidates))


if __name__ == '__main__':
    app.run(port=5001, debug=True)
