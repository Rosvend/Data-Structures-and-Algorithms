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