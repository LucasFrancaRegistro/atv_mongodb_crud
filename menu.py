import pymongo
import compras_crud
import usuario_crud
import produto_crud
import vendedor_crud
client = pymongo.MongoClient("mongodb+srv://programa:o5ma5JcTMMNPbydk@cluster0.ephuxat.mongodb.net/?retryWrites=true&w=majority")
database = client.test

print('''Bem vindo ao central de banco de dados do Mercado Livre
use os numeros para escolher suas opções

no que deseja interagir?

1:  Usuarios
2:  Vendedores
3:  Produtos
4:  Compras''')

def usuarioCRUD():
    print('''O que deseja fazer?
    
    1:  Inserir usuario
    2:  Listar usuarios
    3:  Atualizar usuario
    4:  Deletar usuario''')

    switch( )