from pymongo import MongoClient
from decouple import config
from model import UsuarioModel, UsuarioAssinaturaModel
from datetime import datetime, timedelta
client = MongoClient(config('CONNECTED_DB'))
db = client['TELEGRAMLOJA']
collection = db['Usuarios']

class Usuario:
    def __init__(self):
        self.client = MongoClient(config('CONNECTED_DB'))
        self.db = self.client['TELEGRAMLOJA']
        self.collection = self.db['Usuarios']
        self.collection_payment = self.db['Pagamentos']
        self.collection_expirados = self.db['Expirados']
        self.collection_avisos = self.db['Avisos']
        self.collection_admins = self.db['AdminBOT']
    
    
    def cadastrar_usuario(self, usuario: dict):
        usuario_existe = self.usuario_existe(usuario['id'])
        if usuario_existe:
            print('Usuario já existe')
            return True
        else:
            self.collection.insert_one(usuario)
            print('Usuario cadastrado')
            return False
    
    
    def inserir_idioma(self, id, idioma):
        usuario = self.collection.find_one({'id': id})
        if usuario:
            self.collection.update_one({'id': id}, {'$set': {'idioma': idioma}})
            
    def qtd_start(self, id):
        usuario = self.collection.find_one({'id': id})
        if usuario:
            self.collection.update_one({'id': id}, {'$set': {'qtd_start': usuario['qtd_start'] + 1}})

    def get_qtd_start(self, id):
        usuario = self.collection.find_one({'id': id})
        if usuario:
            return usuario['qtd_start']
        else:
            return None
        
    def usuario_existe(self, id):
        usuario = self.collection.find_one({'id': id})
        if usuario:
            return True
        else:
            return False
    
    def buscar_usuario(self, id):
        usuario = self.collection.find_one({'id': id})
        return usuario
    
    def ver_idioma(self, id):
        usuario = self.collection.find_one({'id': id})
        if usuario:
            return usuario['idioma']
        
        else:
            return None
    def inserir_assinatura(self, assinatura: dict):
        
        self.collection_payment.insert_one(assinatura)
        print('assinatura inserida')
          
    
    
    
    def inserir_qt_assinatura(self, id):
        usuario = self.collection.find_one({'id': id})
        if usuario:
            usuario['qt_assinatura'] += 1
            self.collection.update_one({'id': id}, {'$set': {'qt_assinatura': usuario['qt_assinatura']}})
            print('Qt Assinatura atualizada')
            return True
        
    def qtd_assinatura(self, id):
        usuario = self.collection.find_one({'id': id})
        if usuario:
            return usuario['qt_assinatura']
    
    def existe_assinatura(self, id):
        usuario = self.collection.find_one({'id': id})
        if usuario:
            return True
        else:
            return False
    def delete_assinatura(self, id):
        self.collection_payment.delete_one({'id': id})
        print('assinatura excluida')


    def all_id_assinatura(self):
        assinaturas = self.collection_payment.find({}, {'id': 1, '_id': 0, 'criado': 1, 'expira': 1, 'idioma': 1})
        return assinaturas
    def get_user_id(self, username):
        user = self.collection.find_one({'username': username})
        if user:
            return user['id']
        else:
            return None
   
    def show_info_assinatura(self):
        qtd_usuarios = []
        qtd_testes = []
        valor_total = 0
        qtd_portugal = []
        qtd_espanha = []
        data = self.collection_payment.find({})
        for assinatura in data:
            if assinatura['idioma'] == 'portugues':
                qtd_portugal.append(assinatura['idioma'])
            elif assinatura['idioma'] == 'espanhol':
                qtd_espanha.append(assinatura['idioma'])
            
            elif assinatura['tipo'] == 'teste':
                qtd_testes.append(assinatura['tipo'])
            valor_total += assinatura['valor']
            qtd_usuarios.append(assinatura['id'])
        return{'qtd_usuarios': len(qtd_usuarios), 'qtd_testes': len(qtd_testes), 'qtd_portugal': len(qtd_portugal), 'qtd_espanha': len(qtd_espanha), 'valor_total': valor_total}
    
    def status_assinatura(self, id):
        assinatura = self.collection_payment.find_one({'id': id})
        if assinatura:
            criado = assinatura['criado']
            expira = assinatura['expira']
            return {'criado': criado, 'expira': expira}
        else:
            return None
    
    def insert_admin(self, id):
        self.collection_admins.insert_one({'id': id})
        print('admin inserido')
    
    def delete_admin(self, id):
        self.collection_admins.delete_one({'id': id})
        print('admin excluido')
    
    def get_admins(self):
        admins = self.collection_admins.find({})
        return admins
    def is_admin(self, id):
        admin = self.collection_admins.find_one({'id': id})
        if admin:
            return True
        else:
            return False

usuario = Usuario()
#usuario.insert_admin(str(7124703290))