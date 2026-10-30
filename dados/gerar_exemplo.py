"""
Recria o dados.json com disciplinas e tarefas de exemplo.
Os prazos são calculados a partir do dia em que o script roda,
então sempre existem tarefas atrasadas, para hoje e de cada prioridade.

Responsável: Pessoa 2
Para rodar (da pasta do projeto):  python -m dados.gerar_exemplo
"""
from datetime import date, timedelta  # noqa: F401

from models.disciplina import Disciplina  # noqa: F401
from models.tarefa import Tarefa  # noqa: F401
from repositorio import armazenamento  # noqa: F401
from utils.constantes import (  # noqa: F401
    TIPO_PROVA, TIPO_TRABALHO, TIPO_EXERCICIO,
    STATUS_A_FAZER, STATUS_EM_ANDAMENTO, STATUS_CONCLUIDA,
)


def gerar():
    """
    1. Criar 3 disciplinas (ex.: Cálculo, Programação, Banco de Dados).
    2. Criar cerca de 12 tarefas com prazo = date.today() + timedelta(days=n),
       usando n = -3, -1 (atrasadas), 0 (hoje), 2, 3 (alta), 5, 7 (média), 10, 15 (baixa).
       Misturar tipos, status e disciplinas; deixar algumas concluídas.
    3. armazenamento.salvar(disciplinas, tarefas)
    """
    # TODO (Pessoa 2)
    raise NotImplementedError


if __name__ == "__main__":
    gerar()
    print("dados.json recriado com dados de exemplo.")
