from pyfiglet import Figlet
import random

def obtener_fuente_aleatoria(fuentes_disponibles):
    return random.choice(fuentes_disponibles)

def main():
    figlet = Figlet()

    fuentes_disponibles = figlet.getFonts()
    print("Fuentes disponibles:", fuentes_disponibles)

    fuente_elegida = input("Ingrese el nombre de una fuente o presione Enter para una fuente aleatoria: ")
    if not fuente_elegida:
        fuente_elegida = obtener_fuente_aleatoria(fuentes_disponibles)
        print(f"Se eligió la fuente aleatoria: {fuente_elegida}")
    elif fuente_elegida not in fuentes_disponibles:
        print("La fuente ingresada no es válida.")
        return

    figlet.setFont(font=fuente_elegida)

    texto_imprimir = input("Ingrese el texto que desea mostrar: ")
    texto_figlet = figlet.renderText(texto_imprimir)
    print(texto_figlet)

if __name__ == "__main__":
    main()