from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Khanh Nguyen! This is my first code change'

@app.route('/hello')
def hello_world1():  # put application's code here
    return 'Hello World from Khanh Nguyen! This is my HTML'

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    # 1. Grab the data from the URL and save them to variables
    subject = request.args.get('subject')
    course_number = request.args.get('course_number')
    # 2. Print them to your console (optional, but helpful for debugging)
    print('Subject entered:', subject)
    print('Course number entered:', course_number)
    # 3. CRITICAL STEP: Pass those variables to the template!
    return render_template('favorite-course.html', subject=subject, course_number=course_number)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    # If the user is just visiting the page normally (GET)
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run()
