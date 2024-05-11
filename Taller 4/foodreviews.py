import csv
from collections import defaultdict
from datetime import datetime
from typing import List, Dict
from itertools import islice

class Review:
    def __init__(self, id, userID, productID, profileName, helpfulness_numerator, helpfulness_denominator, score, time, summary, text):
        self.id = id
        self.userID = userID
        self.productID = productID
        self.profileName = profileName
        self.helpfulness_numerator = helpfulness_numerator
        self.helpfulness_denominator = helpfulness_denominator
        self.score = int(score) if score is not None else 0
        self.time = int(time) if time is not None else 0
        self.summary = summary
        self.text = text

    def __str__(self):
        profileName_short = self.profileName[:30]
        summary_short = self.summary[:30]
        return f"{self.productID}: {profileName_short}, {self.score}, {summary_short}"

    @staticmethod
    def print_reviews(scores):
        limited_scores = islice(scores.items(), 30)
        for productID, details in limited_scores:
            print(f"Product ID: {productID}")
            print(f"Profile Name: {details['ProfileName'][:30]}")
            print(f"Total Score: {details['Score']}")
            print(f"Summary: {details['Summary'][:30]}\n")

def read_file(filename):
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            reviews = []
            next(reader)  # Skip header
            for row in reader:
                if row:
                    review = Review(*row)
                    reviews.append(review)
        return reviews
    except FileNotFoundError:
        print("The file was not found.") 
    except Exception as e:
        print(f"An error occurred: {e}")

def puntajeTotal(reviews: List[Review]) -> Dict[str, Dict[str, any]]:
    scores = defaultdict(lambda: {"ProfileName": None, "Score": 0, "Summary": None})
    for review in reviews:
        scores[review.productID]["ProfileName"] = review.profileName
        scores[review.productID]["Score"] += review.score
        scores[review.productID]["Summary"] = review.summary
    return scores

def listarTopM(puntajes: Dict[str, Dict[str, any]], M: int) -> None:
    sorted_puntajes = sorted(puntajes.items(), key=lambda x: x[1]['Score'], reverse=True)
    
    top_m = sorted_puntajes[:M]
    
    for product_id, details in top_m:
        print(f"Product ID: {product_id}, Total Score: {details['Score']}")

reviews = read_file(r"C:\Users\Sofia\OneDrive\Escritorio\Taller 4\Reviews.csv")

if reviews:
    result = puntajeTotal(reviews)
    Review.print_reviews(result)
    #obtener los Top-M productos a partir de la tabla de símbolos de puntajes
    listarTopM(result, 5)
