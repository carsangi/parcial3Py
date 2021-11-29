import uuid


class Revista:

    def __init__(self,nombre,autor,edicion,*args):
        self.id_revista = uuid.uuid4()
        self.nombre = nombre
        self.autor = autor
        self.edicion = edicion

    def __str__(self):
        return f"{self.id_revista}--{self.nombre}--{self.autor}--{self.edicion}"

    def __repr__(self):
        return f"\nId: {self.id_revista}\nNombre: {self.nombre}\nAutor: {self.autor}\nEdicion: {self.edicion}" 