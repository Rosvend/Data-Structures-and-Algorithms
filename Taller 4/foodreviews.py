import csv
from collections import defaultdict
from datetime import datetime
from typing import List, Dict
class Review:
    def __init__(self, id,userID,productID,profileName,helpfulness_numerator,helpfulness_denominator,score,time, summary, text):
        self.id = id
        self.userID = userID
        self.productID = productID
        self.profileName = profileName
        self.helpfulness_numerator = helpfulness_numerator
        self.helpfulness_denominator = helpfulness_denominator
        self.score = int(score)  
        self.time = int(time)
        self.summary = summary
        self.text = text
    
    def get_time(self):
        return datetime.utcfromtimestamp(self.time).strftime('%m/%d/%Y')


def read_file(filename):
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
        print("The file was not found.") #hola
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
#Diccionario por fechas
def reviewsPorFecha(reviews: List[Review]) -> Dict[str, List[Review]]:
    reviews_por_fecha = defaultdict(list)
    for review in reviews:
        fecha = review.get_time()
        reviews_por_fecha[fecha].append(review)
    return reviews_por_fecha
def listarTopMPorRango(reviews: List[Review], fechaIni: datetime, fechaFin: datetime, M: int) -> None:
    # Agrupar las revisiones por fecha
    reviews_por_fecha = reviewsPorFecha(reviews)
    
    # Filtrar las revisiones dentro del rango de fechas especificado
    reviews_en_rango = [review for review in reviews if fechaIni <= datetime.utcfromtimestamp(review.time) <= fechaFin]
    
    # Calcular los puntajes totales dentro del rango de fechas
    puntajes_en_rango = puntajeTotal(reviews_en_rango)
    
    # Obtener los Top-M productos dentro del rango de fechas
    listarTopM(puntajes_en_rango, M)

reviews = read_file(r"C:\Users\USUARIO\Downloads\Reviews.txt")
#puntuación total de cada producto como la suma de los puntajes (score) del producto
if reviews:
    result = puntajeTotal(reviews)
    print(result)

#obtener los Top-M productos a partir de la tabla de símbolos de puntajes
    listarTopM(result, 5)
fecha_inicio = datetime.strptime("10/31/1999", "%m/%d/%Y")
fecha_fin = datetime.strptime("10/31/2012", "%m/%d/%Y")
listarTopMPorRango(reviews, fecha_inicio, fecha_fin, 5)
