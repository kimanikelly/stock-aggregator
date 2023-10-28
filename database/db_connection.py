import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

aggregator_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD")
)
