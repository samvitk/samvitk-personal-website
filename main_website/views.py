from flask import Blueprint, render_template

EXPERIENCE = [
    {
        'company': 'Eightfold AI',
        'position': 'Software Engineering Intern',
        'location': 'Santa Clara, CA',
        'period': 'June 2024 - August 2024',
        'description_1': 'Computed and extracted 21 analytic metrics for Atlassian JIRA Tickets using distinct API Endpoints, implementing the logic into 3 distinct reports.',
        'description_2': "Determined accuracy metrics to enhance Eightfold AI's customer service.",
        'description_3': 'Automated the report to be delivered weekly as a company-wide email with an attached Excel report.'
    },
    {
        'company': 'WHS DECA',
        'position': 'Website Director',
        'location': 'Fremont, CA',
        'period': 'May 2023 - May 2024',
        'description_1': "Improved WHS DECA's website.",
        'description_2': 'Organized and managed chapter events with 200+ students.',
        'description_3': 'Provided assistance with WHS DECA events, informational workshops, and promotion.'    
    },
    {
        'company': 'ASDRP',
        'position': 'Research Intern',
        'location': 'Fremont, CA',
        'period': 'August 2023 - January 2024',
        'description_1': "Researched the applications of large-language models (LLMs) to detect satirical headlines in complex data sources.",
        'description_2': 'Collaborated with four researchers to design an algorithm using the OpenAI API.',
        'description_3': 'Refined the algorithm through iterative testing and adjustments.'    
    },
    {
        'company': 'HiveMind Center',
        'position': 'Python Class Instructor',
        'location': 'Fremont, CA',
        'period': 'January 2023 - April 2023',
        'description_1': "Started classes to teach students aged 8-12 fundamental programming skills with core Python concepts.",
        'description_2': 'Designed slideshows, activities, and a website as learning resources.',
        'description_3': 'Organized and graded assignments and final projects.'    
    }
]

PROJECTS = [
    {
        'title': 'Personal Website Development',
        'company': 'Self-Employed',
        'period': 'July 2024 - Aug 2024',
        'description': "Developed a personal website to showcase my portfolio and skills. Utilized modern web development technologies to create an engaging and responsive design. Implemented server-side logic using Flask and Python, and crafted the front-end with HTML, CSS, and JavaScript.",
        'skills': 'HTML, CSS, JavaScript, Flask, Python'
    }
]

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html", experience=EXPERIENCE, projects=PROJECTS)
