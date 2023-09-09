#Aqui esta todo lo relacionado a guardar informacion bdd mango
import pymongo

class bddMongo:
    def __init__(self, server, puerto, usuario, contrasena, base):
        self.conect = pymongo.MongoClient(f'mongodb://{usuario}:{contrasena}@{server}:{puerto}/?authSource=admin&readPreference=primary&ssl=false&directConnection=true') 
        self.bdd = self.conect[base]

    def insertar(self, datos, coleccion):
        col = self.bdd[coleccion]
        col.insert_one(datos)
