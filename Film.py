from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text, select


connection_string = "postgresql://mfwuaoxb:dzIg8R3uvXrH4XIFgdMb5p_1vjtCsIO4@tai.db.elephantsql.com:5432/mfwuaoxb"
db = create_engine(connection_string, echo=True)

base = declarative_base()


class Film(base):
    __tablename__ = 'films'

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    director = Column(String)
    year = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# Create
#
# doctor_strange= Film(title="Doctor Strange", director="Scott Derricson", year="2016")
# session.add(doctor_strange)
# session.commit()

# Read

# films =  session.query(Film)
#
# for film in films:
#     print(film.title)
#     print(film.year)
#     print(film.director)


# Sorgulama
doctor_strange = session.query(Film).filter(Film.id == 1)

for dc in doctor_strange:
    print(dc.title)

#Update
doctor_strange = session.query(Film).filter(text("id = :value")).params(value=1).one()
doctor_strange.title = "Some 2016 Films"
session.commit()

#Delete
doctor_strange = session.query(Film).filter(text("id = :value")).params(value=1).one()
session.delete(doctor_strange)
session.commit()