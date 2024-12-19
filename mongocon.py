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




    def show_info_assinantes(self, id=None):
        if id:
            assinante = self.collection_payment.find_one({'id': id})  # find_one retorna um único documento
            if assinante:
                return [{
                    'id': assinante.get('id'),
                    'nome': assinante.get('nome'),
                    'username': assinante.get('username'),
                    'idioma': assinante.get('idioma'),
                    'tipo': assinante.get('tipo'),
                    'criacao': assinante.get('criado'),
                    'expiracao': assinante.get('expira'),
                }]
            return []  # Retorne uma lista vazia se nenhum assinante for encontrado
        else:
            assinantes = self.collection_payment.find({})  # find retorna um cursor
            lista_assinantes = []
            for assinante in assinantes:
                lista_assinantes.append({
                    'id': assinante.get('id'),
                    'nome': assinante.get('nome'),
                    'username': assinante.get('username'),
                    'idioma': assinante.get('idioma'),
                    'tipo': assinante.get('tipo'),
                    'criacao': assinante.get('criado'),
                    'expiracao': assinante.get('expira'),
                })
            return lista_assinantes
    
    def delete_assinatura(self, id):
        try:
           # mudar a data de expiração para o dia atual
            self.collection_payment.update_one({'id': id}, {'$set': {'expira': datetime.utcnow()}})

            return True
        except:
            return False
    def extender_assinatura(self, id, dias):
        from datetime import datetime, timedelta
        
        # Busca o assinante pelo ID
        assinante = self.collection_payment.find_one({'id': id})
        
        if assinante:
            try:
                # Converte o campo 'expira' para datetime, caso necessário
                expira_atual = assinante.get('expira')
                if isinstance(expira_atual, str):
                    expira_atual = datetime.fromisoformat(expira_atual)  # Ajuste se necessário para seu formato de string
                
                # Garante que expira_atual é um datetime válido
                if not isinstance(expira_atual, datetime):
                    raise ValueError("Campo 'expira' não é um datetime válido.")
                
                # Calcula a nova data de expiração
                nova_expiracao = expira_atual + timedelta(days=dias)
                
                # Atualiza o registro no banco de dados
                self.collection_payment.update_one({'id': id}, {'$set': {'expira': nova_expiracao}})
                
                return True
            except Exception as e:
                print(f"Erro ao extender assinatura: {e}")
                return False
        
        # Assinante não encontrado
        return False
    def extender_vitalicio(self, id):
        from datetime import datetime, timedelta

        # Busca o assinante pelo ID
        assinante = self.collection_payment.find_one({'id': id})
        
        if assinante:
            try:
                # Converte o campo 'expira' para datetime, caso necessário
                expira_atual = assinante.get('expira')
                if isinstance(expira_atual, str):
                    expira_atual = datetime.fromisoformat(expira_atual)  # Ajuste se necessário para o formato do seu campo
                
                # Garante que expira_atual é um datetime válido
                if not isinstance(expira_atual, datetime):
                    raise ValueError("Campo 'expira' não é um datetime válido.")
                
                # Define uma nova data de expiração vitalícia (100 anos no futuro)
                nova_expiracao = expira_atual + timedelta(days=365 * 100)
                
                # Atualiza o registro no banco de dados
                self.collection_payment.update_one({'id': id}, {'$set': {'expira': nova_expiracao}})
                
                return True
            except Exception as e:
                print(f"Erro ao extender para vitalício: {e}")
                return False
        
        # Assinante não encontrado
        return False
    

    def get_id_nao_assinantes(self):
        usuarios = self.collection.find({'qt_assinatura': {'$lt': 1}})
        return list(usuarios)
usuario = Usuario()

'''
[{'id': '673195223', 'nome': 'Rafael', 'username': 'rafaellima777', 'idioma': 'portugues_br', 'tipo': 'mensal', 'criacao': datetime.datetime(2024, 12, 17, 8, 3, 9, 631000), 'expiracao': datetime.datetime(2025, 1, 16, 8, 3, 9, 631000)}]
❯ 
'''
print(usuario.extender_assinatura('673195223', 7))
print(usuario.show_info_assinantes())
#    id = assinante.get('id') AttributeError: 'str' object has no attribute 'get'