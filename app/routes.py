from flask import render_template
from app import app
from app.cluster_algo import cluster_articles, cluster_product_images


news_articles = [
    "Scientists Discover New Species of Butterfly in the Amazon Rainforest"
    "Government Announces New Policy to Tackle Climate Change",
    "Stock Market Hits Record High Amidst Economic Recovery",
    "COVID-19 Vaccine Rollout Expands to Include Adolescents",
    "Global Leaders Gather for Summit on Cybersecurity",
    "Study Finds Link Between Screen Time and Mental Health in Adolescents",
    "Wildfires Ravage California, Prompting Evacuations",
    "New Study Reveals Alarming Decline in Bee Populations",
    "NASA Rover Discovers Evidence of Ancient Life on Mars",
    "World Health Organization Declares End to Polio Outbreak in Africa"
]
images = [
    '/static/images/gym1.png',
    '/static/images/gym2.png',
    '/static/images/meme.png',
    '/static/images/sports1.png',
    '/static/images/sports2.png',
    '/static/images/students1.png',
    '/static/images/students2.png'
]
text_descriptions = [
    'exercising',
    'exercising',
    'funny',
    'football',
    'football',
    'education',
    'education'
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cluster/articles')
def cluster():
    # Perform clustering on the list of news articles
    clustered_data = cluster_articles(news_articles)

    # Pass clustered data to the template
    return render_template('results.html', clusters=clustered_data)

@app.route('/cluster/images')
def cluster_images():
    # Perform clustering on the list of news articles
    clustered_images = cluster_product_images(images, text_descriptions)

    # Pass clustered data to the template
    return render_template('results2.html', clustered_images=clustered_images)