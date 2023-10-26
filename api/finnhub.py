import finnhub
import os
from dotenv import load_dotenv

load_dotenv()

class Stock_Data:
    def __init__(self):
    
        self.finnhub_client = finnhub.Client(api_key=os.getenv("FINNHUB_API_KEY"))

    def quote(self,symbol):
        return self.finnhub_client.quote(symbol)['c']
