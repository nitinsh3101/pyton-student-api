from flask import Flask, jsonify, request
from student import Student
from flask_cors import cross_origin
from flask_cors import CORS

app = Flask(__name__)
 
CORS(app)

students = [
    Student(1,"Suraj Soma"),
    Student(2,"Hemant Bhosale"),
    Student(3,"Rahul Pandey")
]


def to_serializable(val):
    if isinstance(val, Student):
        strStudent = {
            'sid': val.sid,
            'name': val.name
        }
        return strStudent

# @app.route("/", methods=['GET'])
# def getAllStudents():
#     studList=[]
#     for student in students:
#         studList.append(to_serializable(student))
#     return jsonify(studList)

@app.route("/api/v1/students", methods=['GET'])

def getAll():
    studList=[]
    for student in students:
        studList.append(to_serializable(student))
    return jsonify(studList)

@app.route("/api/v1/students/<int:sid>", methods=['GET'])
def get(sid):
    for student in students:
        if student.sid==sid:
            return jsonify(to_serializable(student))
    return 'student not found'
 
@app.route("/api/v1/students", methods=['POST'])
def add():
    tempStud=Student(int(request.form['sid']), request.form['name'])
    if any(stud.sid == int(request.form['sid']) for stud in students):
        return "student already exist"
    else:
        students.append(tempStud)

    studList=[]
    for student in students:
        studList.append(to_serializable(student))
    return jsonify(studList)


@app.route("/api/v1/students/<int:sid>/", methods=['PUT'])
def update(sid):
    tempStud=None
    for student in students:
        if student.sid==sid:
            tempStud=student

    if(tempStud!=None):
        students.remove(tempStud)
        students.append(Student(sid, request.form['name']))
    else:
        return "student not found"

    studList=[]
    for student in students:
        studList.append(to_serializable(student))
    return jsonify(studList)

@app.route("/api/v1/students/<int:sid>/", methods=['DELETE'])
def remove(sid):
    print(sid)
    tempStud=None
    for student in students:
        if student.sid==sid:
            tempStud=student

    if(tempStud!=None):
        students.remove(tempStud)
    else:
        return "student not found"

    studList=[]
    for student in students:
        studList.append(to_serializable(student))
    return jsonify(studList)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5050)