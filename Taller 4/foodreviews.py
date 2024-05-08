import csv
from collections import defaultdict
from datetime import datetime
from typing import List, Dict


class Review:
    def __init__(self, id, userID, productID, profileName, helpfulness_numerator, helpfulness_denominator, score, time, summary, text):
        self.id = id
        self.userID = userID
        self.productID = productID
        self.profileName = profileName
        self.helpfulness_numerator = int(helpfulness_numerator)
        self.helpfulness_denominator = int(helpfulness_denominator)
        self.score = int(score)
        self.time = int(time)
        self.summary = summary
        self.text = text

    def get_time(self):
        return datetime.utcfromtimestamp(self.time).strftime('%m/%d/%Y')

def read_file(filename: str) -> List[Review]:
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            reviews = []
            next(reader)  
            for row in reader:
                review = Review(*row)
                reviews.append(review)
        return reviews
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def puntajeTotal(reviews: List[Review]) -> Dict[str, int]:
    scores = defaultdict(int)
    for review in reviews:
        scores[review.productID] += review.score
    return dict(scores)

def listarTopM(puntajes: Dict[str, int], M: int) -> None:
    sorted_puntajes = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    
    top_m = sorted_puntajes[:M]
    
    for product_id, score in top_m:
        print(f"Product ID: {product_id}, Total Score: {score}")


filename = r"C:\Users\Sofia\OneDrive\Escritorio\Taller 4\Reviews.csv"
reviews = read_file(filename)

#puntuación total de cada producto como la suma de los puntajes (score) del producto
if reviews:
    result = puntajeTotal(reviews)
    print(result)

#obtener los Top-M productos a partir de la tabla de símbolos de puntajes
listarTopM(result, 5)