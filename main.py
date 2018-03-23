from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/dataviz')
def data_viz():
    return render_template('a1-burtin.html')


if __name__ == '__main__':
    app.run()
