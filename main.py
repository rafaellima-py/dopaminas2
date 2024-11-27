from telebot.async_telebot import AsyncTeleBot
from decouple import config
import asyncio
import aiofiles
from mongocon import *
from traducoes import *
from utils import *
from asyncio import sleep
import datetime
from datetime import timedelta
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatInviteLink
from random import randint
mensagens = {}
temporizador_user = {}
user_plano = {}
admin = '6721447659'
user_images = {}
canal =  '-1002411773802'#'@SecretinhoOficial'
historico_previas = {}
async def set_tempo(id):
    
    tempo = 100
    chamada = 4
    temporizador_user[id] = {'chamada': chamada,
                             'tempo': tempo,
                             'msg1':False,
                             'msg2':False,
                             'msg3':False,
                             'msg4':False
                             }


async def reset_tempo(id):
    if id in temporizador_user:
        try:
            temporizador_user[id]['tempo'] = 100
        except Exception as e:
            print(f"Erro ao resetar tempo para o usuário {id}: {e}")
    else:
        await set_tempo(id)
            

#------------------CHECADOR DE ASSINATURAS ------------------


async def verificar_assinaturas():
    usuario = Usuario()
    limite_msg_usuario = {}  # Dicionário para controlar o limite de mensagens por usuário
    data_all = {}
    
    while True:
        await asyncio.sleep(60)  # Verifica a cada 60 segundos
        
        # Itera sobre todas as assinaturas
        for assinatura in usuario.all_id_assinatura():
            id = assinatura['id']
            data_expiracao = assinatura['expira']  # Se já for datetime, não precisa de conversão
            agora = datetime.datetime.utcnow()
            restante = data_expiracao - agora 
            #total_minutos_restantes = restante.days * 24 * 60 + restante.seconds // 60
            idioma = assinatura['idioma']
            
            data_all[id] = {
               
                'expira': data_expiracao,
                'restante_d': restante.days,
                'restante_m': restante.seconds // 60
            }
            
            # Inicializa o limite de mensagens para novos usuários se ainda não existir
            if id not in limite_msg_usuario:
                limite_msg_usuario[id] = {'expirado': False,
                                          'avisado_5_dias': False,
                                          'avisado_4_dias': False,
                                          'avisado_3_dias': False,
                                          'avisado_2_dias': False,
                                          'avisado_1_dia': False,
                                          }

            print(f"Verificando usuário {id}, expira em: {data_all[id]['restante_d']} dias, {data_all[id]['restante_m']} minutos")
            print(data_all)
            # Verifica se a assinatura expirou
            if data_expiracao <= agora and not limite_msg_usuario[id]['expirado']:
                print(f'{id}: assinatura expirada')
                try:
                    Usuario().delete_assinatura(str(id))
                    await bot.kick_chat_member(chat_id=canal, user_id=id)
                except Exception as e:
                    print(f"Erro ao excluir usuário {id} do chat {canal}: {e}")
                    continue
                await bot.send_message(id, language[idioma]['expirado'])
                limite_msg_usuario[id]['expirado'] = True  # Marca como expirada para não repetir a ação
            
            
            elif data_all[id]['restante_d'] == 5 and not limite_msg_usuario[id]['avisado_5_dias']:
                await bot.send_message(id, language[idioma]['5dias'])
                limite_msg_usuario[id]['avisado_5_dias'] = True  # Marca que o aviso foi enviado
                print(f'{id}: aviso de expiração em 5 dias enviado')
            
            elif data_all[id]['restante_d'] == 4 and not limite_msg_usuario[id]['avisado_4_dias']:
                await bot.send_message(id, language[idioma]['4dias'])
                limite_msg_usuario[id]['avisado_4_dias'] = True  # Marca que o aviso foi enviado
                print(f'{id}: aviso de expiração em 4 dias enviado')
            
            # Verifica se a assinatura vai expirar em 3 dias
            elif data_all[id]['restante_d'] == 3 and not limite_msg_usuario[id]['avisado_3_dias']:
                await bot.send_message(id, language[idioma]['3dias'])
                limite_msg_usuario[id]['avisado_3_dias'] = True  # Marca que o aviso foi enviado
                print(f'{id}: aviso de expiração em 3 dias enviado')
            
            elif data_all[id]['restante_d'] == 2 and not limite_msg_usuario[id]['avisado_2_dias']:
                await bot.send_message(id, language[idioma]['2dias'])
                limite_msg_usuario[id]['avisado_2_dias'] = True  # Marca que o aviso foi enviado
                print(f'{id}: aviso de expiração em 2 dias enviado')
            
            elif data_all[id]['restante_d'] == 1 and not limite_msg_usuario[id]['avisado_1_dia']:
                await bot.send_message(id, language[idioma]['1dias'])
                limite_msg_usuario[id]['avisado_1_dia'] = True  # Marca que o aviso foi enviado
                print(f'{id}: aviso de expiração em 1 dia enviado')
                
                
