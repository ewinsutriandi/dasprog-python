"""
Hanya untuk dijalankan sekali saja untuk menyiapkan database beserta tabel dan isinya
"""
import db

def inisialisasi_db():
    conn = db.get_conn()
    sql_create_menu = """
        CREATE TABLE MENU
        (
            id INTEGER PRIMARY KEY NOT NULL,
            nama TEXT NOT NULL,
            harga INTEGER NOT NULL,
            jenis TEXT NOT NULL 
        )
        """
    sql_create_tamu = """
        CREATE TABLE TAMU
        (
            id INTEGER PRIMARY KEY NOT NULL,
            meja TEXT NOT NULL,
            datang INTEGER timestamp DEFAULT CURRENT_TIMESTAMP,
            sdh_bayar INTEGER DEFAULT 0 
        )
        """
    sql_create_pesanan = """
        CREATE TABLE PESANAN
        (
            id INTEGER PRIMARY KEY NOT NULL,
            nama TEXT NOT NULL,
            harga INTEGER NOT NULL,
            jenis TEXT NOT NULL 
        )
        """
    conn.execute(sql_create_menu)
    conn.execute(sql_create_tamu)
    #conn.execute(sql_create_pesanan)
    conn.close()

def bersihkan_data_pesanan():
    sql_1 = """
        DELETE FROM TAMU 
    """
    sql_2 = """
        DELETE FROM PESANAN 
    """
    conn = db.get_conn()
    conn.execute(sql_2)
    conn.execute(sql_1)
    conn.commit()
    conn.close()

#inisialisasi_db()
#bersihkan_data_pesanan()