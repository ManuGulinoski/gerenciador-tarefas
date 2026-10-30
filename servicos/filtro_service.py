"""
Filtros da tela de Tarefas.

Responsável: Pessoa 2
NÃO importa tkinter. Usa tarefa_service.listar_tarefas() (Pessoa 1) para pegar as tarefas.
Enquanto o serviço da Pessoa 1 não estiver pronto, teste com armazenamento.carregar().
"""
from datetime import date, timedelta  # noqa: F401

from servicos import tarefa_service  # noqa: F401
from utils.constantes import (  # noqa: F401
    PRAZO_HOJE, PRAZO_ESTA_SEMANA, PRAZO_SEMANA_QUE_VEM,
)


def filtrar_tarefas(disciplina_id=None, tipo=None, status=None,
                    prioridade=None, prazo=None):
    """
    Retorna a lista de tarefas que passam em TODOS os filtros informados.
    Parâmetro None = sem filtro naquele campo.

    - disciplina_id: compare com tarefa.disciplina_id
    - tipo: compare com tarefa.tipo
    - status: compare com tarefa.status_atual() (para "Atrasada" funcionar)
    - prioridade: compare com tarefa.prioridade()
    - prazo: PRAZO_HOJE, PRAZO_ESTA_SEMANA ou PRAZO_SEMANA_QUE_VEM
        segunda-feira desta semana = hoje - timedelta(days=hoje.weekday())
        domingo desta semana       = segunda + timedelta(days=6)
        semana que vem             = segunda + 7 dias até domingo + 7 dias
    """
    # TODO (Pessoa 2)
    raise NotImplementedError
