import pymongo
client = pymongo.MongoClient("mongodb+srv://programa:o5ma5JcTMMNPbydk@cluster0.ephuxat.mongodb.net/?retryWrites=true&w=majority")
database = client.test
#print(db)

global db
db = client.mercadolivre

def createEndereso():
    rua =  input('nome da rua ')
    bairro = input('nome do bairro ')
    numero = input('numero da residencia ')
    complemento = input('complemento (opcional) ')
    endereco = {
        "rua": rua,
        "bairro": bairro,
        "numero": numero,
        "complemento": complemento
    }
    return endereco
def insert():
    global db
    col = db.usuario
    nome = input('nome do usuario ')
    email = input('email do usuario ')
    cpf = input('cpf do usuario ')
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

insert()
#delete()
