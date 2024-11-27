import stripe
from decouple import config

stripe.api_key = config('STRIPE_PROD')


preco_pt = [
    9.90,
    16.90,
    22.90,
    37.90,

]
preco_es = [
    11.90,
    16.90,
    24.90,
    49.90,
    
]
produtos = stripe.Product.list()


def formatar_moeda(preco, moeda):
    simbolos = {'usd': '$', 'brl': 'R$', 'eur': '€'}
    return f"{simbolos.get(moeda, moeda)}{preco:.2f}"



def show_product_pt():
    resultado = []
    for produto in produtos.data:
        preco = stripe.Price.list(product=produto.id)
        checkout = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': preco.data[0].id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        if preco.data[0].unit_amount / 100 in preco_pt:
            if produto.images:
                dictn = {'prod_id': produto.id,'nome': produto.name, 'imagem': produto.images[0],
                         'moeda': formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                         'url': checkout.url, 'id_checkout': checkout.id}
                
                resultado.append(dictn)
                
            else:
                dictn = {'prod_id': produto.id,'nome': produto.name,
                         'moeda': formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                         'url': checkout.url, 'id_checkout': checkout.id}
                
                resultado.append(dictn)
    return resultado



def show_product_es():
    resultado = []
    for produto in produtos.data:
        preco = stripe.Price.list(product=produto.id)
        checkout = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': preco.data[0].id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        if preco.data[0].unit_amount / 100 in preco_es:
            if produto.images:
                dictn = {'prod_id': produto.id, 'nome': produto.name, 'imagem': produto.images[0],
                         'moeda': formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency), 'url': checkout.url}
                resultado.append(dictn)
                
            else:
                dictn = {'prod_id': produto.id,'nome': produto.name, 'moeda': formatar_moeda(preco.data[0].unit_amount / 100, 'usd'), 'url': checkout.url}
                resultado.append(dictn)
    return resultado

def single_product(prod_id):
    produto = stripe.Product.retrieve(prod_id)
    preco = stripe.Price.list(product=produto.id)
    checkout = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price': preco.data[0].id,
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )
    if produto.images:
        dictn = {'prod_id': produto.id, 'nome': produto.name, 'imagem': produto.images[0],
                 'moeda': formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                 'url': checkout.url, 'id_checkout': checkout.id, 'preco': preco.data[0].unit_amount / 100}
        return dictn
    else:
        dictn = {'prod_id': produto.id,'nome': produto.name, 'imagem': None,
                 'moeda': formatar_moeda(preco.data[0].unit_amount / 100, preco.data[0].currency),
                 'url': checkout.url, 'id_checkout': checkout.id, 'preco': preco.data[0].unit_amount / 100}
        return dictn


def dict_plain(idioma):
    if idioma == 'espanhol':
        plain = {11.90: 'semanal', 16.90: 'mensal', 24.90: 'bimestral', 49.90: 'vitalicio'}
    elif idioma == 'portugues':
        plain = {9.90: 'semanal', 16.90: 'mensal', 22.90: 'bimestral', 37.90: 'vitalicio'}
    return plain


def list_products_first_once():
    produtos = stripe.Product.list()
    lista = []
    for produto in produtos.data:
        if  produto.name == 'Teste' or produto.name == 'Produto Exemplo' or produto.name == 'Assinatura Trimestral':
        
            pass
        else:
            nome = produto.name
            id = produto.id
            dictn = {'nome': nome, 'id': id}
            lista.append(dictn)
    return lista


def single_product_semanal():
    produto = stripe.Product.list()
    for p in produto.data:
        if p.name == 'DOPAMINAS SEMANAL':
            nome = p.name
            id = p.id
            desc = p.description
            preco = stripe.Price.list(product=p.id)
            preco_value = preco.data[0].unit_amount / 100
            imagem = p.images[0]
            checkout = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price': preco.data[0].id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='https://example.com/success',
                cancel_url='https://example.com/cancel',
            )
            dictn = {'nome': nome,'imagem': imagem, 'id': id, 'desc': desc, 'preco': preco_value, 'url': checkout.url, 'id_checkout': checkout.id}
            return dictn
        
def single_product_mensal():
    produto = stripe.Product.list()
    for p in produto.data:
        
        if p.name == 'DOPAMINAS MENSAL (PROMOÇAO)':
            nome = p.name
            id = p.id
            desc = p.description
            preco = stripe.Price.list(product=p.id)
            preco_value = preco.data[0].unit_amount / 100
            imagem = p.images[0]
            checkout = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price': preco.data[0].id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='https://example.com/success',
                cancel_url='https://example.com/cancel',
            )
            dictn = {'nome': nome,'imagem': imagem, 'id': id, 'desc': desc, 'preco': preco_value, 'url': checkout.url, 'id_checkout': checkout.id}
            return dictn



def produto_trimestral():
    produto = stripe.Product.list()
    for p in produto.data:
        if p.name == 'DOPAMINAS TRIMESTRAL':
            nome = p.name
            id = p.id
            desc = p.description
            preco = stripe.Price.list(product=p.id)
            preco_value = preco.data[0].unit_amount / 100
            imagem = p.images[0]
            checkout = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price': preco.data[0].id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
            )
            dictn = {'nome': nome,'imagem': imagem, 'id': id, 'desc': desc, 'preco': preco_value, 'url': checkout.url, 'id_checkout': checkout.id}
            return dictn

def produto_show(title):
    produto = stripe.Product.list()
    for p in produto.data:
        if p.name == title:
            nome = p.name
            id = p.id
            desc = p.description
            preco = stripe.Price.list(product=p.id)
            preco_value = preco.data[0].unit_amount / 100
            imagem = p.images[0]
            checkout = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price': preco.data[0].id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
            )
            if desc:
                dictn = {'nome': nome,'imagem': imagem, 'id': id, 'desc': desc, 'preco': preco_value, 'url': checkout.url, 'id_checkout': checkout.id}
                return dictn
            else:
                dictn = {'nome': nome,'imagem': imagem, 'id': id,  'preco': preco_value, 'url': checkout.url, 'id_checkout': checkout.id}
                return dictn
            

def bot_in_private(message):
    if message.chat.type == 'private':
        return True

      
