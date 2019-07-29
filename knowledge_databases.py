from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(url,name,topic,rating):
    new_artical = Knowledge(url = url, name=name,topic=topic, rating=rating)
    session.add(new_artical)
    session.commit()

    #   art_title = art_title,
    #   wiki_link = wiki_link,
    #   rating = rating)
    #session.add(article_object)
    #session.commit()
add_article("www.google.com", "poteto", "food",3)

def query_all_articles():
        

def query_article_by_topic():


def delete_article_by_topic():


def delete_all_articles():


def edit_article_rating():
      
