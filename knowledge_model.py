from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__="topics to learn about"
	topic_id = Column(String,primary_key = True)
	wiki_link=Column(String)
	art_title = Column(String)
	rating= Column(Integer)
	def __repr__(self):
		return("art title: {}\n"
				"wiki_link : {}\n"
				"rating: {}").format(
					self.art_title,
					self.wiki_link,
					self.rating)
article_1=Knowledge(art_title="Quantom physics",
	wiki_link= "https://en.wikipedia.org/wiki/Quantum_mechanics",rating=7)
print(article_1)
		






		# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

