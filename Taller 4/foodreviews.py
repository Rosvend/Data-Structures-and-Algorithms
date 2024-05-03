import csv
class Review:
    def __init__(self, id,userID,productID,profileName,helpfulness_numerator,helpfulness_denominator,score,time, summary, text):
        self.id = id
        self.userID = userID
        self.productID = productID
        self.profileName = profileName
        self.helpfulness_numerator = helpfulness_numerator
        self.helpfulness_denominator = helpfulness_denominator
        self.score = score
        self.time = time
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
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

reviews = read_file(r"C:\Users\royda\OneDrive\Documentos\Universidad\3. Tercer semestre\Estructuras de datos y algoritmos\Talleres\Taller 4\Reviews.csv")