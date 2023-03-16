import pymongo
from usuario_crud import createEndereso
client = pymongo.MongoClient("mongodb+srv://programa:o5ma5JcTMMNPbydk@cluster0.ephuxat.mongodb.net/?retryWrites=true&w=majority")
database = client.test
#print(db)

global db
db = client.mercadolivre

def insertProduto():
    global db
    col = db.vendedor
    nome = input('nome do produto: ')
    quantidade = int(input('quantidade de produtos: '))
    preco = int(input('preço do produto: '))
    foto = input('link da foto do produto: ')
    doc = {"nome": nome,
        "quantidade": quantidade,
        "preço": preco,
        "foto": foto}
    col.insert_one(doc)

def sortProduto():
    global db
    col = db.produtos
    doc = col.find().sort('nome')
    for x in doc:
        print(x)