async def temporizador():
    mensagens = {
    'portugues': {
        'msg1': 'Olá! 🎯 Está por aí? Temos muito conteúdo quente esperando por você no VIP! Não perca a chance de voltar e curtir tudo em primeira mão. 😏🔥',
        'msg2': '👀 Sentimos sua falta! Está na hora de retomar o acesso ao conteúdo exclusivo. Venha aproveitar agora, estamos esperando por você no VIP. 😈✨',
        'msg3': 'Você ficou ausente por um tempo, mas o conteúdo exclusivo não para de chegar! 🎁 Aproveite agora e se entregue à experiência VIP que só o nosso canal oferece! 🔥',
        'msg4': 'Hey! Tudo bem por aí? 🧐 O VIP está mais quente do que nunca e você ainda pode voltar quando quiser! Acesse agora e veja o que perdeu. 🚀😏',
    },
    'espanhol': {
        'msg1': '¡Hola! 🎯 ¿Estás ahí? Tenemos mucho contenido exclusivo esperándote en el VIP. No pierdas la oportunidad de regresar y disfrutarlo todo antes que los demás. 😏🔥',
        'msg2': '👀 ¡Te extrañamos! Es hora de recuperar el acceso al contenido exclusivo. Vuelve y aprovecha ahora, te esperamos en el VIP. 😈✨',
        'msg3': 'Has estado ausente por un tiempo, pero el contenido exclusivo sigue llegando. 🎁 ¡Disfruta ahora y sumérgete en la experiencia VIP que solo nuestro canal te ofrece! 🔥',
        'msg4': '¡Hey! ¿Todo bien por ahí? 🧐 El VIP está más caliente que nunca y todavía puedes regresar cuando quieras. ¡Entra ahora y mira lo que te has perdido! 🚀😏',
    },
    
    'portugues_br': {
        'msg1': 'Olá! 🎯 Está por aí? Temos muito conteúdo quente esperando por você no VIP! Não perca a chance de voltar e curtir tudo em primeira mão. 😏🔥',
        'msg2': '👀 Sentimos sua falta! Está na hora de retomar o acesso ao conteúdo exclusivo. Venha aproveitar agora, estamos esperando por você no VIP. 😈✨',
        'msg3': 'Você ficou ausente por um tempo, mas o conteúdo exclusivo não para de chegar! 🎁 Aproveite agora e se entregue à experiência VIP que só o nosso canal oferece! 🔥',
        'msg4': 'Hey! Tudo bem por aí? 🧐 O VIP está mais quente do que nunca e você ainda pode voltar quando quiser! Acesse agora e veja o que perdeu. 🚀😏',
    
        }
}

    while True:
        await sleep(10)
        
        # Itera sobre uma cópia para evitar o erro de modificação do dicionário
        for user, dados in list(temporizador_user.items()):
            temporizador_user[user]['tempo'] -= 10
            existe = Usuario().usuario_existe(str(user))
            if existe:
                idioma = Usuario().ver_idioma(str(user))
                #if idioma == None:
                #    Usuario.inserir_idioma(str(user), 'portugues')
                
                
                print(temporizador_user)
                if temporizador_user[user]['chamada'] > 0 and temporizador_user[user]['msg1'] == False and temporizador_user[user]['tempo'] == 0:
                    await bot.send_message(user, mensagens[idioma]['msg1'])
                    temporizador_user[user]['msg1'] = True
                    temporizador_user[user]['chamada'] -= 1
                    print(f"Enviando mensagem para {user}")
                    await sleep(3600)

                if temporizador_user[user]['chamada'] > 0 and temporizador_user[user]['msg2'] == False and temporizador_user[user]['tempo'] < 0:
                    await bot.send_message(user, mensagens[idioma]['msg2'])
                    temporizador_user[user]['msg2'] = True
                    temporizador_user[user]['chamada'] -= 1
                    print(f"Enviando mensagem para {user}")
                    await sleep(3600*2)

                if temporizador_user[user]['chamada'] > 0 and temporizador_user[user]['msg3'] == False and temporizador_user[user]['tempo'] < 0:
                    await bot.send_message(user, mensagens[idioma]['msg3'])
                    temporizador_user[user]['msg3'] = True
                    temporizador_user[user]['chamada'] -= 1
                    print(f"Enviando mensagem para {user}")
                    await sleep(3600*3)

                if temporizador_user[user]['chamada'] > 0 and temporizador_user[user]['msg4'] == False and temporizador_user[user]['tempo'] < 0:
                    await bot.send_message(user, mensagens[idioma]['msg3'])
                    temporizador_user[user]['msg4'] = True
                    temporizador_user[user]['chamada'] -= 1
                    print(f"Enviando mensagem para {user}")
                    await sleep(20)
                if temporizador_user[user]['chamada'] == 0:
                    temporizador_user.pop(user, None)



