import requests

def obtener_precio_bitcoin():
    try:
        respuesta = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        respuesta.raise_for_status()  # Generar una excepción para códigos de estado incorrectos
        datos = respuesta.json()
        precio_usd = datos["bpi"]["USD"]["rate_float"]
        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    try:
        n_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))
        precio_bitcoin = obtener_precio_bitcoin()

        if precio_bitcoin is not None:
            costo_total_usd = n_bitcoins * precio_bitcoin
            print(f"El costo actual de {n_bitcoins:.8f} Bitcoins es: ${costo_total_usd:,.4f}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()