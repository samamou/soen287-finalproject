# SOEN287 Web Programming Take-Home Final Exam
# Winter 2020
import pandas
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Email, InputRequired
from flask import Flask, render_template, redirect, url_for, request
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
csrf = CSRFProtect(app)


# TODO: Question 2: Survey FlaskForm
# Write your survey FlaskForm starting on the next line
class Survey(FlaskForm):
    email = StringField(label='Email Address', validators=[DataRequired(), Email()])
    checkbox = BooleanField(label='Do you wish to hide your email address?')
    date = StringField(label='Date of Birth', validators=[InputRequired()])
    radio = RadioField(label='How are you feeling today?',
                       choices=[('a', 'Horrible'), ('b', 'Bad'), ('c', 'Good'), ('d', 'Great!')])
    submit = SubmitField('Submit')

# end of your survey FlaskForm


@app.route('/')
def exam():
    return render_template('exam.html')


# TODO: Question 1: questions endpoints
# Routes for the 4 questions templates starting on the next line
@app.route("/q1")
def q1():
    return render_template('q1.html', title='q1')


@app.route("/q2")
def q2():
    return render_template('q2.html', title='q2')


@app.route("/q3")
def q3():
    return render_template('q3.html', title='q3')


@app.route("/q4")
def q4():
    return render_template('q4.html', title='q4')


# End of the 4 questions templates


# TODO: Question 2: Survey Endpoint
# Write your survey endpoint starting on the next line
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    form = Survey()
    if form.is_submitted():
        with open('data/survey.csv', 'w') as f:
            fieldnames = ['Email', 'Checkbox value', 'Birth Month', 'MCQ']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            if form.checkbox.data:
                writer.writerow({'Email': 'null', 'Checkbox value': form.checkbox.data,
                                 'Birth Month': form.date.data, 'MCQ': form.radio.data})
            else:
                writer.writerow({'Email': form.email.data, 'Checkbox value': form.checkbox.data,
                                 'Birth Month': form.date.data, 'MCQ': form.radio.data})
        return redirect(url_for('results'))
    return render_template('survey.html', form=form)

# end of your survey endpoint


# TODO: Question 3: Survey Results Endpoint
# Write your survey results endpoint starting on the next line
@app.route('/results')
def results():
    table = pandas.read_csv('data/survey.csv')
    print(table)
    # import csv as pandas.Dataframe
    return render_template('results.html', data=list(table))

# end of your survey results endpoint


# TODO: Question 4: JavaScript and regular expressions
# Write your postal codes endpoint starting on the next line

# end of your postal codes endpoint

if __name__ == '__main__':
    app.run()
