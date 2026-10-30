"""
Números usados na Home (big numbers e gráficos).

Responsável: Pessoa 4
NÃO importa tkinter nem matplotlib. Só calcula e devolve dicionários.
Use tarefa_service.listar_tarefas() para obter as tarefas.
"""
from servicos import tarefa_service  # noqa: F401
from utils.constantes import STATUS_TODOS, TIPOS  # noqa: F401


def big_numbers():
    """
    Retorna:
    {
        "total": int,
        "concluidas": int,
        "atrasadas": int,
        "para_hoje": int,   # prazo == hoje e não concluída (decidam em equipe)
    }
    """
    # TODO (Pessoa 4)
    raise NotImplementedError


def contagem_por_status():
    """
    Retorna {"A fazer": n, "Em andamento": n, "Concluída": n, "Atrasada": n}
    Use tarefa.status_atual(). Inclua todos os status, mesmo com 0.
    """
    # TODO (Pessoa 4)
    raise NotImplementedError


def contagem_por_tipo():
    """Retorna {"Prova": n, "Trabalho": n, "Exercício": n}"""
    # TODO (Pessoa 4)
    raise NotImplementedError
