from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)
CORS(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    courses = db.Column(db.String(255), nullable=False)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'], courses=','.join(data['courses']))
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully!'}), 201

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    output = [{
        'id': student.id,
        'name': student.name,
        'age': student.age,
        'courses': student.courses.split(',')
    } for student in students]
    return jsonify(output)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
