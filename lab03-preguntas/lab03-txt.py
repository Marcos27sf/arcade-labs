from pathlib import Path
from main import jugar, extraer_preguntas

path = Path("preguntas.txt")

preguntas = []



with open(path, "r", encoding="utf-8") as file:
    for line in file:
        preguntas.append(extraer_preguntas(line.strip()))

jugar(preguntas)