from flask import Flask, jsonify, request

app = Flask(__name__)

books = []

@app.route('/book', methods=['POST'])
def add_book():
    book = request.get_json()
    books.append(book)
    return jsonify(book), 201

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/book/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    book.update(data)
    return jsonify(book)

@app.route('/book/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [b for b in books if b['id'] != id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
