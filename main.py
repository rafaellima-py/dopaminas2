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
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatInviteLink, ReplyKeyboardMarkup, KeyboardButton
from random import randint
from asyncio import sleep
mensagens = {}
temporizador_user = {}
user_plano = {}
admin =  '673195223' #'5090351005' # #'6721447659' #7636075219
user_images = {}
canal =  '-1002411773802'#'@SecretinhoOficial'
historico_previas = {}
mensagens_broadcast = {}
travar_disparo = {}


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


    historico_mensagens = {}  # Histórico de mensagens enviadas

    while True:
        for user, dados in list(temporizador_user.items()):
            # Atualiza o tempo restante
            temporizador_user[user]['tempo'] -= 10
            print(temporizador_user)

            # Verifica se o usuário ainda existe
            existe = Usuario().usuario_existe(str(user))
            if not existe:
                temporizador_user.pop(user, None)
                continue

            # Obtém o idioma do usuário
            idioma = Usuario().ver_idioma(str(user))
            if idioma not in mensagens:
                continue  # Ignora se o idioma não está no dicionário

            # Envio das mensagens baseado no tempo e status
            if not dados['msg1'] and dados['tempo'] <= 0:
                mensagem = mensagens[idioma]['msg1']
                await send_audio(user, 'audio3.ogg')  # Envia o áudio
                historico_mensagens.setdefault(user, []).append(mensagem)  # Salva no histórico
                temporizador_user[user]['msg1'] = True
                temporizador_user[user]['tempo'] += 3600  # Aguarda 1 hora para a próxima mensagem

            elif not dados['msg2'] and dados['tempo'] <= 0:
                mensagem = mensagens[idioma]['msg2']
                # await bot.send_message(user, mensagem)  # Envia a mensagem
                historico_mensagens.setdefault(user, []).append(mensagem)
                temporizador_user[user]['msg2'] = True
                temporizador_user[user]['tempo'] += 3600 * 2  # Aguarda 2 horas

            # Remove o usuário quando todas as mensagens foram enviadas
            if all([dados['msg1'], dados['msg2']]):
                temporizador_user.pop(user, None)

        # Intervalo entre cada iteração
        await asyncio.sleep(10)



bot = AsyncTeleBot(config('TELEGRAM_KEY_TEST'))

@bot.message_handler(commands=['start'])
async def start(message):
    id_user = message.from_user.id
    historico_previas[id_user] = False
    mensagens[id_user] = []
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
       # language_markup.add(InlineKeyboardButton(f'🇪🇸 Espanhol', callback_data='set_language_espanhol'))
        language_markup.add(InlineKeyboardButton(f'🇧🇷 Português do Brasil', callback_data='set_language_portugues_br'))
        await bot.send_message(message.chat.id, 'Choose your language', reply_markup=language_markup)
   
    if usuario_existe:
        idioma = Usuario().ver_idioma(str(message.from_user.id))
        qtd_assinatura = Usuario().qtd_assinatura(str(message.from_user.id))
        if Usuario().get_qtd_start(str(message.from_user.id)) > 0 and not idioma:
            language_markup = InlineKeyboardMarkup(row_width=2)
            language_markup.add(InlineKeyboardButton(f'🇵🇹 Português', callback_data='set_language_portugues'))
           # language_markup.add(InlineKeyboardButton(f'🇪🇸 Espanhol', callback_data='set_language_espanhol'))
            language_markup.add(InlineKeyboardButton(f'🇧🇷 Português do Brasil', callback_data='set_language_portugues_br'))
            await bot.send_message(message.chat.id, 'Choose your language', reply_markup=language_markup)

        if qtd_assinatura == 0:
            print(id_user)
            await wellcome_new_user(id_user=id_user)
            await set_tempo(id_user)
        elif qtd_assinatura > 0:
            await wellcome_old_user(message, message.from_user.id)
            await set_tempo(id_user)
        
            





