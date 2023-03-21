import pymongo
from produto_crud import sortProduto
from usuario_crud import sortUsuario
from vendedor_crud import sortVendedor
client = pymongo.MongoClient("mongodb+srv://programa:o5ma5JcTMMNPbydk@cluster0.ephuxat.mongodb.net/?retryWrites=true&w=majority")
database = client.test
#print(db)

global db
db = client.mercadolivre


def search(docs):
    objetos = []
    for obj in docs:
        objetos.append(obj)
    for obj_index in range(len(objetos)):
        print(str(obj_index) + ':  ' + str(objetos[obj_index]))
    escolha = int(input("Compra a deletar: "))
    objeto = objetos[escolha]["_id"]
    query = { "_id": objeto }
    return query

def searchNomes(docs):
    objetos = []
    for obj in docs:
        objetos.append(obj)
    for obj_index in range(len(objetos)):
        print(str(obj_index) + ':  ' + objetos[obj_index]['nome'])
    return objetos

def insertCompra():
    global db
    col = db.compras
    data = input("Insira a data da compra: ")
    usuarios = searchNomes(sortUsuario())
    escolha = input("Usuario da compra: ")
    usuario = usuarios[int(escolha)]
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
    global db
    col = db.compras
    query = search(sortCompras())
    print('''O que você deseja editar?
    1:  data.
    2:  usuario.
    3:  produto.
    4:  vendedor.''')
    pass


def deleteCompra():
    global db
    col = db.compras
    query = search(sortCompras())
    col.delete_one(query)

#insertCompra()
#search(sortUsuario())
#deleteCompra()