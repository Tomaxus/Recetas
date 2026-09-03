from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField,ListField,StringField, IntField
class Ingrediente(EmbeddedDocument):
    nombre = StringField(required=True, max_length=100)
    cantidad = IntField(required=True, min_value=0)
    unidad = StringField(required=True, max_length=20)

class Origen(EmbeddedDocument):
    region = StringField(required=True, max_length=100)
    pais = StringField(required=True, max_length=100)

class Receta(Document):
    nombre = StringField(required=True, max_length=200)
    tipoCocina = StringField(required=True, max_length=100)
    tiempoPreparacion = StringField(required=True, max_length=50)
    ingredientes = ListField(EmbeddedDocumentField(Ingrediente))
    origen = EmbeddedDocumentField(Origen)

    meta = {'collection': 'recetas_examen'}

    def __str__(self):
        return self.nombre