async def wellcome_new_user(id_user):
    
    idioma = Usuario().ver_idioma(str(id_user))
    #print(idioma)
    if idioma == 'espanhol':
        msg = await bot.send_message(id_user, language[idioma]['inicio'])
        
        msg2 = await send_audio(id_user, 'audio1.ogg')
        await sleep(5)
        msg3 = await cta1(id_user, idioma)
        await registro_historico(msg, id_user)
       
 
    elif idioma == 'portugues':
        print(idioma)
        msg = await bot.send_message(id_user, language[idioma]['inicio'])
        
        msg2 = await send_audio(id_user, 'audio1_ap.ogg')
        await sleep(5)
        msg3 = await cta1(id_user, idioma)
        await registro_historico(msg, id_user)
       
    
    elif idioma == 'ingles':
        msg = await bot.send_message(id_user, language[idioma]['inicio'])
        
        msg2 = await send_audio(id_user, 'audio1_ap.ogg')
        await sleep(5)
        msg3 = await cta1(id_user, idioma)
        await registro_historico(msg, id_user)
    
    elif idioma == 'portugues_br':
        
        msg = await bot.send_message(id_user, language[idioma]['inicio'])
        
        msg2 = await send_audio(id_user, 'audio1_ap.ogg')
        await sleep(5)
        print('antes do cta', id_user)
        msg3 = await cta1(id_user, idioma)
        #await registro_historico(msg, id_user)


async def send_audio(id_user, audio):
    with open(f'sources/{audio}', 'rb') as f:
        msg = await bot.send_audio(id_user, f)
        await registro_historico(msg, id_user)




async def wellcome_old_user(message, id_user):
    
    idioma = Usuario().ver_idioma(str(id_user))
    #print(idioma)
    if idioma == 'espanhol':
        #with open('sources/espanhol.jpeg', 'rb') as f:
        #await bot.send_photo(message.chat.id, f)
        msg = await bot.send_message(message.chat.id, language[idioma]['inicio2'])
        #await registro_historico(msg, id_user)
    
        await old_list_products(message, idioma)
    
    if idioma == 'portugues':
        #with open('sources/portugues.jpeg', 'rb') as f:
        #await bot.send_photo(message.chat.id, f)
        msg = await bot.send_message(message.chat.id, language[idioma]['inicio2'])
        #await registro_historico(msg, id_user)
       
        await old_list_products(message, idioma)
    
    if idioma == 'portugues_br':
        #with open('sources/portugues.jpeg', 'rb') as f:
        #await bot.send_photo(message.chat.id, f)
        msg = await bot.send_message(message.chat.id, language[idioma]['inicio2'])
        #await registro_historico(msg, id_user)
        await old_list_products(message, idioma)
    


async def cta1(id_user, idioma):
    print('id caiu no cta', id_user)
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton(language[idioma]['cta1'], callback_data='cta1'))
    
    msg = await bot.send_message(id_user, language[idioma]['clique'], reply_markup=markup)
    await registro_historico(msg, id_user)



async def list_products(message,idioma):
    
    markup = InlineKeyboardMarkup(row_width=2)
    semanal = InlineKeyboardButton(language[idioma]['semanal'], callback_data='pl_semanal')
    mensal = InlineKeyboardButton(language[idioma]['mensal'], callback_data='pl_mensal')
    trimestral = InlineKeyboardButton(language[idioma]['trimestral'], callback_data='pl_trimestral')
    markup.add(semanal, mensal, trimestral)
    msg = await bot.send_message(chat_id=message.chat.id, text=language[idioma]['plano'], reply_markup=markup)
    #await registro_historico(msg, message.from_user.id)

async def old_list_products(message,idioma):
    markup = InlineKeyboardMarkup(row_width=2)
    semanal = InlineKeyboardButton(language[idioma]['semanal'], callback_data='pl_semanal')
    mensal = InlineKeyboardButton(language[idioma]['mensal'], callback_data='pl_mensal')
    trimestral = InlineKeyboardButton(language[idioma]['trimestral'], callback_data='pl_trimestral')
    markup.add(mensal, trimestral)
    msg = await bot.send_message(chat_id=message.chat.id, text=language[idioma]['plano'], reply_markup=markup)
    #await registro_historico(msg, message.from_user.id)

    

