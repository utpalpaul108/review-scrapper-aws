from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS, cross_origin
import requests, pymongo
from bs4 import BeautifulSoup
import logging

logging.basicConfig(filename="error_log.log", filemode="a", format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/search', methods=["POST"])
@cross_origin()
def search():
    if request.method == "POST":
        base_url = "https://www.flipkart.com/search?q="
        query = request.form.get("query")
        search_url = base_url + query.replace(" ", "%20")

        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        product_list = soup.find_all("div", {"class": "_1AtVbE col-12-12"})

        del product_list[0:2]

        product_url = "https://www.flipkart.com" + product_list[0].div.a["href"]

        # Single product reviews
        single_product = requests.get(product_url)
        single_product_soup = BeautifulSoup(single_product.content, "html.parser")
        product_reviews = single_product_soup.find_all("div", {"class": "_16PBlm"})

        del product_reviews[len(product_reviews) - 1]

        # Single product comment and rating
        customer_reviews = []
        for product_review in product_reviews:

            try:
                comment_heading = product_review.div.div.div.p.text
            except:
                comment_heading = "No comment heading"
                logging.info(comment_heading)

            try:
                comment_rating = product_review.div.div.div.div.text
            except:
                comment_rating = "No Rating"
                logging.info(comment_rating)

            try:
                commenter_name = product_review.select_one("div div:nth-of-type(3)").div.p.text
            except:
                commenter_name = "Anonymous"
                logging.info("No commenter name")

            try:
                comment = product_review.select_one("div div:nth-of-type(2)").div.div.div.text
            except:
                comment = ""
                logging.info("There is no comments")

            single_product_review = {"product": query, "name": commenter_name, "rating": comment_rating,
                                     "comment_head": comment_heading, "comment": comment}
            customer_reviews.append(single_product_review)

        logging.info("log my final result {}".format(customer_reviews))

        client = pymongo.MongoClient(
            "mongodb+srv://utpal108:utpal123@cluster0.ipcemmi.mongodb.net/?retryWrites=true&w=majority")
        db = client['flipcart_web_scrapping']
        db_collection = db['reviews']
        db_collection.insert_many(customer_reviews)

        return redirect(url_for('search_result'))

        # return render_template('search_result.html', reviews=customer_reviews[0:(len(customer_reviews)-1)])


@app.route('/search-result')
@cross_origin()
def search_result():
    client = pymongo.MongoClient(
        "mongodb+srv://utpal108:utpal123@cluster0.ipcemmi.mongodb.net/?retryWrites=true&w=majority")
    db = client['flipcart_web_scrapping']
    db_collection = db['reviews']
    reviews = db_collection.find()
    return render_template('search_result.html', reviews=reviews)


if __name__ == "__main__":
    app.run(debug=True)
