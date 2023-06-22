
from vsearch import search4letters
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/search4')
def search4() -> str:
    """Returns the results of a call to 'search4letters' to the browser."""
    return str(search4letters('life, the universe, and everything', 'xyz'))

@app.route('/entry')
def entry_page() -> 'html':
    """Returns the entry page to browser."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

app.run(debug=True)