async def show_plan(message, plan):
    user_id = message.from_user.id
    idioma = Usuario().ver_idioma(str(user_id))
    await reset_tempo(user_id)
    await delete_mensagem_historico(user_id)
    
    print(idioma, user_id)
    InlineKeyboardMarkup(row_width=2)
   
    #if not historico_previas[user_id]:
        #await show_previas(user_id, idioma)
        #historico_previas[user_id] = True #False manda sem limites, True trava em um
    #msg = await bot.send_message(chat_id=user_id, text= language[idioma]['selecionado'] + language[idioma][plan])
    #await registro_historico(msg, user_id)
    trimestral = {user_id: False}    
    markup = InlineKeyboardMarkup(row_width=3)
    bizum_bt = InlineKeyboardButton(language[idioma]['bizum'], callback_data='cb_bisum')
    mbway_bt = InlineKeyboardButton(language[idioma]['mbway'], callback_data='cb_mbway')
    voltar_bt = InlineKeyboardButton('Back', callback_data='voltar')
    bt_paypal = InlineKeyboardButton('PayPal', callback_data='cb_paypal')
    pix_bt = InlineKeyboardButton('Pague via Pix', callback_data='cb_pix')
    suporte_bt = InlineKeyboardButton(language[idioma]['bt_suporte'], url='https://t.me/midasgn')
    qtd_assinatura = Usuario().qtd_assinatura(str(user_id))
    plano = user_plano[user_id]['plano']
    if plano == 'semanal':
        bt_voltar = InlineKeyboardButton(language[idioma]['voltar_mensal'], callback_data='pl_mensal')
        markup.add(bt_voltar)
    elif plano == 'mensal' and qtd_assinatura < 1:
        bt_voltar = InlineKeyboardButton(language[idioma]['voltar_semanal'], callback_data='pl_semanal')
        markup.add(bt_voltar)
    
    elif plano == 'mensal' and qtd_assinatura > 0 :
        bt_voltar = InlineKeyboardButton(language[idioma]['voltar_trimestral'], callback_data='pl_trimestral')
        markup.add(bt_voltar)

    elif plano == 'trimestral':
        bt_voltar = InlineKeyboardButton(language[idioma]['voltar_mensal'], callback_data='pl_mensal')
        trimestral[user_id] = True
        markup.add(bt_voltar)




    if idioma != 'portugues_br':
        markup.add(mbway_bt,bt_paypal, suporte_bt )
        msg_text = f"{language[idioma]['selecionado'].upper()}\n  __{language[idioma][plan]}__"
        msg_text = msg_text.replace('.', '\\.')

        msg = await bot.send_message(
            chat_id=user_id, 
            text=msg_text, 
            reply_markup=markup, 
            parse_mode='MarkdownV2'
        )

    else:
        markup.add(pix_bt,bt_paypal ,suporte_bt)
        msg_text = f"{language[idioma]['selecionado'].upper()}\n  __{language[idioma][plan]}__"
        msg_text = msg_text.replace('.', '\\.')

        msg = await bot.send_message(
            chat_id=user_id, 
            text=msg_text, 
            reply_markup=markup, 
            parse_mode='MarkdownV2'
        )

        
        await registro_historico(msg, user_id)



async def show_previas(id_user, idioma):
   
    idioma = Usuario().ver_idioma(str(id_user))
    
    
    with open(f'sources/previa{randint(1, 2)}.mp4', 'rb') as f:
        msg = await bot.send_video(id_user, f, caption=language[idioma]['previa'])
        #await registro_historico(msg, user_id)

