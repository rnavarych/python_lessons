from flask import Flask, render_template, request, escape
from annotation import search4letters
from DBcm import UseDatabase

app = Flask(__name__)
app.config['dbConfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'tmm0gqgB1!',
                          'database': 'vsearchlogDB', }


def log_request(req: 'flask_request', res: str) -> None:
    with UseDatabase(app.config['dbConfig']) as cursor:
        _SQL = """insert into log
                      (phrase, letters, ip, browser_string, results)
                      values
                      (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res,))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results'
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results
                           )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to test page')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """DIsplay the contents of the log file as a HTML table."""
    with UseDatabase(app.config['dbConfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)
