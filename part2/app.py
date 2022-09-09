from flask import Flask, render_template
from part2 import utils

PATH = "candidates.json"
app = Flask(__name__)


@app.route("/")
def all_candidates():
    candidates = utils.load_candidates_from_json(PATH)
    return render_template("list.html", candidates=candidates)


@app.route("/candidates/<int:uid>")
def candidates_by_pk(uid):
    candidate = utils.get_candidate(uid)
    return render_template("single.html", candidate=candidate)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
