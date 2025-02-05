from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///polls.db'
db = SQLAlchemy(app)
CORS(app)

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)
    choice_text = db.Column(db.String(255), nullable=False)
    votes = db.Column(db.Integer, default=0)

@app.route('/polls', methods=['POST'])
def create_poll():
    data = request.get_json()
    poll = Poll(question=data['question'])
    db.session.add(poll)
    db.session.commit()
    for choice_text in data['choices']:
        choice = Choice(poll_id=poll.id, choice_text=choice_text)
        db.session.add(choice)
    db.session.commit()
    return jsonify({'message': 'Poll created successfully!'}), 201

@app.route('/polls', methods=['GET'])
def get_polls():
    polls = Poll.query.all()
    output = []
    for poll in polls:
        choices = Choice.query.filter_by(poll_id=poll.id).all()
        output.append({
            'id': poll.id,
            'question': poll.question,
            'choices': [{'id': c.id, 'text': c.choice_text, 'votes': c.votes} for c in choices]
        })
    return jsonify(output)

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    choice = Choice.query.get(data['choice_id'])
    if not choice:
        return jsonify({'error': 'Choice not found'}), 404
    choice.votes += 1
    db.session.commit()
    return jsonify({'message': 'Vote recorded successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
