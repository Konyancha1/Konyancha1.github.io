from flask import render_template
from app import app
from app.cluster_algo import cluster_articles

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cluster')
def cluster():
    # Perform clustering on the list of news articles
    clustered_data = cluster_articles(news_articles)

    # Pass clustered data to the template
    return render_template('results.html', clusters=clustered_data)
