"""Memória do DecifraBot.

- Curta: as últimas mensagens da conversa. Código não entra aqui, só um aviso de que foi colado.
- Média: o último código (já com senhas escondidas), a linguagem e a explicação dele,
  para responder "explica a linha 4" ou "resume".
- Longa: não existe de propósito. O código da pessoa não fica guardado depois da conversa.
"""
from collections import deque


class Memoria:
    TAMANHO_CURTA = 6

    def __init__(self):
        self.curta = deque(maxlen=self.TAMANHO_CURTA)
        self.limpar_media()

    def registrar(self, autor, texto):
        self.curta.append((autor, texto))

    def guardar_codigo(self, codigo, linguagem, resultado):
        self.codigo = codigo
        self.linguagem = linguagem
        self.resultado = resultado

    def limpar_media(self):
        self.codigo = None
        self.linguagem = None
        self.resultado = None
        self.linguagem_preferida = None

    def limpar(self):
        self.curta.clear()
        self.limpar_media()
