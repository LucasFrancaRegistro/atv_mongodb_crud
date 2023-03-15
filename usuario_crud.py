import pymongo
client = pymongo.MongoClient("mongodb+srv://programa:o5ma5JcTMMNPbydk@cluster0.ephuxat.mongodb.net/?retryWrites=true&w=majority")
database = client.test
#print(db)

global db
db = client.mercadolivre

def insert(nome, email, cpf):
    global db
    col = db.usuario
    doc = {"nome": nome, "email": email, "cpf": cpf}
    x = col.insert_one(doc)
    print(x.inserted_id)

#insert('alison', 'alison@gmail', '90252530809')

def sort():
    global db
    col = db.usuario
    doc = col.find().sort('nome')
    for x in doc:
        print(x)

def update():
    global db
    col = db.usuario
    query = { "nome": input("nome do usuario a editar")}
    campo = input("campo para editar ")
    valor = input("valor novo ")
    toUpdate = { "$set": { campo: valor} }
    col.update_one(query, toUpdate)
    

def delete():
    global db
    col = db.usuario
    query = { "nome": input("nome do usuario a deletar ")}
    col.delete_one(query)

delete()
