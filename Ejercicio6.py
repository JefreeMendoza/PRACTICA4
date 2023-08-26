import requests
import sqlite3
import time

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        precio_usd = data["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def crear_tabla(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bitcoin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            precio_usd REAL,
            precio_gbp REAL,
            precio_eur REAL
        )
    ''')
    conn.commit()

def insertar_registro(conn, fecha, precio_usd, precio_gbp, precio_eur):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur)
        VALUES (?, ?, ?, ?)
    ''', (fecha, precio_usd, precio_gbp, precio_eur))
    conn.commit()

def main():
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        conn = sqlite3.connect("cryptos.db")
        crear_tabla(conn)

        fecha_actual = time.strftime("%Y-%m-%d %H:%M:%S")
        insertar_registro(conn, fecha_actual, precio_bitcoin, None, None)

        print("Registro insertado en la base de datos.")
        conn.close()

if __name__ == "__main__":
    main()
