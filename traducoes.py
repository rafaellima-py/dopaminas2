import stripe
from decouple import config
stripe.api_key = config("STRIPE_PROD")


preco_pt = {
    'semanal': 7.99,
    'mensal': 19.99,
    'trimestral': 39.99,
   
}

preco_es = {
    'semanal': 7.99,
    'mensal': 19.99,
    'trimestral': 39.99,
   
}


preco_br = {
    'semanal': 25.99,
    'mensal': 49.99,
    'trimestral': 79.99,
   
}


language = {
    "espanhol": {
        "inicio": """ 
💎INCESTO+18 🫦
💎AMAMANTAR AL HIJO‼️
💎 CONTENIDO RESTRINGIDO 😈
💎 Celebridades FAMOSAS FILTRADAS 👀
💎 NUEVAS 18+ 👅
💎AFICIONADO 🔥
💎 CONTROVERSIAL +18 🥵
💎 MILF 👵🏻
💎VIDAS🎬
💎FAVELADAS🔥
💎ANAL 😈
💎MAMADAS 👄""",
        "inicio2": "¡Hola, Bienvenido de nuevo 🙂",
        "produtos": "🎟️ Productos disponibles 🎟️",
        "call_interesse": "Estás interesado en unirte al mejor canal de putas del mundo ?",
        "cb_nao_interesse": "¡Gracias por tu interés, hasta luego 😉",
        "pg_instrucao": "Realiza el pago y envía una foto del comprobante; este será enviado para la aprobación de un administrador, y recibirás un enlace de acceso después de la aprobación",
        "oferta_semanal": "Sigue con el plan semanal",
        'oferta_exclusiva': "Quiero una oferta exclusiva",
        "oferta_apresentacao": "Tenemos una oferta exclusiva para ti: Paga una semana más y recibe dos semanas gratis\n\n Recibirás en total: 1 mes de acceso por €16,00",
        "obrigado": 'Gracias por suscribirse',
        '5dias': 'Su suscripción caducará en 5 días. Vuelve a firmar un plan. /start',
        '4dias': 'Su suscripción caducará en 4 días. Vuelve a firmar un plan. /start',
        '3dias': 'Su suscripción caducará en 3 días. Vuelve a firmar un plan. /start',
        '2dias': 'Su suscripción caducará en 2 días. Vuelve a firmar un plan. /start',
        '1dias': 'Su suscripción caducará en 1 día. Vuelve a firmar un plan. /start',
        '3min': 'Su suscripción caducará en 30 min. Vuelve a firmar un plan. /start.',
        'expirado': 'Su suscripción ha caducado. Vuelve a firmar un plan. /start.',
        'cta1': 'Quiero suscribirme al vip € 8,00 🔞',
        'plano': 'Elige tu plan',
        'mensal': '🔞 Mensual € 25.99',
        'semanal': '🔥 Semanal € 15.99',
        'trimestral': '😈 Trimestral € 38.99',
        'mbway': 'Pagar con Mbway',
        'bizum': 'Pagar con Bizum',
        'esperando_pg': 'Esperando pago...',
        'previa': '🚧 Confira una previa del nuestro contenido exclusivo 🚧',
        'sim': 'Sí',
        'nao': 'No'
    },
    
    "portugues": {
        "inicio": """
💎INCESTO+18 🫦
💎AMAMENTAR O FILHO‼️
💎 CONTEÚDO RESTRITO 😈
💎 VAZADOS DE FAMOSAS 👀
💎 NOVAS +18 👅
💎 AMADOR 🔥
💎 POLÉMICOS +18 🥵
💎 MILF 👵🏻
💎 LIVES 🎬
💎 FAVELADAS 🔥
💎 ANAL 😈
💎 BOQUETES 👄
""",
        "inicio2": "Olá, Bem-vindo de volta 🙂",
        "produtos": "🎟️ Produtos disponíveis 🎟️",
        "call_interesse": "Tem interesse em entrar no melhor canal de pornografia do mundo?",
        "cb_nao_interesse": "Obrigado pelo seu interesse, até mais 😉",
        "pg_instrucao": "Realize o pagamento e envie uma foto do comprovativo; será enviado para aprovação de um administrador e receberá um link de acesso após a aprovação.",
        "oferta_semanal": "Siga com o plano semanal",
        "oferta_exclusiva": "Quero uma oferta exclusiva",
        "oferta_apresentacao": "Temos uma oferta exclusiva para si: Pague mais uma semana e receba mais duas semanas grátis.\n\n Receberá no total: 1 mês de acesso por €16,00.",
        "obrigado": 'Obrigado por subscrever.',
        '5dias': 'A sua subscrição expirará em 5 dias. Renove o plano novamente /start.',
        '4dias': 'A sua subscrição expirará em 4 dias. Renove o plano novamente /start.',
        '3dias': 'A sua subscrição expirará em 3 dias. Renove o plano novamente /start.',
        '2dias': 'A sua subscrição expirará em 2 dias. Renove o plano novamente /start.',
        '1dias': 'A sua subscrição expirará em 1 dia. Renove o plano novamente /start.',
        '3min': 'A sua subscrição expirará em 30 minutos. Renove o plano novamente /start.',
        'expirado': 'A sua subscrição expirou. Renove o plano novamente /start.',
        'cta1': 'Quero subscrever ao VIP € 8,00 🔞',
        'plano': 'Escolha o seu plano',
        'mensal': f'🔞 Mensal € {str(preco_pt["mensal"])}',
        'semanal': f'🔥 Semanal € {str(preco_pt["semanal"])}',
        'trimestral': f'😈 Trimestral € {str(preco_pt["trimestral"])}',
        'mbway': 'Pagar com Mbway',
        'bizum': 'Pagar com Bizum',
        'esperando_pg': 'A aguardar pagamento...',
        'previa': '🚧 Confira uma prévia do nosso conteúdo exclusivo 🚧',
    },
    
    "portugues_br": {
        "inicio": """
💎INCESTO+18 🫦
💎MAMANDO O FILHO‼️
💎 CONTEÚDO RESTRITO 😈
💎 VAZADOS DE FAMOSAS 👀
💎 NOVINHAS +18 👅
💎 AMADOR 🔥
💎 POLÊMICOS +18 🥵
💎 MILF 👵🏻
💎 LIVES 🎬
💎 FAVELADAS 🔥
💎 ANAL 😈
💎 BOQUETES 👄
""",
        "inicio2": "Olá, Bem-vindo de volta 🙂",
        "produtos": "🎟️ Produtos disponíveis 🎟️",
        "call_interesse": "Tem interesse em entrar no melhor canal de putaria do mundo?",
        "cb_nao_interesse": "Obrigado pelo seu interesse, até mais 😉",
        "pg_instrucao": "Realize o pagamento e envie uma foto do comprovante; será enviado para aprovação de um administrador e você receberá um link de acesso após a aprovação.",
        "oferta_semanal": "Siga com o plano semanal",
        "oferta_exclusiva": "Quero uma oferta exclusiva",
        "oferta_apresentacao": "Temos uma oferta exclusiva para você: Pague mais uma semana e receba mais duas semanas grátis.\n\n Você receberá no total: 1 mês de acesso por €16,00.",
        "obrigado": 'Obrigado por se inscrever.',
        '5dias': 'Sua assinatura expirará em 5 dias. Renove o plano novamente /start.',
        '4dias': 'Sua assinatura expirará em 4 dias. Renove o plano novamente /start.',
        '3dias': 'Sua assinatura expirará em 3 dias. Renove o plano novamente /start.',
        '2dias': 'Sua assinatura expirará em 2 dias. Renove o plano novamente /start.',
        '1dias': 'Sua assinatura expirará em 1 dia. Renove o plano novamente /start.',
        '3min': 'Sua assinatura expirará em 30 minutos. Renove o plano novamente /start.',
        'expirado': 'Sua assinatura expirou. Renove o plano novamente /start.',
        'cta1': 'Quero assinar o VIP € 8,00 🔞',
        'plano': 'Escolha seu plano',
        'mensal': f'🔞 Mensal R$ {str(preco_br["mensal"])}',
        'semanal': f'🔥 Semanal R$ {str(preco_br["semanal"])}',
        'trimestral': f'😈 Trimestral R$ {str(preco_br["trimestral"])}',
        'mbway': 'Pagar com Mbway',
        'bizum': 'Pagar com Bizum',
        'esperando_pg': 'Esperando pagamento...',
        'previa': '🚧 Confira uma prévia do nosso conteúdo exclusivo 🚧',
        'sim': 'Sim',
        'nao': 'Não'
    }
}


