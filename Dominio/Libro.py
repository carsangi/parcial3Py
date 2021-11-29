import uuid


class Libro:

    def __init__(self,nombre,autor,editorial,*args):
        self.id_libro = uuid.uuid4()
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
    
    def __str__(self):
        return f"{self.id_libro}--{self.nombre}--{self.autor}--{self.editorial}"

    def __repr__(self):
        return f"\nId: {self.id_libro}\nNombre: {self.nombre}\nAutor: {self.autor}\nEditorial: {self.editorial}" 