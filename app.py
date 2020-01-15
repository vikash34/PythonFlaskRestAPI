from flask import Flask, jsonify, request

app = Flask(__name__)

books = [{
            'name':'Data Structure',
            'Price':200.60,
            'bookNo':6665462
        },{
            'name':'Operating System',
            'Price':160.60,
            'bookNo':7687665
            
        },{
            'name':'Software Engineering',
            'Price':170.60,
            'bookNo':9898989
            
        }]

#index page content 
@app.route('/')
def hello():
    return "hello"

#get api for show books
@app.route('/books')
def get_books():
    return jsonify({'books':books})

#get api for single books
@app.route('/books/<int:bookNo>')
def get_book_by_id(bookNo):
    for book in books:
        if book["bookNo"]==bookNo:
            return_value = {
                'name':book["name"],
                'Price':book["Price"],
                'bookNo':book["bookNo"]
                }
    return jsonify({'book':return_value})

#post api for add new book
@app.route('/add_book',methods=['POST'])
def add_book():
     newBook= request.get_json()
     books.insert(0,newBook)
     return jsonify({'books':books})

#put api for update book
@app.route('/update_book/<int:bookNo>',methods=['PUT'])
def update_book(bookNo):
     requested_data = request.get_json()
     for book in books:
        if book["bookNo"]== bookNo:
            book["name"]=requested_data['name']
            book["Price"]=requested_data['Price']

     return jsonify({'books':books})


#put api for delete book
@app.route('/delete_book/<int:bookNo>',methods=['DELETE'])
def delete_book(bookNo):
     i=0
     for book in books:
        if book["bookNo"]== bookNo:
           books.pop(i)
        i +=1

     return jsonify({'books':books})


app.run(port=5050)