bot = AsyncTeleBot(config('TELEGRAM_KEY'))

@bot.message_handler(commands=['start'])
async def start(message):
    id_user = message.from_user.id
    historico_previas[id_user] = False
    await set_tempo(message.from_user.id)
    if not bot_in_private(message):
        return
    
    usuario_existe = Usuario().usuario_existe(str(message.from_user.id))
    username = message.from_user.username
    #print(username)
    
    if not usuario_existe:
        #print('nao existe')
        usuario = {
    'id': str(message.from_user.id),
    'nome': message.from_user.first_name,
    'username': message.from_user.username,
    'idioma': None,  # Se você quiser manter idioma como opcional
    'qt_assinatura': 0,
    'qtd_start': 1,
    'data_cadastro': datetime.datetime.now()
}
       

        Usuario().cadastrar_usuario(usuario)
        language_markup = InlineKeyboardMarkup(row_width=2)
        language_markup.add(InlineKeyboardButton(f'🇵🇹 Português', callback_data='set_language_portugues'))
        language_markup.add(InlineKeyboardButton(f'🇪🇸 Espanhol', callback_data='set_language_espanhol'))
        language_markup.add(InlineKeyboardButton(f'🇧🇷 Português do Brasil', callback_data='set_language_portugues_br'))
        await bot.send_message(message.chat.id, 'Choose your language', reply_markup=language_markup)
   
    if usuario_existe:
        idioma = Usuario().ver_idioma(str(message.from_user.id))
        qtd_assinatura = Usuario().qtd_assinatura(str(message.from_user.id))
        if Usuario().get_qtd_start(str(message.from_user.id)) > 0 and not idioma:
            language_markup = InlineKeyboardMarkup(row_width=2)
            language_markup.add(InlineKeyboardButton(f'🇵🇹 Português', callback_data='set_language_portugues'))
            language_markup.add(InlineKeyboardButton(f'🇪🇸 Espanhol', callback_data='set_language_espanhol'))
            language_markup.add(InlineKeyboardButton(f'🇧🇷 Português do Brasil', callback_data='set_language_portugues_br'))
            await bot.send_message(message.chat.id, 'Choose your language', reply_markup=language_markup)

        if qtd_assinatura == 0:
            await wellcome_new_user(message, message.from_user.id)
            await set_tempo(message.from_user.id)
        elif qtd_assinatura > 0:
            await wellcome_new_user(message, message.from_user.id)
            await set_tempo(message.from_user.id)
            





