from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Curso:
    def __init__(self, id, titulo, aulas, horas, dia):
        self.id = id
        self.titulo = titulo
        self.aulas = aulas
        self.horas = horas
        self.dia = dia


curso1 = Curso(id=7, titulo="Intensivão de culinaria", aulas=4, horas=30, dia="Sábado")
curso2 = Curso(id=3, titulo="Aprendendo a desenvolver", aulas=60, horas=124, dia="Terça-feira")


print(curso1.id)  
print(curso1.titulo)  
print(curso1.aulas) 
print(curso1.horas)  
print(curso1.dia)  
