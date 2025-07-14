from flask import render_template, Flask
from app import app 

@app.route('/')
@app.route('/home')
def index():
    my_details = {
            'name': 'Aryan Sharma',
            'college': 'KIET Group of Institutions',
            'year': 'final year',
            'school': 'Kendriya Vidyalaya'
        }

    sections = {
            'about': 'Hi, I am Aryan Sharma, looking for people to collaborate. '
                     'I am particularly interested in Research Internships.',
            'tech_stack': [
                'Machine Learning',
                'Deep Learning',
                'Convolutional Neural Network',
                'Computer Vision',
                'Image Processing',
                'Data Science'
            ]
        }

    projects = {
            'Cat vs Dog Telegram Bot Prediction': {
                'link': 'htk',
                'description': 'bla bla bla'
            }
        }

    return render_template("project.html")