async def wellcome_new_user(message, id_user):
    
    idioma = Usuario().ver_idioma(str(id_user))
    #print(idioma)
    if idioma == 'espanhol':
        with open('sources/espanhol.jpeg', 'rb') as f:
            await bot.send_photo(message.chat.id, f)
            await bot.send_message(message.chat.id, language[idioma]['inicio'])
            await list_products(message, idioma)
    if idioma == 'portugues':
        with open('sources/portugues.jpeg', 'rb') as f:
            await bot.send_photo(message.chat.id, f)
            await bot.send_message(message.chat.id, language[idioma]['inicio'])
            #await list_products(message, idioma)
            await interesse(message, idioma)
    if idioma == 'ingles':
        with open('sources/ingles.jpeg', 'rb') as f:
            await bot.send_photo(message.chat.id, f)
            await bot.send_message(message.chat.id, language[idioma]['inicio'])
            #await list_products(message, idioma)
            await interesse(message, idioma)
    if idioma == 'portugues_br':
        with open('sources/portugues.jpeg', 'rb') as f:
            await bot.send_photo(message.chat.id, f)
            await bot.send_message(message.chat.id, language[idioma]['inicio'])
            #await list_products(message, idioma)
            await interesse(message, idioma)


async def interesse(message, idioma):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton(language[idioma]['sim'], callback_data='sim'))
    markup.add(InlineKeyboardButton(language[idioma]['nao'], callback_data='nao'))
    await bot.send_message(message.chat.id, language[idioma]['call_interesse'], reply_markup=markup)

async def list_products(message,idioma):
    
    markup = InlineKeyboardMarkup(row_width=2)
    semanal = InlineKeyboardButton(language[idioma]['semanal'], callback_data='pl_semanal')
    mensal = InlineKeyboardButton(language[idioma]['mensal'], callback_data='pl_mensal')
    trimestral = InlineKeyboardButton(language[idioma]['trimestral'], callback_data='pl_trimestral')
    markup.add(semanal, mensal, trimestral)
    await bot.send_message(chat_id=message.chat.id, text=language[idioma]['plano'], reply_markup=markup)



async def show_plan(message, plan):
    user_id = message.from_user.id
    idioma = Usuario().ver_idioma(str(user_id))
    
    
    print(idioma, user_id)
    InlineKeyboardMarkup(row_width=2)
   
    if not historico_previas[user_id]:
        await show_previas(message)
        historico_previas[user_id] = True
    await bot.send_message(chat_id=user_id, text=language[idioma][plan])
        
    markup = InlineKeyboardMarkup(row_width=2)
    bizum_bt = InlineKeyboardButton(language[idioma]['bizum'], callback_data='cb_bisum')
    mbway_bt = InlineKeyboardButton(language[idioma]['mbway'], callback_data='cb_mbway')
    voltar_bt = InlineKeyboardButton('Back', callback_data='voltar')
    pix_bt = InlineKeyboardButton('Pague via Pix', callback_data='cb_pix')
    if idioma != 'portugues_br':
        markup.add(bizum_bt, mbway_bt, voltar_bt)
        await bot.send_message(user_id, language[idioma]['plano'], reply_markup=markup)
    else:
        markup.add(pix_bt, voltar_bt)
        await bot.send_message(user_id, language[idioma]['plano'], reply_markup=markup)


async def show_previas(message):
    user_id = message.from_user.id
    idioma = Usuario().ver_idioma(str(user_id))
    
    
    with open(f'sources/previa{randint(1, 2)}.mp4', 'rb') as f:
        await bot.send_video(user_id, f, caption=language[idioma]['previa'])
        

