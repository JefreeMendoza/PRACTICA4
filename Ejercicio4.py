class TablaMultiplicar:
    def guardar_tabla(self, n):
        with open(f"tabla-{n}.txt", "w") as file:
            for i in range(1, 11):
                file.write(f"{n} x {i} = {n * i}\n")
        print(f"Tabla de multiplicar del {n} guardada en tabla-{n}.txt")

    def mostrar_tabla(self, n):
        try:
            with open(f"tabla-{n}.txt", "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"El archivo tabla-{n}.txt no existe.")

    def mostrar_linea(self, n, m):
        try:
            with open(f"tabla-{n}.txt", "r") as file:
                lines = file.readlines()
                if 1 <= m <= 10:
                    print(lines[m - 1].strip())
                else:
                    print("El número de línea debe estar entre 1 y 10.")
        except FileNotFoundError:
            print(f"El archivo tabla-{n}.txt no existe.")

def main():
    tabla = TablaMultiplicar()

    while True:
        print("\n1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            num = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= num <= 10:
                tabla.guardar_tabla(num)
            else:
                print("El número debe estar entre 1 y 10.")
        elif choice == "2":
            num = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= num <= 10:
                tabla.mostrar_tabla(num)
            else:
                print("El número debe estar entre 1 y 10.")
        elif choice == "3":
            num = int(input("Ingrese un número entre 1 y 10: "))
            line = int(input("Ingrese el número de línea (1-10): "))
            if 1 <= num <= 10:
                tabla.mostrar_linea(num, line)
            else:
                print("El número debe estar entre 1 y 10.")
        elif choice == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
