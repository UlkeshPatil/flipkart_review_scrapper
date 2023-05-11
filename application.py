from src.mongo_db_connection import MongodbClient
from src.scrapper import FlipkartScraper
from src.logger import logger
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review" , methods = ['POST' , 'GET'])
def index():
    if request.method == 'POST':
        try:
            logger.info("Entered route /review of main.py")
            searchString = request.form['content'].replace(" ","")
            scrapper = FlipkartScraper(searchString)
            reviews = scrapper.scrape_reviews()
            mongo_db_connection = MongodbClient()
            logger.info("Connected to MongoDb")
            reviews_collection = mongo_db_connection.database["scrapped reviews"]
            reviews_collection.insert_many(reviews)
            logger.info("Added scrapped data in collection")
            return render_template('result.html', reviews=reviews[0:(len(reviews)-1)])
        
        except Exception as e:
            logger.error(e)

        else:
            return render_template('index.html')



if __name__=="__main__":
    app.run(host="0.0.0.0")
    