@bot.callback_query_handler(func=lambda call: True)
async def callback(call):
    
    #------------------------------ SESSAO DE CADASTRO ------------------------------
    # set language callback é referente ao botao inicial de selecionar idioma
    
    
    
    match call.data:


        case 'sim':
            idioma =  Usuario().ver_idioma(str(call.from_user.id))
            markup = InlineKeyboardMarkup(row_width=2)
            markup.add(InlineKeyboardButton(language[idioma]['oferta_exclusiva'], callback_data='pl_exclusiva'))
            markup.add(InlineKeyboardButton(language[idioma]['oferta_semanal'], callback_data='pl_semanal'))
            
            await bot.send_message(call.message.chat.id, language[idioma]['oferta_apresentacao'], reply_markup=markup)
        
        case 'nao':
            idioma =  Usuario().ver_idioma(str(call.from_user.id))
            await bot.send_message(call.message.chat.id, language[idioma]['cb_nao_interesse']) 

        case 'set_language_portugues':
            
            # se ele caiu aqui, não está cadastrado no banco, entao vamos cadastrar em ambos os idiomas
            
            await bot.delete_message(call.message.chat.id, call.message.id)
            Usuario().inserir_idioma(str(call.from_user.id), 'portugues')
            await wellcome_new_user(call.message, str(call.from_user.id))

        case 'set_language_espanhol':
            await bot.delete_message(call.message.chat.id, call.message.id)
            Usuario().inserir_idioma(str(call.from_user.id), 'espanhol')
            await wellcome_new_user(call.message, str(call.from_user.id))

        case 'set_language_portugues_br':
            await bot.delete_message(call.message.chat.id, call.message.id)
            Usuario().inserir_idioma(str(call.from_user.id), 'portugues_br')
            await wellcome_new_user(call.message, str(call.from_user.id))
        
        case 'pl_semanal':
            #await bot.delete_message(call.message.chat.id, call.message.id)
            await bot.delete_message(call.message.chat.id, call.message.id)
            #idioma = Usuario().ver_idioma(str(call.from_user.id))
            await show_plan(call, 'semanal')
            #user_plano[call.from_user.id] = {
            #'nome': call.from_user.first_name,
            #'username': call.from_user.username,
            #'idioma': idioma,
            #'plano': 'semanal',
            #'preco': 'None'
        
    #}
        #    print(user_plano)

        case 'pl_mensal':
            await bot.delete_message(call.message.chat.id, call.message.id)
            await show_plan(call, 'mensal')
            await reset_tempo(call.from_user.id)
            idioma = Usuario().ver_idioma(str(call.from_user.id))
           
            user_plano[call.from_user.id] = {
            'nome': call.from_user.first_name,
            'username': call.from_user.username,
            'idioma': idioma,
            'plano': 'mensal',
            'preco': None
        
    }        
            print(user_plano)
        case 'pl_trimestral':
            await bot.delete_message(call.message.chat.id, call.message.id)
            await reset_tempo(call.from_user.id)
            await show_plan(call, 'trimestral')
            idioma = Usuario().ver_idioma(str(call.from_user.id))
        
            user_plano[call.from_user.id] = {
            'nome': call.from_user.first_name,
            'username': call.from_user.username,
            'idioma': idioma,
            'plano': 'trimestral',
            'preco': None
        
    }      
            print(user_plano)

        case 'cb_bisum':
            idioma = Usuario().ver_idioma(str(call.from_user.id))
            await reset_tempo(call.from_user.id)
            await bot.send_message(call.from_user.id, language[idioma]['pg_instrucao'])
            chave_pg = "Chave: 604338509"
            await bot.send_message(call.from_user.id, text=f"```{chave_pg}```", parse_mode="MarkdownV2")
            await bot.send_message(call.from_user.id, language[idioma]['esperando_pg'])
            
        case 'cb_mbway':
            idioma = Usuario().ver_idioma(str(call.from_user.id))
            await reset_tempo(call.from_user.id)
            await bot.send_message(call.from_user.id, language[idioma]['pg_instrucao'])
            chave_pg = "Chave: 933466639"
            await bot.send_message(call.from_user.id, text=f"```{chave_pg}```", parse_mode="MarkdownV2")
            await bot.send_message(call.from_user.id, language[idioma]['esperando_pg'])
        

        case 'cb_pix':
            idioma = Usuario().ver_idioma(str(call.from_user.id))
            await reset_tempo(call.from_user.id)
            await bot.send_message(call.from_user.id, language[idioma]['pg_instrucao'])
            chave_pg = "Chave: c2e51e73-813e-45f6-87dd-e7b70f859870"
            await bot.send_message(call.from_user.id, text=f"```{chave_pg}```", parse_mode="MarkdownV2")
            await bot.send_message(call.from_user.id, language[idioma]['esperando_pg'])
           
        
        case 'voltar':
            idioma = Usuario().ver_idioma(str(call.from_user.id))
            
            await bot.delete_message(call.message.chat.id, call.message.message_id)
            await reset_tempo(call.from_user.id)
            await list_products(call.message, idioma)
        #--------------- callback para comprovantes manuais ------------------
          # Extrair o message_id da callback data
    message_id = int(call.data.split('_')[1])
    
    # Buscar o ID do usuário que enviou a imagem
    user_id = user_images.get(message_id)
    
    if not user_id:
        await bot.send_message(call.message.chat.id, 'Erro: não foi possível encontrar o usuário.')
        return
    
    match call.data.split('_')[0]:
        case 'aceitar':
            # O admin aceitou o comprovante
            await reset_tempo(call.from_user.id)
            await bot.send_message(call.message.chat.id, 'Comprovante Aceito! Enviando notificação ao usuário...')
            await bot.send_message(user_id, 'Seu comprovante foi aceito! Obrigado.')
            await criar_assinatura(user_id)
            
            
        case 'cancelar':
            await reset_tempo(call.from_user.id)
            # O admin cancelou o comprovante
            await bot.send_message(call.message.chat.id, 'Comprovante Cancelado! Enviando notificação ao usuário...')
            await bot.send_message(user_id, 'Seu comprovante foi cancelado. Por favor, tente novamente.')
    
    # Excluir a foto dos registros (opcional)
    user_images.pop(message_id, None)



