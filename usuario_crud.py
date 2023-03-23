import pymongo
client = pymongo.MongoClient("mongodb+srv://programa:o5ma5JcTMMNPbydk@cluster0.ephuxat.mongodb.net/?retryWrites=true&w=majority")
database = client.test
#print(db)

global db
db = client.mercadolivre

def createEndereco():
    rua =  input('Nome da rua: ')
    bairro = input('Nome do bairro: ')
    numero = input('Numero da residencia: ')
    complemento = input('Complemento (opcional): ')
    endereco = {
        "rua": rua,
        "bairro": bairro,
        "numero": numero,
        "complemento": complemento
    }
    return endereco

def updateEndereco(usuario):
    col = db.usuario
    enderecos = usuario["endereço"]
    print('''O que deseja fazer?
    1:  Atualizar endereço
    2:  Adicionar endereço
    3:  Deletar endereço''')
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        for index in range(len(enderecos)):
            print(str(index) + ':' + str(enderecos[index]))
        enderecoVelho = int(input('Escolha o endereço a atualizar: '))
        enderecoNovo = createEndereco()
        enderecos[enderecoVelho] = enderecoNovo
    elif escolha == '2':
        enderecoNovo = createEndereco()
        enderecos.append(enderecoNovo)
    elif escolha == '3':
        for index in range(len(enderecos)):
            print(str(index) + ':' + str(enderecos[index]))
        enderecos.pop(int(input('Escolha o endereço a deletar: ')))
    query = { "_id": usuario["_id"]}
    toUpdate = {"$set": { "endereço": enderecos}}
    col.update_one(query, toUpdate)



def insertUsuario():
    global db
    col = db.usuario
    nome = input('Nome do usuario: ')
    email = input('Email do usuario: ')
    cpf = input('Cpf do usuario: ')
    enderecos = []
    while True:
        enderecos.append(createEndereco())
        resposta = input('Quer adicionar outro endereço? (y/n) ')
        if resposta == 'n':
            break
    doc = {"nome": nome,
        "email": email,
        "cpf": cpf,
        'endereço': enderecos
        }
    x = col.insert_one(doc)
    print(x.inserted_id)

def sortUsuario():
    global db
    col = db.usuario
    docs = col.find().sort('nome')
    return docs

def updateUsuario():
    from compras_crud import search
    global db
    col = db.usuario
    usuarios = search(sortUsuario())
    usuario = usuarios[int(input("Escolha o usuario que deseja editar: "))]
    print('''O que deseja editar? 
    Nome
    Email
    Cpf
    Endereço
    Favoritos''')
    escolha = input("Escreva a sua opção: ").lower()
    if escolha == "endereço":
        updateEndereco(usuario)
    elif escolha == "favoritos":
        updateFavorito(usuario)
    else:
        valor = input("valor novo ")
        toUpdate = { "$set": { escolha: valor} }
        query = { "_id": usuario["_id"]}
        col.update_one(query, toUpdate)
    

def deleteUsuario():
    from compras_crud import search
    global db
    col = db.usuario
    usuarios = search(sortUsuario())
    escolha = int(input("usuario a deletar: "))
    usuario = usuarios[escolha]["_id"]
    query = { "_id": usuario }
    col.delete_one(query)

def updateFavorito(usuario):
    from compras_crud import search
    from produto_crud import sortProduto
    global db
    col = db.usuario
    favoritos = usuario["favoritos"]
    print('''O que deseja fazer?
    1:  Adicinar aos favoritos
    2:  Remover dos favoritos''')
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        print('aaaaa')
        produtos = search(sortProduto())
        favoritos.append(produtos[int(input("escolha o produto que quer adicionar: "))])
    elif escolha == '2':
        for index in range(len(favoritos)):
            print(str(index) + ':' + str(favoritos[index]))
        favoritos.pop(int(input("Escolha o produto para remover: ")))
    query = { "_id": usuario["_id"]}
    toUpdate = {"$set":{ "favoritos": favoritos}}
    col.update_one(query, toUpdate)




# insert()
#delete()
updateUsuario()