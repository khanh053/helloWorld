from app import app, db
from models import Student, Major
import datetime as dt

with app.app_context():
    db.drop_all()
    db.create_all()

    majors = ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management', \
              'Operations Management & Business Analytics', 'Supply Chain Management']
    for each_major in majors:
        a_major = Major(major=each_major)
        db.session.add(a_major)
    db.session.commit()

    # MODIFICATION: Added 'email' to initial student data
    students = [
        {'first_name': 'Robert', 'last_name':'Smith', 'email': 'rsmith@umd.edu', 'major_id':3,
            'birth_date': dt.datetime(2007, 6, 1), 'is_honors':1},
        {'first_name': 'Leo', 'last_name': 'Van Munching', 'email': 'leo.vm@umd.edu', 'major_id':6,
         'birth_date': dt.datetime(2008, 3, 24), 'is_honors': 0},
    ]

    for s in students:
        a_student = Student(first_name=s['first_name'], last_name=s['last_name'], email=s['email'],
                            major_id=s['major_id'], birth_date=s['birth_date'], is_honors=s['is_honors'])
        db.session.add(a_student)
    db.session.commit()
    print("Database re-created with email fields successfully!")