import uuid


class Comic:

    def __init__(self,nombre,autor,numero,*args):
        self.id_comic = uuid.uuid4()
        self.nombre = nombre
        self.autor = autor
        self.numero = numero

    def __str__(self):
        return f"{self.id_comic}--{self.nombre}--{self.autor}--{self.numero}"

    def __repr__(self):
        return f"\nId: {self.id_comic}\nNombre: {self.nombre}\nAutor: {self.autor}\nEditorial: {self.numero}" 