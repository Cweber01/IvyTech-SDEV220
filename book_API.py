# M04 Working with API's
# Charles Weber SDEV220
# This code, when used in tandom with a venv, will support an api for a database of books ==-

from flask import flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

# creating an sqlite database in same directory titled 'data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://data.db'
db = SQLAlchemy(app)


class book(db.Model):
    id = db.Column(db.integer, primary_key=True, unique=True, nullable=False)
    book_title = db.Column(db.String(100), nullable=False)
    author_name = db.Column(db.String(100), nullable=False)
    publisher_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        # parameterized string
        return f'{self.id} - {self.book_title} - {self.author_name} - {self.publisher_name}'


@app.route('/')
def index():
    return 'Hello'


@app.route('/books')
def get_drinks():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'ID Number': book.id,
                     'Title': book.book_title,
                     'Author': book.author_name,
                     'Publisher': book.publisher_name
                     }

        output.append(book_data)

    # temp return
    return {'books', output}


# < ITEM > can define a parameter
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return ({'ID Number': book.id,
             'Title': book.book_title,
             'Author': book.author_name,
             'Publisher': book.publisher_name
            })

# adding/posting an object
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_title=request.json['name'],author_name=request.json['author'],publisher_name=request.json['publisher'])
    # Important to commit this to app
    db.session.add(book)
    db.session.commit()
    return {'id':book.id}


# deleting an object
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if drink is None:
        return ['error': 'not found']
    db.sessions.delete(drink)
    dbg.session.commit()
    return ['successfully added drink']