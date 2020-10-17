# Web programming final project questions and implementation 
Concordia University Soen 287 Final Take-Home Exam


## Flaskform Survey
Survey results are saved in a CSV file as shown below

<img width="400" alt="flaskform" src="https://user-images.githubusercontent.com/46803937/93269008-2f500480-f77c-11ea-8432-b6d602c54ef0.png">
<img width="400" alt="results" src="https://user-images.githubusercontent.com/46803937/93268761-c5375f80-f77b-11ea-8074-93c72050af10.png">



## Question 1
This question is about HTML, CSS, and Jinja2 template inheritance.
Do NOT use Bootstrap for this question.
Use only plain HTML and CSS.
No external CSS or JS files (included or downloaded from another server, except for examples provided in the course) are allowed.
All your CSS declarations have to be written the file static/exam.css.
Steps
Create an exam stylesheet (file static/exam.css) and use it to style the exam template (file templates/exam.html). Modify the exam template to include the exam stylesheet in the document head.
Transform, using CSS declarations written in the exam stylesheet, the unordered list in the exam template into a proper navigation bar (or menu). The menu should be vertical, and should be floating to the left.
Add an icon (a small image, saved inside the static folder) as the first menu item in your menu. This should work as the Home menu item, to go back to the web site home (route /).
Your menu should be styled this way:
the background should be lime green
the menu text should be black
the text should be 10% larger than the normal text size, using a fixed-width font
there should be a 2-pixel solid border, color Concordia red, with rounded corners around the whole menu (but not around or between individual menu items)
the menu items hover colors (text and background) should be different from the non-hover colors. You choose the colors you want here. The differences should be visible when viewing the page. Try to choose nice colors.
Modify the default colors and font for the whole web site. The default colors should not be same as for the menu, so you should have different CSS declarations for them.
Also modify the style of the code, em and strong elements to be different from the default style. The exact style is for you to decide here (but choose something that makes sense and doesn't make the site unreadable).
Modify the exam template to become the base template of the site, using the Jinja2 template syntax. There should be, at a minimum, blocks for the head and title elements. Also add a contents div, and a corresponding Jinja2 block for it. The menu should appear on all the pages.
Add some contents to the base template. Add the following to the contents block (the exact format is up to you):
Your name
Your email
Your web site title or topic (from your assignment 3)
A description of your web site (100 to 200 words approximately)
A screenshot of your web site (the main page or some other interesting page, your choice)
Modify the 4 question templates (templates/q1.html to templates/q4.html) to extend the exam template. The title and contents blocks should be redefined in the 4 question templates.
Modify the file app.py to add routes for the 4 question templates (templates/q1.html to templates/q4.html). Put your code where indicated in the TODO comments. The links to the questions in exam.html should work properly when running the application.
Add links to the previous and the next questions in each question. For example in question 2, there should be a link to question 1 and another link to question 3. In question 1, there should not be any previous question link, and in the last question, there should not be a next question link. These links should be added to the base template, not directly to each question page.

## Question 2
This question is about HTML forms and how to process them in Flask.
The Python part of your answer has to be written in the app.py file, in the proper places.
You will need to create a HTML template (file templates/survey.html), extending the exam template.
Steps
Create a FlaskForm for a survey in the file app.py.
The first field in your form should be an email input field (the person's email address who's filling the survey)
The second field should be a checkbox. If checked, the person's email address should be hidden in the results. Otherwise, the person's email address is recorded in the results.
The third field should be a date field (the person's date of birth).
Then there should be a radio button group, corresponding to the choices a, b, c, d of a multiple-choice question (MCQ). You have to write your own question with 4 choices.

Add the proper validators to your form. Each field should be mandatory except for the checkbox field. Make sure the email field contains a valid email address.
Create an endpoint for your survey form in the file app.py.
The route should be /survey, and it should accept both the GET and POST methods. It should follow the POST/REDIRECT/GET pattern
Method GET: displays the form
Method POST: save the survey results in a CSV file
Redirect to /survey/results on success (this endpoint has to be implemented in question 3)

## Question 3
Warning: You must have completed question 2 before attempting this question.
This question is about completing the /survey/results endpoint.
After successfully completing the form in question 2, users will be redirected to this endpoint.
The purpose of this endpoint is to display the survey results in a table by reading the data in the CSV file and generating the table with Jinja2 code.
You will need to create a HTML template (file templates/results.html), extending the exam template.
Steps
Open the CSV file containing the survey results, and read the data into a list or some other structure.
Render the templates/results.html template with the data read from the file.
Using Jinja2 code in the template, create a table to display the data read from the file.
Add another table in the template, containing the survey statistics:
the total number of survey submissions
the number of anonymous submissions (number of submissions with hidden email addresses)
the percentage of anonymous submissions
the number of answers for each choice of the MCQ (the number of a answers, the number of b answers, etc...)
the percentage for each choice of the MCQ
It is probably easier to calculate these statistics in the endpoint Python code, and then pass the calculated statistics to the template for displaying. The statistics table will always have the same structure (same number of rows and columns).
You should put the statistics table after the survey results table.


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the necessary packages. You can see which versions are required below. 

```bash
click            7.1.2
dnspython        2.0.0
email-validator  1.1.1
Flask            1.1.2
Flask-SQLAlchemy 2.4.4
Flask-WTF        0.14.3
idna             2.10
itsdangerous     1.1.0
Jinja2           2.11.2
MarkupSafe       1.1.1
pip              20.2.3
pybald-routes    2.11
repoze.lru       0.7
Routes           2.4.1
setuptools       50.3.0
six              1.15.0
SQLAlchemy       1.3.19
Werkzeug         1.0.1
WTForms          2.3.3
```

## Resources and credits 

```bash 
Python Installation
https://youtu.be/YYXdXT2l-Gg

Virtual Environment Setup pt 1
https://youtu.be/N5vscPTWKOk

Virtual Environment Setup pt 2
https://youtu.be/cY2NXB_Tqq0/
```

## Contributions
Suggestions and contributions are more than welcome.


## License
[MIT](https://choosealicense.com/licenses/mit/)
