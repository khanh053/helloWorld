import os
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Student, Major
from datetime import datetime as dt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'university.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'beyond_course_scope'
db.init_app(app)

@app.route('/')
@app.route('/student/view')
def student_view_all():
    students = Student.query.outerjoin(Major, Student.major_id == Major.major_id).add_entity(Major).all()
    return render_template('student_view_all.html', students=students)

@app.route('/student/create', methods=['GET', 'POST'])
def student_create():
    majors = Major.query.all()
    if request.method == 'POST':
        # MODIFICATION: Capture email from form
        new_student = Student(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email=request.form['email'],
            major_id=request.form['major_id'],
            birth_date=dt.strptime(request.form['birth_date'], '%Y-%m-%d'),
            is_honors=True if 'is_honors' in request.form else False
        )
        db.session.add(new_student)
        db.session.commit()
        flash(f'Student {new_student.first_name} added successfully!', 'success')
        return redirect(url_for('student_view_all'))
    return render_template('student_entry.html', action='create', majors=majors)

@app.route('/student/edit/<int:student_id>', methods=['GET', 'POST'])
def student_edit(student_id):
    student = Student.query.get(student_id)
    majors = Major.query.all()
    if request.method == 'POST' and student:
        # MODIFICATION: Update email
        student.first_name = request.form['first_name']
        student.last_name = request.form['last_name']
        student.email = request.form['email']
        student.major_id = request.form['major_id']
        student.birth_date = dt.strptime(request.form['birth_date'], '%Y-%m-%d')
        student.is_honors = True if 'is_honors' in request.form else False
        db.session.commit()
        flash(f'Student {student.first_name} updated!', 'success')
        return redirect(url_for('student_view_all'))
    return render_template('student_entry.html', student=student, action='update', majors=majors)

@app.route('/student/view/<int:student_id>')
def student_view(student_id):
    student = Student.query.get(student_id)
    return render_template('student_entry.html', student=student, action='view')



if __name__ == '__main__':
    app.run(debug=True, port=8000)