import csv
import logging
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

# Inisialisasi logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Inisialisasi metadata
metadata = MetaData()

# Definisi tabel Sentiments
sentiments = Table(
    'sentiments', metadata,
    Column('sentiment_id', Integer, primary_key=True),
    Column('sentiment_label', String(20), unique=True)
)

# Definisi tabel Tweets
tweets = Table(
    'tweets', metadata,
    Column('id', Integer, primary_key=True),
    Column('text', String(280)),
    Column('sentiment_id', Integer, ForeignKey('sentiments.sentiment_id'))
)

# Manajer Database
class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        metadata.create_all(self.engine)
        logging.info("Tabel berhasil dibuat.")

    def insert_from_csv(self, csv_file):
        session = self.Session()
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    text = row.get('tweets', '').strip()
                    label = row.get('labels', '').strip()

                    if not text or not label:
                        logging.warning("Baris CSV dengan data kosong dilewati.")
                        continue

                    # Tetapkan sentiment_id berdasarkan label
                    if label == 'good':
                        sentiment_id = 2
                    elif label == 'bad':
                        sentiment_id = 3
                    else:
                        sentiment_id = 1  # Default ke netral

                    # Masukkan sentiment jika belum ada
                    existing_sentiment = session.execute(
                        sentiments.select().where(sentiments.c.sentiment_id == sentiment_id)
                    ).fetchone()
                    
                    if not existing_sentiment:
                        session.execute(
                            sentiments.insert().values(sentiment_id=sentiment_id, sentiment_label=label)
                        )
                        session.commit()

                    # Masukkan tweet
                    session.execute(
                        tweets.insert().values(text=text, sentiment_id=sentiment_id)
                    )
                    session.commit()
                    logging.info(f"Tweet '{text}' berhasil dimasukkan dengan sentiment '{label}'.")

        except Exception as e:
            logging.error(f"Terjadi kesalahan: {e}")
            session.rollback()
        finally:
            session.close()
            logging.info("Sesi database ditutup.")

if __name__ == "__main__":
    DB_USERNAME = 'root'
    DB_PASSWORD = ''
    DB_HOST = 'localhost'
    DB_NAME = 'db_sentiment_gpt'
    db_url = f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    
    db_manager = DatabaseManager(db_url)
    db_manager.create_tables()
    db_manager.insert_from_csv('data_source/data.csv')