import sqlite3
from models import Menu,Tamu,Pesanan

def get_conn():
    conn = sqlite3.connect('warung_makan.db')
    return conn

def create_menu(nama,jenis,harga):
    sql = """
        INSERT INTO MENU (nama,jenis,harga) VALUES (?,?,?) 
    """
    conn = get_conn()
    cursor = conn .cursor()
    cursor.execute(sql,[nama,jenis,harga])
    conn.commit()
    conn.close()

def menu_by_id(id):
    sql = """
        SELECT id,nama,jenis,harga from MENU where id = ?
    """
    conn = get_conn()
    cursor = conn .cursor()
    cursor.execute(sql,[id])
    row = cursor.fetchone()
    mn = None
    if row:
        mn = Menu(row[1],row[2],row[3],row[0])
    conn.close()
    return mn

def list_menu_by_jenis(jenis):
    sql = """
        SELECT id,nama,jenis,harga from MENU where jenis = ?
    """
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(sql,[jenis])
    rows = cursor.fetchall()
    daftar_menu = []
    for row in rows:
        mn = Menu(row[1],row[2],row[3],row[0])
        daftar_menu.append(mn)
    conn.close()
    return daftar_menu

def create_tamu(meja):
    sql = """
        INSERT INTO TAMU (meja) VALUES (?) 
    """
    conn = get_conn()
    cursor = conn .cursor()
    cursor.execute(sql,[meja])
    tamu_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return tamu_id

def create_pesanan(pesanan):
    sql = """
        INSERT INTO PESANAN (tamu_id,nama,jenis,harga,jumlah) VALUES (?,?,?,?,?) 
    """
    conn = get_conn()
    cursor = conn .cursor()
    params= [pesanan.tamu_id,pesanan.menu.nama,pesanan.menu.jenis,pesanan.menu.harga,pesanan.jumlah]
    print("params:",params)
    cursor.execute(sql,params)
    conn.commit()
    conn.close()
