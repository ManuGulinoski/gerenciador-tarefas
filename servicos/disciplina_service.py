"""
Regras de negócio das disciplinas.

Responsável: Pessoa 1
NÃO importa tkinter. Em caso de erro de validação, lança ValueError("mensagem").
A tela captura o erro e mostra no messagebox.

Padrão usado em todas as funções que alteram dados:
    disciplinas, tarefas = armazenamento.carregar()
    ... altera as listas ...
    armazenamento.salvar(disciplinas, tarefas)
"""
from models.disciplina import Disciplina  # noqa: F401  (usado na implementação)
from repositorio import armazenamento     # noqa: F401
from utils.constantes import MAX_NOME_DISCIPLINA  # noqa: F401


def listar_disciplinas():
    """Retorna a lista de Disciplina, ordenada por nome."""
    # TODO (Pessoa 1)
    raise NotImplementedError


def buscar_disciplina(disciplina_id):
    """Retorna a Disciplina com esse id, ou None se não existir."""
    # TODO (Pessoa 1)
    raise NotImplementedError


def criar_disciplina(nome):
    """
    Cria e salva uma disciplina. Retorna a Disciplina criada.

    Validações (lançar ValueError com mensagem amigável):
    - nome vazio (lembre do .strip())
    - nome com mais de MAX_NOME_DISCIPLINA caracteres
    - já existe disciplina com o mesmo nome (comparar sem diferenciar
      maiúsculas/minúsculas: .lower())
    """
    # TODO (Pessoa 1)
    raise NotImplementedError


def editar_disciplina(disciplina_id, novo_nome):
    """
    Renomeia a disciplina. Mesmas validações de criar_disciplina,
    mas ignorando a própria disciplina na checagem de nome repetido.
    """
    # TODO (Pessoa 1)
    raise NotImplementedError


def contar_tarefas_da_disciplina(disciplina_id):
    """
    Retorna quantas tarefas estão ligadas a essa disciplina.
    A tela usa esse número no pop-up de confirmação:
    "Excluir 'Cálculo'? 5 tarefas também serão excluídas."
    """
    # TODO (Pessoa 1)
    raise NotImplementedError


def excluir_disciplina(disciplina_id):
    """
    Exclui a disciplina E todas as tarefas com esse disciplina_id
    (exclusão em cascata). A confirmação é feita pela tela, antes de chamar.
    """
    # TODO (Pessoa 1)
    raise NotImplementedError
