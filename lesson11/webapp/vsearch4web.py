from flask import Flask, render_template, request, escape, session
from annotation import search4letters
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in

app = Flask(__name__)
app.secret_key = 'SuperSecretKeyByRaman'
app.config['dbConfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'tmm0gqgB1!2',
                          'database': 'vsearchlogDB', }


# def check_logged_in() -> bool:
#     if 'logged_in' in session:
#         return True
#     return False


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
    try:
        log_request(request, results)
    except Exception as err:
        print('***** Logging failed with this error:', str(err))
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
    try:
        """DIsplay the contents of the log file as a HTML table."""
        with UseDatabase(app.config['dbConfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents, )
    except ConnectionError as err:
        print('Is you database  switched on? Errors:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Errors:', str(err))
    except SQLError as err:
        print('Is your query correct? Errors:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'Error'


@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def getuser() -> str:
    return 'User value currently is set to: ' + session['user']


@app.route('/login')
def login():
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def logout():
    session.pop('logged_in')
    return 'You are now logged out.'


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page 1'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'This is page 2'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'This is page 3'


if __name__ == '__main__':
    app.run(debug=True)
