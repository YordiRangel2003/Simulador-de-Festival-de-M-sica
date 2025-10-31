class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f" 🙋🏻 Hola, soy {self.nombre}, interpreto música del género {self.genero}.")

    def actuar(self):
        print(f"{self.nombre} realiza una actuación genérica.")

    def despedirse(self):
        print(f"{self.nombre} se despide del público con una gran sonrisa.")


class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"🎤 {self.nombre} canta su éxito '{self.cancion_mas_popular}' con gran energía.")


class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f" 🎧 El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")


class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f" 🎸La banda {self.nombre}, con {self.integrantes} integrantes, toca un poderoso solo de guitarra.")


def iniciar_festival(lista_artistas):
    print("\n¡Comienza el Festival Musical! \n")
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("🎇Fin de la actuación.🎇\n")


    print("Artistas que participaron en el festival:")
    for artista in lista_artistas:
        print(f" - {artista.nombre}")
    print(f"Se presentaron {len(lista_artistas)} artistas en total. ¡Gracias por asistir al festival! \n")


def main():
    print("--------- FESTIVAL MUSICAL ---------")
    
    cantidad = int(input("¿Cuántos artistas se presentarán en el festival? "))
    while cantidad<=0:
        print("Debe ser al menos 1 artista.")
        cantidad = int(input("¿Cuántos artistas se presentarán en el festival? "))
            
            
    lista_artistas = []
    
    print("========= MENU DEL FESTIVAL========")
    print("+. Agregar Cantante")
    print("-. Agregar DJ")
    print("*. Agregar Banda")
    print("/. Iniciar Festival")
    print("E. Salir")

    while True:
        opcion = input("Seleccione una opción (+,-,*,/,E): ").upper()

        if opcion == "+":
            nombre = input("Nombre del artista: ")
            genero = input("Género musical: ")
            popularidad = int(input("Popularidad (1-100): "))
            cancion = input("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)
            lista_artistas.append(artista)
            print(f"{nombre} ha sido agregado al festival.\n")

        elif opcion == "-":
            nombre = input("Nombre del artista: ")
            genero = input("Género musical: ")
            popularidad = int(input("Popularidad (1-100): "))
            estilo = input("Estilo musical: ")
            artista = DJ(nombre, genero, popularidad, estilo)
            lista_artistas.append(artista)
            print(f"{nombre} ha sido agregado al festival.\n")

        elif opcion == "*":
            nombre = input("Nombre de la banda: ")
            genero = input("Género musical: ")
            popularidad = int(input("Popularidad (1-100): "))
            integrantes = int(input("Número de integrantes: "))
            artista = Banda(nombre, genero, popularidad, integrantes)
            lista_artistas.append(artista)
           
            print(f"{nombre} ha sido agregada al festival.\n")

        elif opcion == "/":
            if lista_artistas:
                iniciar_festival(lista_artistas)
            else:
                print("No hay artistas registrados aún.\n")

        elif opcion == "E":
            print("¡Gracias por usar el simulador del Festival Musical! ")
            break

        else:
            print("Opción no válida. Intente nuevamente.\n")


if __name__ == "__main__":
    main()
