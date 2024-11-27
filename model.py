from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta

class UsuarioModel(BaseModel):
    id : str
    nome : str
    username: str
    idioma : Optional[str] = None
    qt_assinatura : Optional[int] = 0

class UsuarioAssinaturaModel(BaseModel):
    id : str
    nome :  Optional[str] = 'None'
    username: str = 'Usuario desconhecido'
    idioma : Optional[str]
    assinatura : bool = False
    valor : Optional[float] = None
    criado : Optional[datetime] = None
    expira : Optional[datetime] = None

usuarios = {
       1: {
           'nome': 'Rafael',
           'username': 'rafael',
           'idioma': 'portugues',
           'assinatura': 'mensal',
           'valor': 10,
           'tipo': 'pagamento',
           'criado': '2021-01-01',
           'expira': '2021-02-01'
       },
       2: {
           'nome': 'Rafael',
           'username': 'rafael',
           'idioma': 'espanhol',
           'assinatura': 'mensal',
           'valor': 10,
           'tipo': 'pagamento',
           
       },
}

# ler 