produtos = stripe.Product.list()


def formatar_moeda(preco, moeda):
    simbolos = {"usd": "$", "brl": "R$", "eur": "€"}
    return f"{simbolos.get(moeda, moeda)}{preco:.2f}"



def show_product_pt():
    resultado = []
    for produto in produtos.data:
        preco = stripe.Price.list(product=produto.id)
        checkout = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": preco.data[0].id,
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
        if preco.data[0].unit_amount / 100 in preco_pt:
            if produto.images:
                dictn = {"prod_id": produto.id,"nome": produto.name, "imagem": produto.images[0],
                         "moeda": formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                         "url": checkout.url, "id_checkout": checkout.id}
                
                resultado.append(dictn)
                
            else:
                dictn = {"prod_id": produto.id,"nome": produto.name,
                         "moeda": formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                         "url": checkout.url, "id_checkout": checkout.id}
                
                resultado.append(dictn)
    return resultado



def show_product_es():
    resultado = []
    for produto in produtos.data:
        preco = stripe.Price.list(product=produto.id)
        checkout = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": preco.data[0].id,
                    "quantity": 1,
                },
            ],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
        if preco.data[0].unit_amount / 100 in preco_es:
            if produto.images:
                dictn = {"prod_id": produto.id, "nome": produto.name, "imagem": produto.images[0],
                         "moeda": formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency), "url": checkout.url}
                resultado.append(dictn)
                
            else:
                dictn = {"prod_id": produto.id,"nome": produto.name, "moeda": formatar_moeda(preco.data[0].unit_amount / 100, "usd"), "url": checkout.url}
                resultado.append(dictn)
    return resultado

def single_product(prod_id):
    produto = stripe.Product.retrieve(prod_id)
    preco = stripe.Price.list(product=produto.id)
    checkout = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price": preco.data[0].id,
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
    )
    if produto.images:
        dictn = {"prod_id": produto.id, "nome": produto.name, "imagem": produto.images[0],
                 "moeda": formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                 "url": checkout.url, "id_checkout": checkout.id, "preco": preco.data[0].unit_amount / 100}
        return dictn
    else:
        dictn = {"prod_id": produto.id,"nome": produto.name, "imagem": None,
                 "moeda": formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                 "url": checkout.url, "id_checkout": checkout.id, "preco": preco.data[0].unit_amount / 100}
        return dictn


def dict_plain(idioma):
    if idioma == "espanhol":
        plain = {11.90: "semanal", 16.90: "mensal", 24.90: "bimestral", 49.90: "vitalicio"}
    elif idioma == "portugues":
        plain = {9.90: "semanal", 16.90: "mensal", 22.90: "bimestral", 37.90: "vitalicio"}
    return plain
#print((single_product("prod_QuvWYoJ6uKPzB3")))