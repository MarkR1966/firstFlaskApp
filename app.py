from flask import Flask
from flask import render_template
app = Flask(__name__)

dummyData = [
    {
        "f_name": "Mark",
        "l_name": "Rafferty",
        "title": "Mr",
        "content": "Blah blah blah"
    },
    {
        "f_name": "Jim",
        "l_name": "Jones",
        "title": "Mr",
        "content": "More content"
    }
]

dummyContact = [
    {
        "branch": "Head Office",
        "address": "Manchester",
        "cont": "Mr James Brown",
        "tel": "123-456-789"
    },
    {
        "branch": "Sales Office",
        "address": "Glasgow",
        "cont": "Mr Steve Smith",
        "tel": "789-456-789"
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', title='Homepage', posts=dummyData)


@app.route('/about')
def about():
    return render_template('about.html', title='About', contacts=dummyContact)

@app.route('/another')
def another():
    return render_template('another.html', title='Another')

if __name__ == '__main__':
    app.run()