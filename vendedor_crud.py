import pymongo
from usuario_crud import createEndereso
client = pymongo.MongoClient("mongodb+srv://programa:o5ma5JcTMMNPbydk@cluster0.ephuxat.mongodb.net/?retryWrites=true&w=majority")
database = client.test
#print(db)

global db
db = client.mercadolivre

def insertVendedor():
    global db
    col = db.vendedor
    nome = input('nome do vendedor: ')
    email = input('email do vendedor: ')
    cpf = input('cpf do vendedor: ')
    enderecos = []
    while True:
        enderecos.append(createEndereso())
        resposta = input('quer adicionar outro endereço? (y/n) ')
        if resposta == 'n':
            break
    doc = {"nome": nome,
        "email": email,
        "cpf": cpf,
        'endereço': enderecos
        }
    x = col.insert_one(doc)
    print(x.inserted_id)

def sortVendedor():
    global db
    col = db.vendedor
    docs = col.find().sort('nome')
    return docs

def updateVendedor():
    global db
    col = db.vendedor
    query = { "nome": input("nome do vendedor a editar")}
    campo = input("campo para editar ")
    valor = input("valor novo ")
    toUpdate = { "$set": { campo: valor} }
    col.update_one(query, toUpdate)

def deleteVendedor():
    global db
    col = db.vendedor
    query = { "nome": input("nome do vendedor a deletar ")}
    col.delete_one(query)

#deleteVendedor()
#insertVendedor()