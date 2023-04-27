from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# create the database engine
engine = create_engine(f"""mysql+mysqldb://{settings.database_username}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}""")
# create a session factory
SessionLocal = sessionmaker(bind=engine)

# create the declarative base class
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
while True:
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="fastapi"
        )
        print("Connection to MySQL database was successful!")
        break
    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database: {}".format(error))
        time.sleep(3)

mycursor = mydb.cursor(dictionary=True)
"""
