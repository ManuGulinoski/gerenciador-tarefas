"""
Frase motivacional da API ZenQuotes.

Responsável: Pessoa 4
NÃO importa tkinter.
"""
import requests  # noqa: F401

from utils.constantes import URL_ZENQUOTES, FRASE_RESERVA  # noqa: F401


def buscar_frase():
    """
    Retorna uma tupla (frase, autor).

    A API responde uma lista assim: [{"q": "texto da frase", "a": "autor", ...}]
    Use requests.get(URL_ZENQUOTES, timeout=5).

    Se der QUALQUER erro (sem internet, timeout, resposta estranha),
    retorne FRASE_RESERVA. O app nunca pode travar por causa da API.
    """
    # TODO (Pessoa 4)
    raise NotImplementedError
