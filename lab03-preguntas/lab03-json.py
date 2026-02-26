from pathlib import Path
import json
from main import jugar

path = Path("preguntas.json")

preguntas = []

with open(path, "r", encoding="utf-8") as file:
    preguntas = json.load(file)

jugar(preguntas)