@bot.callback_query_handler(func=lambda call: True)
async def callback(call):
    
    #------------------------------ SESSAO DE CADASTRO ------------------------------
    # set language callback é referente ao botao inicial de selecionar idioma
    
    
    
    match call.data:   
        case callback if callback.startswith('gerenciar_'):
            print(callback)
            id = str(callback.split('_')[1])
            user_info = Usuario().show_info_assinantes(id)
            markup = InlineKeyboardMarkup(row_width=2)
            markup.add(InlineKeyboardButton('Dar vitalício', callback_data=f'extender_vitalicio_{id}'))
            markup.add(InlineKeyboardButton('Cancelar assinatura ', callback_data=f'cancelar_assinatura_{id}'))
            markup.add(InlineKeyboardButton('Dar +7 Dias' , callback_data=f'extender_dias_7_{id}'))
            markup.add(InlineKeyboardButton('Dar +30 Dias' , callback_data=f'extender_dias_30_{id}'))
            markup.add(InlineKeyboardButton('<< Voltar' , callback_data=f'gerenciar'))
            if user_info:
                nome = user_info[0]['nome']
                username = user_info[0]['username']
                idioma = user_info[0]['idioma']
                tipo = user_info[0]['tipo']
                criacao = user_info[0]['criacao']
                expiracao = user_info[0]['expiracao']
                data_format = datetime.datetime.strftime(criacao, "%d-%m-%Y")
                data_ex_format = datetime.datetime.strftime(expiracao, "%d-%m-%Y")
                dias_restantes = expiracao - datetime.datetime.now()
                print(dias_restantes)
                if dias_restantes.days > 0:
                    dias_restantes = f"{dias_restantes.days} dias"
                elif dias_restantes.days == 0:
                    dias_restantes = f"{dias_restantes.seconds // 60} minutos"
    
                await bot.send_message(
                call.message.chat.id,
                (
                f"""
                📋 **Informações do Assinante** 
                👤 Nome: {nome}
                🌐 Usuário: @{username}
                📖 Idioma: {idioma}
                📦 Tipo: {tipo}
                📅 Criado em: {data_format}
                ⏳ Expira em: {data_ex_format}
                ⏳ Dias restantes: {dias_restantes}

                """),reply_markup=markup
                
            )           
        case callback if callback.startswith('cancelar_assinatura_'):
            id = str(callback.split('_')[2])

            try:
                await bot.kick_chat_member(chat_id=canal, user_id=id)
                Usuario().delete_assinatura(str(id))
                        
            except Exception as e:
                print(f"Erro ao excluir usuário {id} do chat {canal}: {e}")



        case callback if callback.startswith('extender_dias_7_'):
            id = str(callback.split('_')[3])
            try:
                Usuario().extender_assinatura(id, 7)
                await bot.send_message(call.message.chat.id, 'Assinatura foi extendida com sucesso!')
            except Exception as e:
                print(e)
                await bot.send_message(call.message.chat.id, 'Erro ao extender assinatura!')
        
        case callback if callback.startswith('extender_dias_30_'):
            id = str(callback.split('_')[3])
            print(id, "30dias")
            try:
                Usuario().extender_assinatura(id, 30)
                await bot.send_message(call.message.chat.id, 'Assinatura foi extendida!')
            except Exception as e:
                print(e)
                await bot.send_message(call.message.chat.id, 'Erro ao extender assinatura!')
        
        
        case callback if callback.startswith('extender_vitalicio_'):
            id = str(callback.split('_')[2])
            print(id, "vitalício")
            try:
                Usuario().extender_vitalicio(id)
                await bot.send_message(call.message.chat.id, 'Vitalício foi adicionado!')
            except Exception as e:
                print(e)
                await bot.send_message(call.message.chat.id, 'Erro ao adicionar vitalício!')
        
   
   
        case callback if callback.startswith('gerenciar'):
            if str(call.from_user.id) != str(admin):
                await bot.send_message(call.message.chat.id, 'Você não tem permissão para executar esta função.')
                return

            menu = InlineKeyboardMarkup(row_width=2)
            assinantes = Usuario().show_info_assinantes()

            if not assinantes:  # Verifica se a lista está vazia
                await bot.send_message(call.message.chat.id, 'Você não possui nenhuma assinatura.')
                return

            # Gera o menu com os assinantes
            for assinante in assinantes:
                nome = assinante.get('nome', 'N/A')
                id_assinante = assinante.get('id', 'N/A')
                username = assinante.get('username', 'N/A')
                menu.add(InlineKeyboardButton(f"{nome} ({username})", callback_data=f"gerenciar_{id_assinante}"))

            await bot.send_message(call.message.chat.id, 'Escolha um assinante para gerenciar:', reply_markup=menu)

        
        case 'cta1':
            await reset_tempo(call.from_user.id)
            idioma =  Usuario().ver_idioma(str(call.from_user.id))
            markup = InlineKeyboardMarkup(row_width=2)
            markup.add(InlineKeyboardButton(language[idioma]['oferta_exclusiva'], callback_data='pl_mensal')) 
            markup.add(InlineKeyboardButton(language[idioma]['oferta_semanal'], callback_data='pl_semanal'))
            await delete_mensagem_historico(call.from_user.id)
            await send_audio(call.from_user.id, 'audio2_ap.ogg')
            await sleep(10)
            msg = await bot.send_message(call.message.chat.id, text=f'_{language[idioma]['plano']}_', reply_markup=markup, parse_mode='MarkdownV2')
            await registro_historico(msg, call.from_user.id)
        case 'set_language_portugues':
            
            # se ele caiu aqui, não está cadastrado no banco, entao vamos cadastrar em ambos os idiomas
            await reset_tempo(call.from_user.id)
            await bot.delete_message(call.message.chat.id, call.message.id)
            Usuario().inserir_idioma(str(call.from_user.id), 'portugues')
            await wellcome_new_user(call.from_user.id)

        case 'set_language_espanhol':
            await reset_tempo(call.from_user.id)
            await bot.delete_message(call.message.chat.id, call.message.id)
            Usuario().inserir_idioma(str(call.from_user.id), 'espanhol')
            await wellcome_new_user(call.from_user.id)

        case 'set_language_portugues_br':
            await bot.delete_message(call.message.chat.id, call.message.id)
            Usuario().inserir_idioma(str(call.from_user.id), 'portugues_br')
            await wellcome_new_user(call.from_user.id)
        
        case 'pl_semanal':
            await reset_tempo(call.from_user.id)
            #await bot.delete_message(call.message.chat.id, call.message.id)
            #await delete_mensagem_historico(call.from_user.id, 1)
            idioma = Usuario().ver_idioma(str(call.from_user.id))
            user_plano[call.from_user.id] = {
            'nome': call.from_user.first_name,
            'username': call.from_user.username,
            'idioma': idioma,
            'plano': 'semanal',
            'preco': 'None'}

            await show_plan(call, 'semanal')
            print(user_plano)


        case 'pl_mensal':
            #await delete_mensagem_historico(call.from_user.id, 1)
            await reset_tempo(call.from_user.id)
            idioma = Usuario().ver_idioma(str(call.from_user.id))
           
            user_plano[call.from_user.id] = {
            'nome': call.from_user.first_name,
            'username': call.from_user.username,
            'idioma': idioma,
            'plano': 'mensal',
            'preco': None  }        
            await show_plan(call, 'mensal')
            print(user_plano)


        case 'pl_trimestral':
            await bot.delete_message(call.message.chat.id, call.message.id)
            await reset_tempo(call.from_user.id)
            idioma = Usuario().ver_idioma(str(call.from_user.id))
        
            user_plano[call.from_user.id] = {
            'nome': call.from_user.first_name,
            'username': call.from_user.username,
            'idioma': idioma,
            'plano': 'trimestral',
            'preco': None
        
    }      
            await show_plan(call, 'trimestral')
            print(user_plano)

        case 'cb_bisum':
            idioma = Usuario().ver_idioma(str(call.from_user.id))
            await reset_tempo(call.from_user.id)
            markup = InlineKeyboardMarkup()
            bt_suporte = InlineKeyboardButton(language[idioma]['bt_suporte'], url='https://t.me/midasgn')
            markup.add(bt_suporte)
            await bot.send_message(call.from_user.id, language[idioma]['pg_instrucao'] + language[idioma]['suporte'], reply_markup=markup)
            chave_pg = "Chave: 604338509"
            await bot.send_message(call.from_user.id, text=f"```{chave_pg}```", parse_mode="MarkdownV2")
            await bot.send_message(call.from_user.id, language[idioma]['esperando_pg'])
            
        case 'cb_mbway':
            idioma = Usuario().ver_idioma(str(call.from_user.id))
            await reset_tempo(call.from_user.id)
            markup = InlineKeyboardMarkup()
            bt_suporte = InlineKeyboardButton(language[idioma]['bt_suporte'], url='https://t.me/midasgn')
            markup.add(bt_suporte)
            await bot.send_message(call.from_user.id, language[idioma]['pg_instrucao'] + language[idioma]['suporte'], reply_markup=markup)
            chave_pg = "Chave: 933466639"
            await bot.send_message(call.from_user.id, text=f"```{chave_pg}```", parse_mode="MarkdownV2")
            await bot.send_message(call.from_user.id, language[idioma]['esperando_pg'])
        

        case 'cb_pix':
            idioma = Usuario().ver_idioma(str(call.from_user.id))
            await reset_tempo(call.from_user.id)
            markup = InlineKeyboardMarkup()
            bt_suporte = InlineKeyboardButton(language[idioma]['bt_suporte'], url='https://t.me/midasgn')
            markup.add(bt_suporte)
            await bot.send_message(call.from_user.id, language[idioma]['pg_instrucao'] + language[idioma]['suporte'], reply_markup=markup)
            chave_pg = "Chave: mccctavares@gmail.com"
            await bot.send_message(call.from_user.id, text=f"```{chave_pg}```", parse_mode="MarkdownV2")
            await bot.send_message(call.from_user.id, language[idioma]['esperando_pg'])
           
        
       
        case 'cb_paypal':
            idioma = Usuario().ver_idioma(str(call.from_user.id))
            await reset_tempo(call.from_user.id)
            markup = InlineKeyboardMarkup()
            bt_suporte = InlineKeyboardButton(language[idioma]['bt_suporte'], url='https://t.me/midasgn')
            markup.add(bt_suporte)
            await bot.send_message(call.from_user.id, language[idioma]['pg_instrucao'] + language[idioma]['suporte'], reply_markup=markup)
            chave_pg = "Chave: dopaminasltda@gmail.com"
            await bot.send_message(call.from_user.id, text=f"```{chave_pg}```", parse_mode="MarkdownV2")
            await bot.send_message(call.from_user.id, language[idioma]['esperando_pg'])



        case 'voltar':
            idioma = Usuario().ver_idioma(str(call.from_user.id))

            #await delete_mensagem_historico(call.from_user.id, 1)
            await reset_tempo(call.from_user.id)
            plano = user_plano[call.from_user.id]['plano']
            if plano == 'semanal':
                pass

        case 'visualizar':
            user_id = call.from_user.id
            mensagem = mensagens_broadcast.get(user_id)
            markup = InlineKeyboardMarkup(row_width=2)
            markup.add(InlineKeyboardButton('Enviar', callback_data='enviar'))
            print(mensagem)
            if not mensagem:
                await bot.send_message(user_id, 'Nenhuma mensagem salva. Use /disparar para começar.')
                return

            # Exibe o conteúdo dependendo do tipo
            if mensagem['type'] == 'text':
                await bot.send_message(user_id, mensagem['content'], reply_markup=markup)
            elif mensagem['type'] == 'photo':
                await bot.send_photo(user_id, mensagem['content'], caption=mensagem.get('caption'), reply_markup=markup)
            elif mensagem['type'] == 'video':
                await bot.send_video(user_id, mensagem['content'], caption=mensagem.get('caption'), reply_markup=markup)
            else:
                await bot.send_message(user_id, 'Tipo de mensagem desconhecido.')
        
        case 'enviar':
    
            user_id = call.from_user.id
            mensagem = mensagens_broadcast.get(user_id)

            if not mensagem:
                await bot.send_message(user_id, 'Nenhuma mensagem para enviar.')
                return

            usuario = Usuario()
            users = usuario.get_id_nao_assinantes()

            if not users:
                await bot.send_message(user_id, 'Nenhum usuário para enviar a mensagem.')
                return

            qtd_mensagens = 0
            lote_tamanho = 10
            intervalo = 2
            botoes = ReplyKeyboardMarkup(resize_keyboard=True)
            botoes.add(KeyboardButton(text='/start'))
            # Envio em lotes
            for i in range(0, len(users), lote_tamanho):
                lote = users[i:i + lote_tamanho]

                for user in lote:
                    try:
                        if mensagem['type'] == 'text':
                            await bot.send_message(user['id'], mensagem['content'], reply_markup=botoes)
                        elif mensagem['type'] == 'photo':
                            await bot.send_photo(user['id'], mensagem['content'],
                                                  caption=mensagem.get('caption'), reply_markup=botoes)
                            
                        elif mensagem['type'] == 'video':
                            await bot.send_video(user['id'], mensagem['content'],
                                                  caption=mensagem.get('caption'), reply_markup=botoes)
                        qtd_mensagens += 1
                    except Exception as e:
                        print(f"Erro ao enviar para {user['id']}: {e}")
                        continue

                await asyncio.sleep(intervalo)

        # Notifica o administrador
            await bot.send_message(user_id, f"Você enviou a mensagem para {qtd_mensagens} usuários!")

        #--------------- callback para comprovantes manuais ------------------
          # Extrair o message_id da callback data
    message_id = int(call.data.split('_')[1])
    historico_previas[call.from_user.id] = False
    # Buscar o ID do usuário que enviou a imagem
    user_id = user_images.get(message_id)
    
    if not user_id:
        #await bot.send_message(call.message.chat.id, 'Erro: não foi possível encontrar o usuário.')
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



