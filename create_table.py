from config import conn, cur
'''
Creates the tables needed. Run once.

Note: The script will drop all pre-existing tables and all data within if executed more than once.
'''

cur.execute('''
DROP TABLE IF EXISTS doctor;
DROP TABLE IF EXISTS facility;
DROP TABLE IF EXISTS lab;
DROP TABLE IF EXISTS patient;

CREATE TABLE doctor (
    id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    name TEXT,
    specialization TEXT,
    time TEXT,
    qualification TEXT,
    room_number TEXT
);

CREATE TABLE facility (
    id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE lab (
    id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    name TEXT UNIQUE,
    cost INTEGER
);

CREATE TABLE patient (
    id SERIAL NOT NULL PRIMARY KEY UNIQUE,
    name TEXT,
    disease TEXT,
    gender TEXT,
    age INTEGER
);
''')

conn.commit()
