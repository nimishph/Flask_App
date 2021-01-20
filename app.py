from flask import Flask, render_template, request

from repos.exceptions import GithubApiException
from repos.api import repos_with_most_stars

app = Flask(__name__)

available_languages = ["Python", "JavaScript", "Ruby", "Java"]


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # code for a GET
        selected_languages = available_languages
        pass
    elif request.method == 'POST':
        # code for a POST
        selected_languages = request.form.getlist("languages")
        pass

    results = repos_with_most_stars(selected_languages)

    return render_template(
        'index.html',
        selected_languages=selected_languages,
        available_languages=available_languages,
        results=results)


@app.errorhandler(GithubApiException)
def handle_api_error(error):
    return render_templates('error.html', message=error)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080)
