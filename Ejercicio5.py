import requests
import csv

def obtener_precio_bitcoin():
    try:
        respuesta = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        respuesta.raise_for_status()
        datos = respuesta.json()
        precio_usd = datos["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def guardar_en_txt(precio):
    with open("precio_bitcoin.txt", "w") as archivo:
        archivo.write(str(precio))

def guardar_en_csv(precio):
    with open("precio_bitcoin.csv", "w", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Fecha", "Precio USD"])
        escritor_csv.writerow([obtener_fecha_actual(), precio])

def obtener_fecha_actual():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    precio_bitcoin = obtener_precio_bitcoin()

    if precio_bitcoin is not None:
        guardar_en_txt(precio_bitcoin)
        guardar_en_csv(precio_bitcoin)

        print(f"Precio actual de Bitcoin: ${precio_bitcoin:.4f}")
        print("Datos guardados en precio_bitcoin.txt y precio_bitcoin.csv")

if __name__ == "__main__":
    main()