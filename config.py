# connects to the PostgreSQL database

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get('HOST')
database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')

conn = psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password)

cur = conn.cursor()
