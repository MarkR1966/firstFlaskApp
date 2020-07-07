from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ

from forms import PostsForm

app = Flask(__name__)

#86.2.192.144


app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sup3rn0va01@34.89.36.49:3306/posts'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + \
                                        environ.get('MYSQL_USER') + \
                                        ':' + \
                                        environ.get('MYSQL_PASSWORD') + \
                                        '@' + \
                                        environ.get('MYSQL_HOST') + \
                                        ':' + \
                                        environ.get('MYSQL_PORT') + \
                                        '/' + \
                                        environ.get('MYSQL_DB_NAME')
db = SQLAlchemy(app)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return ''.join(
            [
                'Title: ' + self.title + '\n'
                'Name: ' + self.f_name + ' ' + self.l_name + '\n'
                'Content: ' + self.content
            ]
        )


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
    post_data = Posts.query.all()
    return render_template('homepage.html', title='Homepage', posts=post_data)


@app.route('/about')
def about():
    return render_template('about.html', title='About', contacts=dummyContact)

@app.route('/add')
def add():
    form = PostsForm()
    return render_template('post.html', title='Add a post', form=form)

@app.route('/another')
def another():
    return render_template('another.html', title='Another')

@app.route('/create')
def create():
    db.create_all()
    post = Posts(f_name='Mark', l_name='Rafferty', title='Mr.', content='Blah Blah Blah')
    post2 = Posts(f_name='Mark2', l_name='Rafferty2', title='Mr.', content='More content')
    db.session.add(post)
    db.session.add(post2)
    db.session.commit()
    return "Added table and populated some records"

@app.route('/delete')
def delete():
    #db.drop_all()  # drops all the schemas
    db.session.query(Posts).delete()  # deletes the contents of the table
    db.session.commit()
    return "everything is gone woops soz"


if __name__ == '__main__':
    app.run()