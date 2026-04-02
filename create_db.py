from app import app, db
from models import User, Student, Major
import datetime as dt
from werkzeug.security import generate_password_hash

with app.app_context():
    # 1. WIPE AND RECREATE THE DATABASE
    db.drop_all()
    db.create_all()
    print("Database wiped and recreated.")

    # 2. INITIAL LOADING OF USERS
    # Added MANAGER role to test your new /training route
    users = [
        {
            'username': 'khanh053',
            'email': 'khanh053@umd.edu',
            'first_name': 'Khanh',
            'last_name': 'Nguyen',
            'password': generate_password_hash('khanh053', method='pbkdf2:sha256'),
            'role': 'STUDENT'
        },
        {
            'username': 'admin',
            'email': 'admin@umd.edu',
            'first_name': 'Crystal',
            'last_name': 'Ball',
            'password': generate_password_hash('adminpw', method='pbkdf2:sha256'),
            'role': 'ADMIN'
        },
        {
            'username': 'manager',
            'email': 'manager@umd.edu',
            'first_name': 'Joe',
            'last_name': 'King',
            'password': generate_password_hash('managerpw', method='pbkdf2:sha256'),
            'role': 'MANAGER'
        }
    ]

    for u in users:
        print(f'{u["username"]} inserted into user')
        new_user = User(username=u['username'], email=u['email'], first_name=u['first_name'],
                        last_name=u['last_name'], password=u['password'], role=u['role'])
        db.session.add(new_user)
    db.session.commit()

    # 3. INITIAL LOADING OF MAJORS
    # Changed 'major_name' to 'major' to match the model definition
    majors_list = ["Accounting", "Finance", "Information Systems"]
    for m_name in majors_list:
        print(f'{m_name} inserted into major')
        new_major = Major(major=m_name)
        db.session.add(new_major)
    db.session.commit()

    # 4. ADD YOUR STUDENT RECORD
    print("Adding Khanh Nguyen to the Student table...")
    me_as_student = Student(
        first_name='Khanh',
        last_name='Nguyen',
        email='khanh053@umd.edu',
        major_id=3,
        birth_date=dt.date(2005, 3, 5),
        is_honors=False
    )
    db.session.add(me_as_student)
    db.session.commit()


    print("\n--- DATABASE RECREATED SUCCESSFULLY ---")