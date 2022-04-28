import psycopg2

from config import config


#
# def connect():
#     """Veritabanına bağlantı sağla"""
#
#     conn = None
#     try:
#         params = config()
#         print("Veritabanına bağlanıyorum...")
#
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#
#         cur.execute("SELECT version()")
#         db_version = cur.fetchone()
#         print(f"Postgresql versiyonu: {db_version}")
#
#         conn.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print("Veritabanı bağlantısı kapatıldı")
#
#
# if __name__ == '__main__':
#     connect()

#
# def create_tables():
#     commands = (
#             """
#             CREATE TABLE vendors(
#                 vendor_id SERIAL PRIMARY  KEY,
#                 vendor_name  VARCHAR  not null
#             )
#             """,
#
#             """
#                 CREATE TABLE parts(
#                     part_id  SERIAL PRIMARY  KEY ,
#                     part_name  VARCHAR NOT NULL
#                 )
#             """
#             )
#
#     conn = None
#     try:
#         params = config()
#         print("Veritabanına bağlanıyorum...")
#
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#
#         for command in commands:
#             cur.execute(command)
#
#         conn.commit()
#         conn.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print("Veritabanı bağlantısı kapatıldı")
#
#
# if __name__ == '__main__':
#     create_tables()


# Ekleme işlemi
# def insert_accounts(user_name, password, email):
#     sql = """
#           INSERT INTO  accounts(user_name, password, email, created_on, last_login)
#         VALUES (%s, %s, %s, current_timestamp, current_timestamp ) RETURNING user_id ;
#     """
#
#     conn = None
#     user_id = None
#
#     try:
#         params = config()
#         print("Veritabanına bağlanıyorum...")
#
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#
#         cur.execute(sql,(user_name, password, email))
#         user_id =  cur.fetchone()[0]
#
#         print(f"Kullanıcı ID: {user_id}")
#         conn.commit()
#         conn.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print("Veritabanı bağlantısı kapatıldı")
# #
# insert_accounts(user_name="kenan_coskun", password="Bla bla", email="kenan@coskun.com")


def insert_account_list(accountlist):
    sql = """
          INSERT INTO  accounts(user_name, password, email, created_on, last_login)
        VALUES (%s, %s, %s, current_timestamp, current_timestamp ) ;
    """

    conn = None
    user_id = None

    try:
        params = config()
        print("Veritabanına bağlanıyorum...")

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, accountlist)

        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Veritabanı bağlantısı kapatıldı")


#
insert_account_list(

        [
                ('abuzer_kadayif', 'abuzer', 'abuzer@kadayif.com'),
                ('hakan_eryaman', 'abuzer', 'hakan@kadayif.com'),
                ('halil_gunes', 'abuzer', 'halil@kadayif.com'),
                ('muammer_xx', 'abuzer', 'muammer@kadayif.com')

                ]

        )
