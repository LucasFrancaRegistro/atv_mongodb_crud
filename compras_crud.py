import pymongo
import pickle
client = pymongo.MongoClient("mongodb+srv://programa:o5ma5JcTMMNPbydk@cluster0.ephuxat.mongodb.net/?retryWrites=true&w=majority")
database = client.test
import redis
conR = redis.Redis(host='redis-10721.c261.us-east-1-4.ec2.cloud.redislabs.com',
                  port=10721,
                  password='123senha')


global db
db = client.mercadolivre

def search(docs):
    objetos = []
    for obj in docs:
        objetos.append(obj)
    for obj_index in range(len(objetos)):
        print(str(obj_index) + ':  ' + str(objetos[obj_index]))
    return objetos

def searchNomes(docs):
    objetos = []
    for obj in docs:
        objetos.append(obj)
    for obj_index in range(len(objetos)):
        print(str(obj_index) + ':  ' + objetos[obj_index]['nome'])
    return objetos

def insertCompra():
    from produto_crud import sortProduto
    from usuario_crud import sortUsuario
    from vendedor_crud import sortVendedor
    global db
    col = db.compras
    data = input("Insira a data da compra: ")
    usuarios = searchNomes(sortUsuario())
    escolha = input("Usuario da compra: ")
    usuario = usuarios[int(escolha)]
    del usuario["favoritos"]
    produtos = searchNomes(sortProduto())
    escolha = input("Produto comprado: ")
    produto = produtos[int(escolha)]
    del produto["vendedor"]
    vendedores = searchNomes(sortVendedor())
    escolha = input("Vendedor do produto: ")
    vendedor = vendedores[int(escolha)]
    doc = {"data": data,
        "usuario": usuario,
        "produto": produto,
        "vendedor": vendedor}
    col.insert_one(doc)

def sortCompras():
    global db
    col = db.compras
    docs = col.find()
    return docs

def updateCompra():
    from produto_crud import sortProduto
    from usuario_crud import sortUsuario
    from vendedor_crud import sortVendedor
    global db
    col = db.compras
    compras = search(sortCompras())
    compra = compras[int(input("Escolha a compra que deseja editar: "))]
    print('''O que você deseja editar?
    Data
    Usuario
    Produto
    Vendedor''')
    escolha = input("Escreva sua opção: ").lower()
    if escolha == 'usuario':
        usuarios = search(sortUsuario())
        usuario = usuarios[int(input('Escolha o usuario que deseja atribuir a compra: '))]
        del usuario["favoritos"]
        valor = usuario
    elif escolha == 'produto':
        produtos = search(sortProduto())
        produto = produtos[int(input('Escolha o produto ue deseja atribuir a compra:'))]
        del produto["vendedor"]
        valor = produto
    elif escolha == 'produto':
        vendedores = search(sortVendedor())
        valor = vendedores[int(input('Escolha o vendedor ue deseja atribuir a compra:'))]
    toUpdate = { "$set": { escolha: valor} }
    query = { "_id": compra["_id"]}
    col.update_one(query, toUpdate)


def deleteCompra():
    global db
    col = db.compras
    compras = search(sortCompras())
    escolha = int(input("Compra a deletar: "))
    compra = compras[escolha]["_id"]
    query = { "_id": compra }
    col.delete_one(query)

def syncRedis():
    global db
    col = db.compras
    comprasMongo = sortCompras()
    if conR.exists("compras") > 0:
        comprasRedis = conR.lrange("teste", 0, -1)
        for compra in range(len(comprasMongo)):
            if conR.exists(comprasMongo[compra]["email"]) < 1:
                conR.set(comprasMongo[compra]["email"], pickle.dumps(comprasMongo[compra]))
                

    else:
        for compra in compras:
            conR.lpush("compras", pickle.dumps(compra))
    

#def syncMongo():

# for i in conR.lrange("teste", 0, -1):
#     print(i)
# conR.lpush("teste", "oi1")
# conR.lpush("teste", "oi2")
# print(conR.lrange("teste", 0, -1))
#insertCompra()
#search(sortUsuario())
#deleteCompra()
#updateCompra()