async def criar_assinatura(user_id):
    if user_plano[user_id]['plano'] == 'semanal':
                expiracao = datetime.datetime.utcnow() + timedelta(days=7)
            
    elif user_plano[user_id]['plano'] == 'mensal':
        expiracao = datetime.datetime.utcnow() + timedelta(days=30)
    elif user_plano[user_id]['plano'] == 'trimestral':
        expiracao = datetime.datetime.utcnow() + timedelta(days=90)
    id = str(user_id)
    nome = user_plano[user_id]['nome']
    username = user_plano[user_id]['username']
    idioma = user_plano[user_id]['idioma']
    
    valor = user_plano[user_id]['preco']
    tipo = user_plano[user_id]['plano']
    criado = datetime.datetime.utcnow()
    expira = expiracao
                
    user_assinatura = {
    'id': str(user_id),
    'nome': nome,
    'username': username,
    'idioma': idioma,
    'assinatura': True,
    'valor': valor,
    'tipo': tipo,
    'criado': criado,
    'expira': expira
}

    existe_assinatura = Usuario().existe_assinatura(str(user_id))
    if existe_assinatura:
        Usuario().delete_assinatura(str(user_id))
        Usuario().inserir_assinatura(user_assinatura)
        Usuario().inserir_qt_assinatura(str(user_id))
        temporizador_user.pop(user_id, None)
    else:
        Usuario().inserir_assinatura(user_assinatura)
        Usuario().inserir_qt_assinatura(str(user_id))
    
                
                     
            
    await bot.send_message(user_id, language[idioma]['obrigado'])
    await sleep(1)

    limit = 1 
    convite: ChatInviteLink = await bot.create_chat_invite_link(chat_id=canal, member_limit=limit)
    await bot.send_message(user_id, f'Link: {convite.invite_link}')
            
    user_plano.pop(user_id, None)
    temporizador_user.pop(user_id, None)


@bot.message_handler(content_types=['photo'])
async def handle_photo(message):
    if message.chat.type == 'private':
        await reset_tempo(message.from_user.id)
        user_id = message.from_user.id  # Obtém o ID do usuário que enviou a imagem
        user_images[message.message_id] = user_id  # Armazena o ID do usuário usando message_id como chave
        
        await bot.send_message(message.chat.id, 'Sending to admin...')
        
        # Encaminhar a foto para o administrador
        await bot.forward_message(admin, message.chat.id, message.message_id)
        
        # Criar botões de Aceitar/Cancelar
        botoes = InlineKeyboardMarkup(row_width=2)
        aceitar = InlineKeyboardButton('Aceitar', callback_data=f'aceitar_{message.message_id}')
        cancelar = InlineKeyboardButton('Cancelar', callback_data=f'cancelar_{message.message_id}')
        botoes.add(aceitar, cancelar)
        
        # Enviar a mensagem para o admin com os botões
        await bot.send_message(admin, 'Comprovante recebido. Aceitar ou Cancelar?', reply_markup=botoes)
    


async def main():
    print('Iniciando verificação de assinaturas')
    #asyncio.create_task(verificar_assinaturas())
        
        
    print('Iniciando temporizador')
    asyncio.create_task(temporizador())    
    
    
    await bot.polling(none_stop=True)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)

        