from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/qibla')
def qibla():
    return render_template('Qibla.html')

@app.route('/kidung')
def kidung():
    return render_template('Kidung.html')

if __name__ == '__main__':
    app.run(debug=True)