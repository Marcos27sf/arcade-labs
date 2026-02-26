from random import shuffle

def jugar(preguntas: list) -> None:
    puntos = 0
    letras = ["a", "b", "c", "d"]

    for pregunta in preguntas:
        shuffle(pregunta["opciones"])
        print(pregunta["pregunta"])

        for letra, opcion in zip(letras, pregunta["opciones"]):
            print(f"{letra}. {opcion}")
        
        eleccion_valida = False
        while not eleccion_valida:
            try:
                eleccion = input("Introduce tu respuesta: ").lower()
                index_eleccion = letras.index(eleccion)
                if pregunta["opciones"][index_eleccion] == pregunta["correcta"]:
                    puntos += 5
                eleccion_valida = True
            except:
                print("Opción no válida")
    
    print(f"La puntuación obtenida ha sido: {puntos}")

def extraer_preguntas(pregunta: str) -> dict:
    pregunta_segmentada = pregunta.split("|")
    pregunta_dict = {}

    pregunta_dict["pregunta"] = pregunta_segmentada[0]
    pregunta_dict["correcta"] = pregunta_segmentada[1]
    pregunta_dict["opciones"] = pregunta_segmentada[1:]
    
    return pregunta_dict