"""
Regras de negócio das tarefas.

Responsável: Pessoa 1
Os filtros ficam em filtro_service.py (Pessoa 2).
NÃO importa tkinter. Em caso de erro de validação, lança ValueError("mensagem").
"""
from models.tarefa import Tarefa      # noqa: F401
from repositorio import armazenamento  # noqa: F401
from utils.constantes import (         # noqa: F401
    MAX_NOME_TAREFA, MAX_DESCRICAO_TAREFA,
    TIPOS, STATUS_SELECIONAVEIS, STATUS_CONCLUIDA,
)


def listar_tarefas():
    """Retorna todas as tarefas, ordenadas por prazo (mais próximo primeiro)."""
    # TODO (Pessoa 1)
    raise NotImplementedError


def buscar_tarefa(tarefa_id):
    """Retorna a Tarefa com esse id, ou None."""
    # TODO (Pessoa 1)
    raise NotImplementedError


def _validar(nome, tipo, prazo, disciplina_id, status, descricao):
    """
    Função interna usada por criar e editar. Lança ValueError se:
    - nome vazio ou maior que MAX_NOME_TAREFA
    - tipo não está em TIPOS
    - prazo é None (a tela deve converter o texto da data para date antes)
    - disciplina_id vazio ou inexistente
    - status não está em STATUS_SELECIONAVEIS
    - descricao maior que MAX_DESCRICAO_TAREFA
    """
    # TODO (Pessoa 1)
    raise NotImplementedError


def criar_tarefa(nome, tipo, prazo, disciplina_id,
                 status, descricao="", cor=None):
    """
    Valida, cria a Tarefa, salva no JSON e retorna a tarefa criada.
    'prazo' chega como datetime.date.
    """
    # TODO (Pessoa 1)
    raise NotImplementedError


def editar_tarefa(tarefa_id, nome, tipo, prazo, disciplina_id,
                  status, descricao="", cor=None):
    """Valida e atualiza todos os campos da tarefa existente."""
    # TODO (Pessoa 1)
    raise NotImplementedError


def excluir_tarefa(tarefa_id):
    """Remove a tarefa. A confirmação é feita pela tela antes de chamar."""
    # TODO (Pessoa 1)
    raise NotImplementedError


def concluir_tarefa(tarefa_id):
    """Atalho do ícone de concluir: muda o status para STATUS_CONCLUIDA."""
    # TODO (Pessoa 1)
    raise NotImplementedError

