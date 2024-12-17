import stripe
from decouple import config
stripe.api_key = config("STRIPE_PROD")


preco_pt = {
    'semanal': 6.99,
    'mensal': 13.99,
    'trimestral': 26.99,
   
}

preco_es = {
    'semanal': 6.99,
    'mensal': 13.99,
    'trimestral': 26.99,
   
}


preco_br = {
    'semanal': 9.99,
    'mensal': 19.99,
    'trimestral': 29.99,
   
}


language = {
    "espanhol": {
        "inicio": """¡Tardaste, pero lo conseguiste, eh?! Este es el mejor grupo de Telegram, basta de caer en estafas.""",
        "inicio2": "¡Hola, Bienvenido de nuevo 🙂",
        "produtos": "🎟️ Productos disponibles 🎟️",
        "call_interesse": "Estás interesado en unirte al mejor canal de putas del mundo ?",
        "cb_nao_interesse": "¡Gracias por tu interés, hasta luego 😉",
        "pg_instrucao": "Realiza el pago y envía una foto del comprobante; este será enviado para la aprobación de un administrador, y recibirás un enlace de acceso después de la aprobación",
        "oferta_semanal": f"Sigue con el plan semanal {str(preco_es['semanal'])} ",
        'oferta_exclusiva': f"Quiero una oferta exclusiva {str(preco_es['mensal'])} ",
        "oferta_apresentacao": f"Tenemos una oferta exclusiva para ti: Paga una semana más y recibe dos semanas gratis\n\n Recibirás en total: 1 mes de acceso por € {str(preco_es['mensal'])}",
        "obrigado": 'Gracias por suscribirse',
        '5dias': 'Su suscripción caducará en 5 días. Vuelve a firmar un plan. /start',
        '4dias': 'Su suscripción caducará en 4 días. Vuelve a firmar un plan. /start',
        '3dias': 'Su suscripción caducará en 3 días. Vuelve a firmar un plan. /start',
        '2dias': 'Su suscripción caducará en 2 días. Vuelve a firmar un plan. /start',
        '1dias': 'Su suscripción caducará en 1 día. Vuelve a firmar un plan. /start',
        '3min': 'Su suscripción caducará en 30 min. Vuelve a firmar un plan. /start.',
        'expirado': 'Su suscripción ha caducado. Vuelve a firmar un plan. /start.',
        'cta1': f'Quiero suscribirme al vip semanal: €{str(preco_es["semanal"])} 🔞',
        'plano': 'Elige tu plan',
        'mensal': f'🔞 Mensual € {str(preco_es["mensal"])}',
        'semanal': f'🔥 Semanal € {str(preco_es["semanal"])}',
        'trimestral': f'😈 Trimestral € {str(preco_es["trimestral"])}',
        'voltar_semanal': '🔞 Quiero el semanal',
        "voltar_mensal": '🔞 Quiero el mensual',
        'voltar_trimestral': '😈 Quiero el trimestral',
        'mbway': 'Pagar con Mbway',
        'bizum': 'Pagar con Bizum',
        'esperando_pg': 'Esperando pago...',
        'previa': '🚧 Confira una previa del nuestro contenido exclusivo 🚧',
        'sim': 'Sí',
        'nao': 'No',
        'selecionado': 'Seleccionaste el plan',
        'suporte': '💬 Si tienes alguna duda, pregunta o sugerencia, contáctanos en nuestro canal de suporte.',
        'bt_suporte': '💬 Suporte',
    },
    
    "portugues": {
        "inicio": """Demorou, mas conseguiste, hein?! Este é o melhor grupo do Telegram, chega de cair em esquemas...""",
        "inicio2": "Olá, Bem-vindo de volta 🙂",
        "produtos": "🎟️ Produtos disponíveis 🎟️",
        "call_interesse": "Tem interesse em entrar no melhor canal de pornografia do mundo?",
        "cb_nao_interesse": "Obrigado pelo seu interesse, até mais 😉",
        "pg_instrucao": "Realize o pagamento e envie uma foto do comprovativo; será enviado para aprovação de um administrador e receberá um link de acesso após a aprovação.",
        "oferta_semanal": f"Siga com o plano semanal  {str(preco_pt['semanal'])} ",
        "oferta_exclusiva": f"Quero uma oferta exclusiva {str(preco_pt['mensal'])} ",
        "oferta_apresentacao": f"Temos uma oferta exclusiva para si: Pague mais uma semana e receba mais duas semanas grátis.\n\n Receberá no total: 1 mês de acesso por € {str(preco_pt['mensal'])}.",
        "obrigado": 'Obrigado por subscrever.',
        '5dias': 'A sua subscrição expirará em 5 dias. Renove o plano novamente /start.',
        '4dias': 'A sua subscrição expirará em 4 dias. Renove o plano novamente /start.',
        '3dias': 'A sua subscrição expirará em 3 dias. Renove o plano novamente /start.',
        '2dias': 'A sua subscrição expirará em 2 dias. Renove o plano novamente /start.',
        '1dias': 'A sua subscrição expirará em 1 dia. Renove o plano novamente /start.',
        '3min': 'A sua subscrição expirará em 30 minutos. Renove o plano novamente /start.',
        'expirado': 'A sua subscrição expirou. Renove o plano novamente /start.',
        'cta1': f'Quero subscrever ao VIP semanal: €{str(preco_pt["semanal"])} 🔞',
        'plano': 'Escolha o seu plano',
        'mensal': f'🔞 Mensal € {str(preco_pt["mensal"])}',
        'semanal': f'🔥 Semanal € {str(preco_pt["semanal"])}',
        'trimestral': f'😈 Trimestral € {str(preco_pt["trimestral"])}',
        'voltar_semanal': '🔞 Quero o semanal',
        "voltar_mensal": '🔞 Quero o mensal',
        'voltar_trimestral': '😈 Quero o trimestral',
        'mbway': 'Pagar com Mbway',
        'bizum': 'Pagar com Bizum',
        'esperando_pg': 'A aguardar pagamento...',
        'previa': '🚧 Confira uma prévia do nosso conteúdo exclusivo 🚧',
        'selecionado': 'Selecionaste o plano',
        'suporte': '💬 Se você tiver alguma dúvida, pergunte ou sugira algo, entre em contato no nosso canal de suporte.',
        'bt_suporte': '💬 Suporte',
    },
    
    "portugues_br": {
        "inicio": """Demorou mas conseguiu ein?! Esse é o melhor grupo do Telegram, chega de cair em golpes..""",
        "inicio2": "Olá, Bem-vindo de volta 🙂",
        "produtos": "🎟️ Produtos disponíveis 🎟️",
        "call_interesse": "Tem interesse em entrar no melhor canal de putaria do mundo?",
        "cb_nao_interesse": "Obrigado pelo seu interesse, até mais 😉",
        "pg_instrucao": "Realize o pagamento e envie uma foto do comprovante; será enviado para aprovação de um administrador e você receberá um link de acesso após a aprovação.",
        "oferta_semanal": f"Siga com o plano semanal R$ {str(preco_br['semanal'])} ",
        "oferta_exclusiva": f"Quero uma oferta exclusiva R$ {str(preco_br['mensal'])} ",
        "oferta_apresentacao": f"Temos uma oferta exclusiva para você: Pague mais uma semana e receba mais duas semanas grátis.\n\n Você receberá no total: 1 mês de acesso por R$ {str(preco_br['mensal'])} ",
        "obrigado": 'Obrigado por se inscrever.',
        '5dias': 'Sua assinatura expirará em 5 dias. Renove o plano novamente /start.',
        '4dias': 'Sua assinatura expirará em 4 dias. Renove o plano novamente /start.',
        '3dias': 'Sua assinatura expirará em 3 dias. Renove o plano novamente /start.',
        '2dias': 'Sua assinatura expirará em 2 dias. Renove o plano novamente /start.',
        '1dias': 'Sua assinatura expirará em 1 dia. Renove o plano novamente /start.',
        '3min': 'Sua assinatura expirará em 30 minutos. Renove o plano novamente /start.',
        'expirado': 'Sua assinatura expirou. Renove o plano novamente /start.',
        'cta1': f'Quero assinar o VIP semanal: R${str(preco_br["semanal"])} 🔞',
        'plano': 'Escolha seu plano',
        'mensal': f'🔞 Mensal R$ {str(preco_br["mensal"])}',
        'semanal': f'🔥 Semanal R$ {str(preco_br["semanal"])}',
        'trimestral': f'😈 Trimestral R$ {str(preco_br["trimestral"])}',
        'voltar_semanal': '🔞 Quero o semanal',
        "voltar_mensal": '🔞 Quero o mensal',
        'voltar_trimestral': '😈 Quero o trimestral',
        'mbway': 'Pagar com Mbway',
        'bizum': 'Pagar com Bizum',
        'esperando_pg': 'Esperando pagamento...',
        'previa': '🚧 Confira uma prévia do nosso conteúdo exclusivo 🚧',
        'sim': 'Sim',
        'nao': 'Não',
        'selecionado': 'Você selecionou o plano',
        'suporte': '💬 Se você tiver alguma dúvida, pergunte ou sugira algo, entre em contato no nosso canal de suporte.',
        'bt_suporte': '💬 Suporte',
        'escolha': 'Escolha'
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