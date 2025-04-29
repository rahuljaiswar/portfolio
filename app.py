from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', skills=data.skills, projects=data.projects, certificates=data.certificates)

if __name__ == '__main__':
    app.run(debug=True)
