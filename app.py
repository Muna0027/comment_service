from flask import Flask, jsonify, request

app = Flask(__name__)

comments = {
    '1': {'text': 'This is the first comment.'},
    '2': {'text': 'This is the second comment.'}
}

@app.route('/comment/<id>')
def get_comment(id):
    comment_info = comments.get(id, {})
    return jsonify(comment_info)

@app.route('/comment', methods=['POST'])
def create_comment():
    data = request.json
    new_id = str(len(comments) + 1)
    comments[new_id] = data
    return jsonify({'message': 'Comment created'})

@app.route('/comment/<id>', methods=['PUT'])
def update_comment(id):
    if id in comments:
        data = request.json
        comments[id] = data
        return jsonify({'message': 'Comment updated'})
    else:
        return jsonify({'error': 'Comment not found'})

@app.route('/comment/<id>', methods=['DELETE'])
def delete_comment(id):
    if id in comments:
        del comments[id]
        return jsonify({'message': 'Comment deleted'})
    else:
        return jsonify({'error': 'Comment not found'})

if __name__ == '__main__':
    app.run(port=5002)
