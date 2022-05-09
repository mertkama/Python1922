# SQL Alchemy
# pip install SQLAlchemy
# pip install psycopg2

# Object Relation Management


from sqlalchemy import (
    create_engine,
    MetaData, Table, Column, Integer, String,
    )

from sqlalchemy.sql import text

# postgresql://kullanici_adi:şifre@sunucu_adresi:port/veritabani_adi
engine = create_engine("postgresql://mfwuaoxb:dzIg8R3uvXrH4XIFgdMb5p_1vjtCsIO4@tai.db.elephantsql.com:5432/mfwuaoxb",
                       echo=True)

meta = MetaData()

ogrenciler = Table(
        "ogrenciler", meta,
        Column('id', Integer, primary_key=True,
               autoincrement=True),
        Column('adi', String),
        Column('soyadi', String)
        )

meta.create_all(engine)


def ogrenciEkle(engine, ad, soyad):

    baglanti = engine.connect()
    ekle = ogrenciler.insert().values(adi=ad, soyadi=soyad)
    cikti = baglanti.execute(ekle)


# ogrenciEkle(engine, "Mehmet Nuri", "ÖZTÜRK")


baglanti = engine.connect()
#
# baglanti.execute(ogrenciler.insert(), [
#         {"adi": "ALi", "soyadi": "Kemal"},
#         {"adi": "Veli", "soyadi": "Orhan"}
#         ])


# Seçme

# s = ogrenciler.select()
# cikti =  baglanti.execute(s)
#
# cikti = list(cikti)
# print(cikti)


# Query(Sorgu) Yazma aql

# s  = text("select ogrenciler.adi, ogrenciler.soyadi from ogrenciler where  id = :id")
# n = baglanti.execute(s, id=3).fetchall()
#
# print(n)

# aralikli_sorgu = text("SELECT ogrenciler.adi, ogrenciler.soyadi FROM ogrenciler WHERE ogrenciler.id BETWEEN :x AND :y")
# aa = baglanti.execute(aralikli_sorgu, x=2, y=3).fetchall()
# print(aa)
#
# # Create Read Update Delete


#Update
# guncelleme = ogrenciler.update().where(ogrenciler.c.id == 3).values(adi="Can")
# baglanti.execute(guncelleme)

# DELETE
# silinecek = ogrenciler.delete().where(ogrenciler.c.id == 3)
# baglanti.execute(silinecek)


#Toplu Silme
silinecek = ogrenciler.delete().where(ogrenciler.c.id > 5)
baglanti.execute(silinecek)