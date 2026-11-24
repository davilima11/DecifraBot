"""Testes da versão web (index.html), que roda o mesmo código Python no navegador."""
import json
from pathlib import Path

from decifra import ponte
from web.manifesto import listar

RAIZ = Path(__file__).resolve().parent.parent


def test_lista_de_arquivos_do_site_esta_atualizada():
    # se alguém criar um arquivo novo em decifra/ e esquecer de rodar web/manifesto.py, o site quebra
    salvo = json.loads((RAIZ / "web" / "arquivos.json").read_text(encoding="utf-8"))
    assert salvo == listar()
    assert all((RAIZ / arquivo).exists() for arquivo in salvo)


def test_ponte_devolve_json_que_a_pagina_entende():
    ponte.limpar()
    resposta = json.loads(ponte.responder('import os\nos.remove("a.txt")'))
    assert resposta["tipo"] == "explicacao"
    assert resposta["linhas"][0] == {"numero": 1, "texto": resposta["linhas"][0]["texto"], "nivel": 0}
    assert resposta["alertas"] and "apaga o arquivo" in resposta["alertas"][0]["texto"]
    assert resposta["conceitos"] and resposta["explicacao"]
    pergunta = json.loads(ponte.responder("o que é uma lista?"))
    assert pergunta["tipo"] == "texto" and "lista" in pergunta["texto"]


def test_linha_com_crase_nao_quebra_a_citacao():
    ponte.limpar()
    ponte.responder("const t = `oi ${nome}`;\nconsole.log(t);")
    resposta = json.loads(ponte.responder("explica a linha 1"))
    assert "`` const t = `oi ${nome}`; ``" in resposta["texto"]
