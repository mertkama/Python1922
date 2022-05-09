from sqlalchemy import (
    create_engine,
    MetaData, Table, Column, Integer, String, ForeignKey,
    )

from sqlalchemy.sql import text, select

engine = create_engine("postgresql://mfwuaoxb:dzIg8R3uvXrH4XIFgdMb5p_1vjtCsIO4@tai.db.elephantsql.com:5432/mfwuaoxb",
                       echo=True)

meta = MetaData()

calisanlar = Table(
        "calisanlar", meta,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("adi", String),
        Column("soyadi", String)
        )

adresler = Table(
        "adresler", meta,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("c_id", Integer, ForeignKey("calisanlar.id")),
        Column("il_adi", String),
        Column("ilce_adi", String),
        Column("acik_adres", String)
        )

meta.create_all(engine)

baglanti = engine.connect()

# calisan1 =  calisanlar.insert().values(adi= "Kemal", soyadi="UNAKITAN")
# baglanti.execute(calisan1)

# adres = adresler.insert().values(c_id=2, il_adi="Adana", ilce_adi="Ceyhan",
#                                  acik_adres="Karpuz Caddesi, Bicibici Mah. Kebap Sok. No:62")
#
# baglanti.execute(adres)

# calisan1 =  select([calisanlar,adresler]).where(calisanlar.c.id == adresler.c.c_id)
# calisan1 = baglanti.execute(calisan1)
#
# for i in calisan1:
#     print(i)

# calisanA = calisanlar.select().where(calisanlar.c.adi.startswith('A%'))
# calisanA = baglanti.execute(calisanA)
# print(list(calisanA))


print(calisanlar.join(adresler))
# CALISANLAR JOIN ADRESLER ON CALISANLAR.ID = ADRESLER.C_ID

j =  calisanlar.join(adresler,calisanlar.c.id == adresler.c.c_id)

sec =  select([calisanlar]).select_from(j)

cikti =  baglanti.execute(sec).fetchone()
print(cikti)