import pymongo
from datetime import date
from produto_crud import sortProduto
from usuario_crud import sortUsuario
from vendedor_crud import sortVendedor
client = pymongo.MongoClient("mongodb+srv://programa:o5ma5JcTMMNPbydk@cluster0.ephuxat.mongodb.net/?retryWrites=true&w=majority")
database = client.test
#print(db)

global db
db = client.mercadolivre

def search(function):
    docs = function
    objetos = []
    for obj in objetos:
        objetos.append(obj)
    for obj_index in range(len(objetos)):
        print(str(obj_index) + ':  ' + objetos[obj_index]['nome'])

def insertCompra():
    global db
    col = db.compras
    data = date.today()
    search(sortUsuario())

#insertCompra()
search(sortProduto())