async def registro_historico(mensagem, id_user):

    mensagens[id_user].append(mensagem)
    print(mensagens)

async def delete_mensagem_historico(id_user):
    items = mensagens[id_user]
    if len(items) > 0:
        for item in items:
            try:
                await bot.delete_message(item.chat.id, item.message_id)
            except Exception as e:
                pass
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


@bot.message_handler(content_types=['photo', 'video', 'text'])
async def handle_photo(message):
    if str(message.from_user.id) == str(admin):
            user_id = message.from_user.id
            print(mensagens_broadcast)
                # Determina o tipo de conteúdo recebido
            if message.content_type == 'text':
                mensagens_broadcast[user_id] = {'type': 'text', 'content': message.text, 'caption': None}
                print(mensagens_broadcast)
            elif message.content_type == 'photo':
                photo_id = message.photo[-1].file_id  # Maior resolução
                mensagens_broadcast[user_id] = {'type': 'photo', 'content': photo_id, 'caption': message.caption}
            elif message.content_type == 'video':
                video_id = message.video.file_id
                mensagens_broadcast[user_id] = {'type': 'video', 'content': video_id, 'caption': message.caption}
            else:
                await bot.send_message(user_id, 'Tipo de mensagem não suportado.')
                return
    

            # Finaliza o travamento e apresenta os botões de ação
            travar_disparo[user_id] = False
            markup = InlineKeyboardMarkup(row_width=2)
            bt_enviar = InlineKeyboardButton('Enviar', callback_data='enviar')
            bt_visualizar = InlineKeyboardButton('Visualizar', callback_data='visualizar')
            markup.add(bt_enviar, bt_visualizar)

            await bot.send_message(
                user_id,
                'Sua mensagem foi salva! Escolha uma ação abaixo:',
                reply_markup=markup
            )

    else:
        if message.content_type == 'text':
            pass

        elif message.chat.type == 'private':
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
 


@bot.message_handler(commands=['gerenciar', 'gerenciar_assinatura', 'gerente', 'assinantes'])
async def gerenciar_assinatura(message):
    print(message.from_user.id)
    if str(message.from_user.id) != str(admin):
        await bot.send_message(message.chat.id, 'Você não tem permissão para executar esta função.')
        return

    menu = InlineKeyboardMarkup(row_width=2)
    assinantes = Usuario().show_info_assinantes()

    if not assinantes:  # Verifica se a lista está vazia
        await bot.send_message(message.chat.id, 'Você não possui nenhuma assinatura.')
        return

    for assinante in assinantes:
        nome = assinante['nome']
        id = assinante['id']
        username = assinante['username']

        nome_bt = InlineKeyboardButton(f'{nome} ({username})', callback_data=f'gerenciar_{id}')
        menu.add(nome_bt)

    await bot.send_message(message.chat.id, 'Escolha uma assinatura para gerenciar', reply_markup=menu)


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

        