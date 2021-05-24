from flask import Flask, render_template, url_for, request

def ses4(sentence: str, word: str = 'aeiou') -> set:
    return set(word).intersection(set(sentence))


app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return render_template('start.html')


@app.route('/search4')
def do_search() -> str:
    return render_template('index.html')


@app.route('/entry')
def entry_page() -> str:
    return render_template('about.html',)


if __name__ == '__main__':
    app.run(debug='True')